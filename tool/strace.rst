.. _strace:

strace 跟踪进程中的系统调用
===========================
strace常用来跟踪进程执行时的系统调用和所接收的信号。 在Linux世界，进程不能直接访问硬件设备，当进程需要访问硬件设备(比如读取磁盘文件，接收网络数据等等)时，必须由用户态模式切换至内核态模式，通过系统调用访问硬件设备。strace可以跟踪到一个进程产生的系统调用,包括参数，返回值，执行消耗的时间。

输出参数含义
--------------------
每一行都是一条系统调用，等号左边是系统调用的函数名及其参数，右边是该调用的返回值。
strace 显示这些调用的参数并返回符号形式的值。strace 从内核接收信息，而且不需要以任何特殊的方式来构建内核。

::

    $strace cat /dev/null 
    execve("/bin/cat", ["cat", "/dev/null"], [/* 22 vars */]) = 0
    brk(0)                                  = 0xab1000
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f29379a7000
    access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
    ...
    

参数
---------------------
::

    -c 统计每一系统调用的所执行的时间,次数和出错的次数等. 
    -d 输出strace关于标准错误的调试信息. 
    -f 跟踪由fork调用所产生的子进程. 
    -ff 如果提供-o filename,则所有进程的跟踪结果输出到相应的filename.pid中,pid是各进程的进程号. 
    -F 尝试跟踪vfork调用.在-f时,vfork不被跟踪. 
    -h 输出简要的帮助信息. 
    -i 输出系统调用的入口指针. 
    -q 禁止输出关于脱离的消息. 
    -r 打印出相对时间关于,,每一个系统调用. 
    -t 在输出中的每一行前加上时间信息. 
    -tt 在输出中的每一行前加上时间信息,微秒级. 
    -ttt 微秒级输出,以秒了表示时间. 
    -T 显示每一调用所耗的时间. 
    -v 输出所有的系统调用.一些调用关于环境变量,状态,输入输出等调用由于使用频繁,默认不输出. 
    -V 输出strace的版本信息. 
    -x 以十六进制形式输出非标准字符串 
    -xx 所有字符串以十六进制形式输出. 
    -a column 
    设置返回值的输出位置.默认 为40. 
    -e expr 
    指定一个表达式,用来控制如何跟踪.格式如下: 
    [qualifier=][!]value1[,value2]... 
    qualifier只能是 trace,abbrev,verbose,raw,signal,read,write其中之一.value是用来限定的符号或数字.默认的 qualifier是 trace.感叹号是否定符号.例如: 
    -eopen等价于 -e trace=open,表示只跟踪open调用.而-etrace!=open表示跟踪除了open以外的其他调用.有两个特殊的符号 all 和 none. 
    注意有些shell使用!来执行历史记录里的命令,所以要使用\\. 
    -e trace=set 
    只跟踪指定的系统 调用.例如:-e trace=open,close,rean,write表示只跟踪这四个系统调用.默认的为set=all. 
    -e trace=file 
    只跟踪有关文件操作的系统调用. 
    -e trace=process 
    只跟踪有关进程控制的系统调用. 
    -e trace=network 
    跟踪与网络有关的所有系统调用. 
    -e strace=signal 
    跟踪所有与系统信号有关的 系统调用 
    -e trace=ipc 
    跟踪所有与进程通讯有关的系统调用 
    -e abbrev=set 
    设定 strace输出的系统调用的结果集.-v 等与 abbrev=none.默认为abbrev=all. 
    -e raw=set 
    将指 定的系统调用的参数以十六进制显示. 
    -e signal=set 
    指定跟踪的系统信号.默认为all.如 signal=!SIGIO(或者signal=!io),表示不跟踪SIGIO信号. 
    -e read=set 
    输出从指定文件中读出 的数据.例如: 
    -e read=3,5 
    -e write=set 
    输出写入到指定文件中的数据. 
    -o filename 
    将strace的输出写入文件filename 
    -p pid 
    跟踪指定的进程pid. 
    -s strsize 
    指定输出的字符串的最大长度.默认为32.文件名一直全部输出. 
    -u username 
    以username 的UID和GID执行被跟踪的命令

命令实例
--------------------
跟踪可执行程序
^^^^^^^^^^^^^^^^^^^^
::

    strace -f -F -o ~/straceout.txt myserver
-f -F选项告诉strace同时跟踪fork和vfork出来的进程，-o选项把所有strace输出写到~/straceout.txt里 面，myserver是要启动和调试的程序。

跟踪服务程序
^^^^^^^^^^^^^^^^^^^^
::

    strace -o output.txt -T -tt -e trace=all -p 28979
跟踪28979进程的所有系统调用（-e trace=all），并统计系统调用的花费时间，以及开始时间（并以可视化的时分秒格式显示），最后将记录结果存在output.txt文件里面。
