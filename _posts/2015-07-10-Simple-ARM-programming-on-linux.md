---
layout: post
title: Compiling and debugging ARM assembly with GDB and qemu
---

Recentely I've been involved with simple ARM assembly programming at university.
The toolchains provided to me were either clunky (CYGWIN on Windows) or totally
 broken (the linux binaries), so I had to come up with something.

## Installing the ARM toolchain
The first thing you need to compile an ARM program is a compiler, of course.
Fortunately, the ARM architecture is widely supported nowadays, therefore this won't be a problem. <br>
I've choosen the GCC-based toolchain, which you can probably find in your favourite distro's package repository.

In my case (Archlinux) I had to install the following packages from AUR:
{% highlight text %}
arm-none-eabi-gcc
arm-none-eabi-gdb
{% endhighlight %}
The last one is actually the debugger, but we'll need it later anyway.

To test your compiler, try to save this snippet in a file, e.g. `empty.s`
{% highlight asm %}
.text
.global _start
_start:
    mov r0, #1
    b   _start
{% endhighlight %}
To compile it, we will assemble and link it:
{% highlight text %}
arm-none-eabi-as empty.s -o empty.o
arm-none-eabi-ld empty.o -o empty
{% endhighlight %}

I everything goes well, you should obtain an `empty` ELF executable.
Unfortunately, unless you have an ARM machine at hand, it will be difficult to execute it: the easiest way to overcome this is to use `qemu`.

## Debugging with qemu and GDB
After having installed qemu, you will be able to run your program as follows:
{% highlight text %}
qemu-arm executable
{% endhighlight %}
To understand what is really going on in the program, we'll connect `gdb` to qemu, that will serve as a gdb server.
We first need to be sure that the program has been built with debugging symbols turned on:
{% highlight text %}
arm-none-eabi-as empty.s -g -o empty.o
arm-none-eabi-ld empty.o -o empty
{% endhighlight %}

To run our program, we'll use:
{% highlight text %}
qemu-arm -singlestep -g 1234 empty
{% endhighlight %}
so that it halts on the first instruction (useful for debugging). The -g parameter specifies which port will be used by the gdb server to listen for clients.

There are many GUIs one can use to make GDB more palatable, but none of them satisfied me, and I sticked to the integrated terminal UI that gdb offers.

Here's what you need to do to connect to qemu:
{% highlight text %}
➜ arm-none-eabi-gdb
GNU gdb (GDB) 7.9.1
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later > <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "--host=x86_64-unknown-linux-gnu --target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) file empty
Reading symbols from empty...done.
(gdb) target remote localhost:1234
Remote debugging using localhost:1234
_start () at empty.s:4
4	    mov r0, #1
(gdb)
{% endhighlight %}

We first load the debugging symbols using the `file` command, then we connect to our remote target.

##Crash course on GDB
The TUI provided from GDB is good enough to debug simple (and complex) programs: press `Ctrl+x` and then `A` to active it: above your usual GDB command prompt, you will see the source being debugged.
Issue this command to have a good view of the registers.
{% highlight text %}
layout regs
{% endhighlight %}

You should end up with something like this:
![GDB session](/img/2015-07-10-232039_1440x900_scrot.png "ugh...")

These are some basic commands to know, only one key press away:

* **s** Step by a single instruction
* **b** Set a breakpoint. You can use this in many ways, like `b source.s:312` where source.s is the source and 312 the line number where you want the breakpoint.
* **c** Continue until next breakpoint

For more commands, like setting watchs or printing memory data, you can follow the [official guide](https://sourceware.org/gdb/onlinedocs/gdb/).
