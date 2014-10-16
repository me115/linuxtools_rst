.. _01_program_build:

程序构建
===========

.. contents:: 目录

一般源代码提供的程序安装需要通过配置、编译、安装三个步骤；

1. 配置做的工作主要是检查当前环境是否满足要安装软件的依赖关系，以及设置程序安装所需要的初始化信息，比如安装路径，需要安装哪些组件；配置完成，会生成makefile文件供第二步make使用；
#. 编译是对源文件进行编译链接生成可执行程序；
#. 安装做的工作就简单多了，就是将生成的可执行文件拷贝到配置时设置的初始路径下；

配置
--------------------
查询可用的配置选项::

    ./configure --help

配置路径::
    
    ./configure --prefix=/usr/local/snmp
--prefix是配置使用的最常用选项，设置程序安装的路径；

编译
---------------------
编译使用make编译::

    make -f myMakefile
通过-f选项显示指定需要编译的makefile；如果待使用makefile文件在当前路径，且文件名为以下几个，则不用显示指定：

makefile Makefile


makefile编写的要点
^^^^^^^^^^^^^^^^^^^^
- 必须满足第一条规则，满足后停止
- 除第一条规则，其他无顺序

makefile中的全局自变量
^^^^^^^^^^^^^^^^^^^^^^
- $@目标文件名
- @^所有前提名，除副本
- @＋所有前提名，含副本
- @＜一个前提名
- @？所有新于目标文件的前提名
- @*目标文件的基名称
   

.. note::

    系统学习makefile的书写规则，请参考 跟我一起学makefile [#]_

更多选择 CMake
^^^^^^^^^^^^
CMake是一个跨平台的安装（编译）工具，可以用简单的语句来描述所有平台的安装(编译过程)。他能够输出各种各样的makefile或者project文件。使用CMake，能够使程序员从复杂的编译连接过程中解脱出来。它使用一个名为 CMakeLists.txt 的文件来描述构建过程,可以生成标准的构建文件,如 Unix/Linux 的 Makefile 或Windows Visual C++ 的 projects/workspaces 。

编译依赖的库
^^^^^^^^^^^^^^^^^^^^
makefile编译过程中所依赖的非标准库和头文件路径需要显示指明::

    CPPFLAGS -I标记非标准头文件存放路径
    LDFLAGS  -L标记非标准库存放路径

如果CPPFLAGS和LDFLAGS已在用户环境变量中设置并且导出（使用export关键字），就不用再显示指定；

::

    make -f myMakefile LDFLAGS='-L/var/xxx/lib -L/opt/mysql/lib' 
        CPPFLAGS='-I/usr/local/libcom/include -I/usr/local/libpng/include'

.. caution::

    链接多库时，多个库之间如果有依赖，需要注意书写的顺序，右边是左边的前提；

g++编译
^^^^^^^^^^^^^^^^^^^^
::

    g++ -o unixApp unixApp.o a.o b.o
选项说明：

- -o:指明生成的目标文件
- -g：添加调试信息
- -E: 查看中间文件

应用：查询宏展开的中间文件：

在g++的编译选项中，添加 -E选项，然后去掉-o选项 ，重定向到一个文件中即可::

    g++ -g -E unixApp.cpp  -I/opt/app/source > midfile


查询应用程序需要链接的库::

    $ldd myprogrammer
	libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00000039a7e00000)
	libm.so.6 => /lib64/libm.so.6 (0x0000003996400000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00000039a5600000)
	libc.so.6 => /lib64/libc.so.6 (0x0000003995800000)
	/lib64/ld-linux-x86-64.so.2 (0x0000003995400000)

.. note::
    
    关于ldd的使用细节，参见 :ref:`ldd` 

安装
--------------------
安装做的工作就简单多了，就是将生成的可执行文件拷贝到配置时设置的初始路径下::

    $make install
其实 **install** 就是makefile中的一个规则，打开makefile文件后可以查看程序安装的所做的工作；

总结
----------------------------------------------------
configure make install g++


.. [#]  陈皓 跟我一起写Makefile http://scc.qibebt.cas.cn/docs/linux/base/%B8%FA%CE%D2%D2%BB%C6%F0%D0%B4Makefile-%B3%C2%F0%A9.pdf
