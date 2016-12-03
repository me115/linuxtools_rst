.. _lsof:

lsof 一切皆文件
================

lsof（list open files）是一个查看当前系统文件的工具。在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。如传输控制协议 (TCP) 和用户数据报协议 (UDP) 套接字等，系统在后台都为该应用程序分配了一个文件描述符，该文件描述符提供了大量关于这个应用程序本身的信息。

lsof打开的文件可以是：

1. 普通文件
2. 目录
3. 网络文件系统的文件
4. 字符或设备文件
5. (函数)共享库
6. 管道，命名管道
7. 符号链接
8. 网络文件（例如：NFS file、网络socket，unix域名socket）
9. 还有其它类型的文件，等等

命令参数
-----------------
- -a 列出打开文件存在的进程
- -c<进程名> 列出指定进程所打开的文件
- -g 列出GID号进程详情
- -d<文件号> 列出占用该文件号的进程
- +d<目录> 列出目录下被打开的文件
- +D<目录> 递归列出目录下被打开的文件
- -n<目录> 列出使用NFS的文件
- -i<条件> 列出符合条件的进程。（4、6、协议、:端口、 @ip ）
- -p<进程号> 列出指定进程号所打开的文件
- -u 列出UID号进程详情
- -h 显示帮助信息
- -v 显示版本信息

使用实例
-------------------

实例1：无任何参数
^^^^^^^^^^^^^^^^^^^^^
::

	$lsof| more
	COMMAND     PID      USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME
	init          1      root  cwd       DIR              253,0     4096          2 /
	init          1      root  rtd       DIR              253,0     4096          2 /
	init          1      root  txt       REG              253,0   150352    1310795 /sbin/init
	init          1      root  mem       REG              253,0    65928    5505054 /lib64/libnss_files-2.12.so
	init          1      root  mem       REG              253,0  1918016    5521405 /lib64/libc-2.12.so
	init          1      root  mem       REG              253,0    93224    5521440 /lib64/libgcc_s-4.4.6-20120305.so.1
	init          1      root  mem       REG              253,0    47064    5521407 /lib64/librt-2.12.so
	init          1      root  mem       REG              253,0   145720    5521406 /lib64/libpthread-2.12.so
	...

说明：

lsof输出各列信息的意义如下：

- COMMAND：进程的名称
- PID：进程标识符
- PPID：父进程标识符（需要指定-R参数）
- USER：进程所有者
- PGID：进程所属组
- FD：文件描述符，应用程序通过文件描述符识别该文件。如cwd、txt等::

    （1）cwd：表示current work dirctory，即：应用程序的当前工作目录，这是该应用程序启动的目录，除非它本身对这个目录进行更改
    （2）txt ：该类型的文件是程序代码，如应用程序二进制文件本身或共享库，如上列表中显示的 /sbin/init 程序
    （3）lnn：library references (AIX);
    （4）er：FD information error (see NAME column);
    （5）jld：jail directory (FreeBSD);
    （6）ltx：shared library text (code and data);
    （7）mxx ：hex memory-mapped type number xx.
    （8）m86：DOS Merge mapped file;
    （9）mem：memory-mapped file;
    （10）mmap：memory-mapped device;
    （11）pd：parent directory;
    （12）rtd：root directory;
    （13）tr：kernel trace file (OpenBSD);
    （14）v86  VP/ix mapped file;
    （15）0：表示标准输入
    （16）1：表示标准输出
    （17）2：表示标准错误
    一般在标准输出、标准错误、标准输入后还跟着文件状态模式：r、w、u等
    （1）u：表示该文件被打开并处于读取/写入模式
    （2）r：表示该文件被打开并处于只读模式
    （3）w：表示该文件被打开并处于
    （4）空格：表示该文件的状态模式为unknow，且没有锁定
    （5）-：表示该文件的状态模式为unknow，且被锁定
    同时在文件状态模式后面，还跟着相关的锁
    （1）N：for a Solaris NFS lock of unknown type;
    （2）r：for read lock on part of the file;
    （3）R：for a read lock on the entire file;
    （4）w：for a write lock on part of the file;（文件的部分写锁）
    （5）W：for a write lock on the entire file;（整个文件的写锁）
    （6）u：for a read and write lock of any length;
    （7）U：for a lock of unknown type;
    （8）x：for an SCO OpenServer Xenix lock on part      of the file;
    （9）X：for an SCO OpenServer Xenix lock on the      entire file;
    （10）space：if there is no lock.

- TYPE：文件类型，如DIR、REG等，常见的文件类型::

    （1）DIR：表示目录
    （2）CHR：表示字符类型
    （3）BLK：块设备类型
    （4）UNIX： UNIX 域套接字
    （5）FIFO：先进先出 (FIFO) 队列
    （6）IPv4：网际协议 (IP) 套接字
- DEVICE：指定磁盘的名称
- SIZE：文件的大小
- NODE：索引节点（文件在磁盘上的标识）
- NAME：打开文件的确切名称

实例2：查找某个文件相关的进程
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

	$lsof /bin/bash
	COMMAND     PID USER  FD   TYPE DEVICE SIZE/OFF    NODE NAME
	mysqld_sa  2169 root txt    REG  253,0   938736 4587562 /bin/bash
	ksmtuned   2334 root txt    REG  253,0   938736 4587562 /bin/bash
	bash      20121 root txt    REG  253,0   938736 4587562 /bin/bash


实例3：列出某个用户打开的文件信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -u username

 -u 选项，u是user的缩写

实例4：列出某个程序进程所打开的文件信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -c mysql

-c 选项将会列出所有以mysql这个进程开头的程序的文件，其实你也可以写成 lsof | grep mysql, 但是第一种方法明显比第二种方法要少打几个字符；

实例5：列出某个用户以及某个进程所打开的文件信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof  -u test -c mysql

实例6：通过某个进程号显示该进程打开的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -p 11968

实例7：列出所有的网络连接
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -i

实例8：列出所有tcp 网络连接信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -i tcp

    $lsof -n -i tcp
    COMMAND     PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
    svnserve  11552 weber    3u  IPv4 3799399      0t0  TCP *:svn (LISTEN)
    redis-ser 25501 weber    4u  IPv4  113150      0t0  TCP 127.0.0.1:6379 (LISTEN)

实例9：列出谁在使用某个端口
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -i :3306

实例10：列出某个用户的所有活跃的网络端口
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -a -u test -i

实例11：根据文件描述列出对应的文件信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -d description(like 2)

示例::

    $lsof -d 3 | grep PARSER1
    tail      6499 tde    3r   REG    253,3   4514722     417798 /opt/applog/open/log/HOSTPARSER1_ERROR_141217.log.001


说明：
0表示标准输入，1表示标准输出，2表示标准错误，从而可知：所以大多数应用程序所打开的文件的 FD 都是从 3 开始


实例12：列出被进程号为1234的进程所打开的所有IPV4 network files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $lsof -i 4 -a -p 1234

实例13：列出目前连接主机nf5260i5-td上端口为：20，21，80相关的所有文件信息，且每隔3秒重复执行
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    lsof -i @nf5260i5-td:20,21,80 -r 3
