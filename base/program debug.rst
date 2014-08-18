gdb

file 查看文件
跨越权限
setgid
setuid
动态链接库
ldd
nm
对比objdump readelf 460
size hello查看内存占用
编译动态链接库的命令和静态链接库的对比
库的命名规则 lib前缀

pmap 显示进程虚拟内存 进程使用空间
strace 分析程序进行系统调用行为
显示用户模式到内核模式的过渡
调试信号量
跟踪进程系统调用使用率
strace -p $pid 看看进程都在干啥.
valgrind 调试内存

进程调试命令:truss、strace和ltrace
http://hi.baidu.com/yndaijian/item/7277d0162f9c8724f6625ccc
进程无法启动，软件运行速度突然变慢，程序的"SegmentFault"等等都是让每个Unix系统用户头痛的问题，而这些问题都可以通过使用truss、strace和ltrace这三个常用的调试工具来快速诊断软件的"疑难杂症"。

file
作用：用于查看文件的类型；
比如我们在64位机器上发现了一个32位的库，链接不上，这就有问题了：
::

	/opt/app/todeav1/test$file a.out
	a.out: ELF 64-bit LSB executable, AMD x86-64, version 1 (SYSV), for GNU/Linux 2.6.9, dynamically linked (uses shared libs), for GNU/Linux 2.6.9, not stripped


调试
lsof 查看系统所有打开文件
fuser
strings 查看数据中的文本信息
xxd 十六进制显示数据 只显示文本
注意大端和小端
一般网络字节顺序 大端方式
本地 小端方式
hexdump 十六进制输出
od
调试IPC
删除dead对象
ipcs -m
lsof |head -l ；lsof|grep 55276
获取对象更多信息  ipcs -m -i 32376
调试套接字
netstat
netstat --tcp -n活动网络连接
lsof
lsof -n -i tcp
查看Core文件由哪个程序生成：
file core
$od -c filename

ltrace 跟踪进程调用
只能跟踪动态链接库
不能跟踪静态链接库

通过strace 或 oprofile命令；

以ASCII字符显示文件

GDB中应该知道的几个调试方法
http://coolshell.cn/articles/3643.html

lsof学习
http://blog.csdn.net/hproc/article/details/7446221


