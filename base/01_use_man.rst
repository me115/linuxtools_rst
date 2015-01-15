.. _01_use_man:

学会使用命令帮助  
================

概述  
--------------------
在linux终端，面对命令不知道怎么用，或不记得命令的拼写及参数时，我们需要求助于系统的帮助文档；
linux系统内置的帮助文档很详细，通常能解决我们的问题，我们需要掌握如何正确的去使用它们；

- 在只记得部分命令关键字的场合，我们可通过man -k来搜索；
- 需要知道某个命令的简要说明，可以使用whatis；而更详细的介绍，则可用info命令；
- 查看命令在哪个位置，我们需要使用which；
- 而对于命令的具体参数及使用方法，我们需要用到强大的man；

下面介绍这些命令；


命令使用
--------------------

查看命令的简要说明
^^^^^^^^^^^^^^^^^^^^  
简要说明命令的作用（显示命令所处的man分类页面）::

    $whatis command

正则匹配::

    $whatis -w "loca*"

更加详细的说明文档::

    $info command  

使用man
^^^^^^^^^^^^^^^^^^^^

查询命令command的说明文档::

    $man command
    eg：man date

使用page up和page down来上下翻页

在man的帮助手册中，将帮助文档分为了9个类别，对于有的关键字可能存在多个类别中，
我们就需要指定特定的类别来查看；（一般我们查询bash命令，归类在1类中）；

man页面所属的分类标识(常用的是分类1和分类3) ::

    (1)、用户可以操作的命令或者是可执行文件 
    (2)、系统核心可调用的函数与工具等
    (3)、一些常用的函数与数据库 
    (4)、设备文件的说明 
    (5)、设置文件或者某些文件的格式 
    (6)、游戏  
    (7)、惯例与协议等。例如Linux标准文件系统、网络协议、ASCⅡ，码等说明内容  
    (8)、系统管理员可用的管理条令  
    (9)、与内核有关的文件 


前面说到使用whatis会显示命令所在的具体的文档类别，我们学习如何使用它 ::

    eg:
    $whatis printf  
    printf               (1)  - format and print data  
    printf               (1p)  - write formatted output  
    printf               (3)  - formatted output conversion  
    printf               (3p)  - print formatted output  
    printf [builtins]    (1)  - bash built-in commands, see bash(1)  
我们看到printf在分类1和分类3中都有；分类1中的页面是命令操作及可执行文件的帮助；而3是常用函数库说明；如果我们想看的是C语言中printf的用法，可以指定查看分类3的帮助：  
::

    $man 3 printf

    $man -k keyword

查询关键字
根据命令中部分关键字来查询命令，适用于只记住部分命令的场合；  

eg：查找GNOME的config配置工具命令::

    $man -k GNOME config| grep 1  

对于某个单词搜索，可直接使用/word来使用:   /-a;
多关注下SEE ALSO 可看到更多精彩内容  


查看路径
^^^^^^^^
查看程序的binary文件所在路径::
    
    $which command  
    
eg:查找make程序安装路径::

    $which make
    /opt/app/openav/soft/bin/make install

查看程序的搜索路径::

    $whereis command
当系统中安装了同一软件的多个版本时，不确定使用的是哪个版本时，这个命令就能派上用场；


总结  
^^^^
whatis info man which whereis

