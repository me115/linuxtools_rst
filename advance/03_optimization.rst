.. _03_optimization:

性能优化
=================
性能优化的核心是找出系统的瓶颈点，问题找到了，优化的工作也就完成了大半；
这里介绍的性能优化主要从两个层面来介绍：系统层面和程序层面；

分析系统瓶颈
--------------------
iostat vmstat top
系统响应变慢，我们有很多工具来排查具体的问题出在哪里；
首先查询当前进程的使用使用正常：

::

    $top
	top - 09:14:56 up 264 days, 20:56,  1 user,  load average: 0.02, 0.04, 0.00
	Tasks:  87 total,   1 running,  86 sleeping,   0 stopped,   0 zombie
	Cpu(s):  0.0%us,  0.2%sy,  0.0%ni, 99.7%id,  0.0%wa,  0.0%hi,  0.0%si,  0.2%st
	Mem:    377672k total,   322332k used,    55340k free,    32592k buffers
	Swap:   397308k total,    67192k used,   330116k free,    71900k cached
	PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
	1 root      20   0  2856  656  388 S  0.0  0.2   0:49.40 init
	2 root      20   0     0    0    0 S  0.0  0.0   0:00.00 kthreadd
	3 root      20   0     0    0    0 S  0.0  0.0   7:15.20 ksoftirqd/0
	4 root      RT   0     0    0    0 S  0.0  0.0   0:00.00 migration/

top指令可以满足；
进入交互模式后，输入M，进程列表按内存使用大小降序排序，便于我们观察最大内存使用者使用有问题；（检测内存泄漏问题）
输入P，进程列表按CPU使用大小降序排序，便于我们观察最耗CPU资源的使用者是否有问题；
top第三行显示当前系统的，其中有两个值很关键：
%id：空闲CPU时间百分比，如果这个值过低，表明系统CPU存在瓶颈；
%wa：等待I/O的CPU时间百分比，如果这个值过低，表明IO存在瓶颈；

查看内存是否存在瓶颈，使用top指令看比较麻烦，而free命令更为直观：
::

    [/home/weber#]free
                 total       used       free     shared    buffers     cached
    Mem:        501820     452028      49792      37064       5056     136732
    -/+ buffers/cache:     310240     191580
    Swap:            0          0          0
    [/home/weber#]top
    top - 17:52:17 up 42 days,  7:10,  1 user,  load average: 0.02, 0.02, 0.05
    Tasks:  80 total,   1 running,  79 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    KiB Mem:    501820 total,   452548 used,    49272 free,     5144 buffers
    KiB Swap:        0 total,        0 used,        0 free.   136988 cached Mem

top工具显示了free工具的第一行所有信息，但真实可用的内存，还需要自己计算才知道；
系统实际可用的内存为free工具输出第二行的free+buffer+cached；也就是第三行的free值191580；关于free命令各个值的详情解读，请参考这篇文章 :ref:`free` ;

如果内存指过低，系统响应变慢很明显，因为这使得系统不停的做换入换出的工作；



分析进程调用
--------------------
pstrace  pstack

程序分析工具
--------------------

分析系统瓶颈
分析系统IO
分析CPU
找出耗时的程序；

:ref:`sar`  

优化程序代码
------------------
优化自己开发的程序，建议采用以下准则::

1. 二八法则：在任何一组东西中，最重要的只占其中一小部分，约20%，其余80%的尽管是多数，却是次要的；在优化实践中，我们将精力集中在优化那20%最耗时的代码上，整体性能将有显著的提升；这个很好理解。函数A虽然代码量大，但在一次正常执行流程中，只调用了一次。而另一个函数B代码量比A小很多，但被调用了1000次。显然，我们更应关注B的优化。
2. 编完代码，再优化；编码的时候总是考虑最佳性能未必总是好的；在强调最佳性能的编码方式的同时，可能就损失了代码的可读性和开发效率；

gprof使用步骤
^^^^^^^^^^^^^^^^^^^^
1. 用gcc、g++、xlC编译程序时，使用-pg参数，如：g++ -pg -o test.exe test.cpp编译器会自动在目标代码中插入用于性能测试的代码片断，这些代码在程序运行时采集并记录函数的调用关系和调用次数，并记录函数自身执行时间和被调用函数的执行时间。
2. 执行编译后的可执行程序，如：./test.exe。该步骤运行程序的时间会稍慢于正常编译的可执行程序的运行时间。程序运行结束后，会在程序所在路径下生成一个缺省文件名为gmon.out的文件，这个文件就是记录程序运行的性能、调用关系、调用次数等信息的数据文件。
3) 使用gprof命令来分析记录程序运行信息的gmon.out文件，如：gprof test.exe gmon.out则可以在显示器上看到函数调用相关的统计、分析信息。上述信息也可以采用gprof test.exe gmon.out> gprofresult.txt重定向到文本文件以便于后续分析。

关于gprof的使用案例，请参考 [f1]_ ;

其它工具
--------------------
调试内存泄漏的工具valgrind，感兴趣的朋友可以google了解；

OProfile: Linux 平台上的一个功能强大的性能分析工具,使用参考 [f2]_ ;


.. [f1] C++的性能优化实践 http://www.cnblogs.com/me115/archive/2013/06/05/3117967.html
.. [f2] 用 OProfile 彻底了解性能 http://www.ibm.com/developerworks/cn/linux/l-oprof/
.. [f3] Linux上的free命令详解 http://www.cnblogs.com/coldplayerest/archive/2010/02/20/1669949.html
strace 、lstrace:跟踪进程调用
valgrind：调试内存
pmap： 显示进程、虚拟内存，进程使用空间
pmap可以报告某个或多个进程的内存使用情况。使用pmap判断主机中哪个进程因占用过多内存导致内存瓶颈。
strace截取和记录系统进程调用，以及进程收到的信号。是一个非常有效的检测、指导和调试工具。系统管理员可以通过该命令容易地解决程序问题。

pmap 显示进程虚拟内存 
^^^^^^^^^^^^^^^^^^^^^^
进程使用空间


top 好学习
sh+g 选择屏幕
f 交互式改变显示域 w保存设置
free
vmstat
看懂每一列 书上有
扩展
iostat
mpstat
sar -r 1 4 提供虚拟内存信息
sar 最常用与监控系统性能 书上
Oprofile 系统最新加入
分析时间消耗
