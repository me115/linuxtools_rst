.. _objdump:

objdump 
====================

ogjdump工具用来显示二进制文件的信息，就是以一种可阅读的格式让你更多地了解二进制文件可能带有的附加信息。


参数说明
--------------------
选项详解：
- --archive-headers
    -a 显示档案库的成员信息，与 ar tv 类似

    objdump -a libpcap.a
    和 ar -tv libpcap.a 显示结果比较比较
    显然这个选项没有什么意思。

- --adjust-vma=offset
    When  dumping  information, first add offset to all
    the section addresses.  This is useful if the  sec-
    tion  addresses  do  not correspond  to the symbol
    table, which can happen when  putting  sections  at
    particular  addresses when using a format which can
    not represent section addresses, such as a.out.

- --target=bfdname
    指定目标码格式。这不是必须的，objdump能自动识别许多格式，
    比如：objdump -b oasys -m vax -h fu.o
    显示fu.o的头部摘要信息，明确指出该文件是Vax系统下用Oasys
    编译器生成的目标文件。objdump -i将给出这里可以指定的
    目标码格式列表

- -C 将底层的符号名解码成用户级名字，除了去掉所有开头的下划线之外，还使得C++函数名以可理解的方式显示出来。

- --debugging 
    显示调试信息。企图解析保存在文件中的调试信息并以C语言的语法显示出来。仅仅支持某些类型的调试信息。

- -d 反汇编那些含有指令机器码的section

- --disassemble-all
    -D 与 -d 类似，但反汇编所有section

- --prefix-addresses
    反汇编的时候，显示每一行的完整地址。这是一种比较老的反汇编格式。显示效果并不理想，但可能会用到其中的某些显示，自己可以对比。

- --disassemble-zeroes 一般反汇编输出将省略大块的零，该选项使得这些零块也被反汇编。

- -EB / -EL  / --endian={big|little}
    这个选项将影响反汇编出来的指令。
    little-endian就是我们当年在dos下玩汇编的时候常说的高位在高地址，
    x86都是这种。

- --file-headers
    -f 显示objfile中每个文件的整体头部摘要信息。

- --section-headers
    --headers
    -h 显示目标文件各个section的头部摘要信息。

- --help 简短的帮助信息。

- --info
    -i 显示对于 -b 或者 -m 选项可用的架构和目标格式列表。

- --section=name
    -j name 仅仅显示指定section的信息

- --line-numbers
    -l 用文件名和行号标注相应的目标代码，仅仅和-d、-D或者-r一起使用使用-ld和使用-d的区别不是很大，在源码级调试的时候有用，要求编译时使用了-g之类的调试编译选项。

- --architecture=machine
    -m machine
    指定反汇编目标文件时使用的架构，当待反汇编文件本身没有描述架构信息的时候(比如S-records)，这个选项很有用。可以用-i选项列出这里能够指定的架构。

- --reloc
    -r 显示文件的重定位入口。如果和-d或者-D一起使用，重定位部分以反汇编后的格式显示出来。

- --dynamic-reloc
    -R 显示文件的动态重定位入口，仅仅对于动态目标文件有意义，比如某些共享库。

- --full-contents
    -s 显示指定section的完整内容。

    objdump --section=.text -s inet.o | more

- --source
    -S 尽可能反汇编出源代码，尤其当编译的时候指定了-g这种调试参数时，效果比较明显。隐含了-d参数。

- --show-raw-insn
    反汇编的时候，显示每条汇编指令对应的机器码，除非指定了

- --prefix-addresses，这将是缺省选项。

- --no-show-raw-insn
    反汇编时，不显示汇编指令的机器码，这是指定 --prefix-addresses选项时的缺省设置。

- --stabs
    Display the contents of the .stab, .stab.index, and
    .stab.excl sections from an ELF file.  This is only
    useful  on  systems  (such as Solaris 2.0) in which
    .stab debugging symbol-table entries are carried in
    an ELF section.  In most other file formats, debug-
    ging  symbol-table  entries  are interleaved  with
    linkage symbols, and are visible in the --syms output.

- --start-address=address
    从指定地址开始显示数据，该选项影响-d、-r和-s选项的输出。

- --stop-address=address
    显示数据直到指定地址为止，该选项影响-d、-r和-s选项的输出。

- --syms
    -t 显示文件的符号表入口。类似于nm提供的信息

- --dynamic-syms
    -T 显示文件的动态符号表入口，仅仅对动态目标文件有意义，比如某些共享库。它显示的信息类似于 nm -D|--dynamic 显示的信息。

- --version 版本信息

    objdump --version

- --all-headers
    -x 显示所有可用的头信息，包括符号表、重定位入口。-x 等价于
    -a -f -h -r -t 同时指定。

    objdump -x inet.o


示例
--------------------

查看本机目标结构（使用大端还是小端存储）::

    $objdump -i


反汇编程序::

    $objdump -d mian.o

显示符号表入口::

    $objdump  -t main.o

希望显示可用的简洁帮助信息，直接输入objdump即可；（objdump -H)
