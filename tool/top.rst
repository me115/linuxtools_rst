.. _top:

top linux下的任务管理器
=========================

top命令是Linux下常用的性能分析工具，能够实时显示系统中各个进程的资源占用状况，类似于Windows的任务管理器。top是一个动态显示过程,即可以通过用户按键来不断刷新当前状态.如果在前台执行该命令,它将独占前台,直到用户终止该程序为止.比较准确的说,top命令提供了实时的对系统处理器的状态监视.它将显示系统中CPU最“敏感”的任务列表.该命令可以按CPU使用.内存使用和执行时间对任务进行排序；而且该命令的很多特性都可以通过交互式命令或者在个人定制文件中进行设定。

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
	4 root      RT   0     0    0    0 S  0.0  0.0   0:00.00 migration/0


- 第一行
    * 09:14:56 ：     系统当前时间
    * 264 days, 20:56 ：   系统开机到现在经过了多少时间
    * 1 users  ：            当前2用户在线
    * load average: 0.02, 0.04, 0.00：        系统1分钟、5分钟、15分钟的CPU负载信息

- 第二行
    * Tasks：任务;
    * 87 total：很好理解，就是当前有87个任务，也就是87个进程。
    * 1 running：1个进程正在运行
    * 86 sleeping：86个进程睡眠
    * 0 stopped：停止的进程数
    * 0 zombie：僵死的进程数

- 第三行
    * Cpu(s)：表示这一行显示CPU总体信息
    * 0.0%us：用户态进程占用CPU时间百分比，不包含renice值为负的任务占用的CPU的时间。
    * 0.7%sy：内核占用CPU时间百分比
    * 0.0%ni：改变过优先级的进程占用CPU的百分比
    * 99.3%id：空闲CPU时间百分比
    * 0.0%wa：等待I/O的CPU时间百分比
    * 0.0%hi：CPU硬中断时间百分比
    * 0.0%si：CPU软中断时间百分比
    * 注：这里显示数据是所有cpu的平均值，如果想看每一个cpu的处理情况，按1即可；折叠，再次按1；

- 第四行
    * Men：内存的意思
    * 8175320kk total：物理内存总量
    * 8058868k used：使用的物理内存量
    * 116452k free：空闲的物理内存量
    * 283084k buffers：用作内核缓存的物理内存量

- 第五行
    * Swap：交换空间
    * 6881272k total：交换区总量
    * 4010444k used：使用的交换区量
    * 2870828k free：空闲的交换区量
    * 4336992k cached：缓冲交换区总量

- 进程信息
    * 再下面就是进程信息：
    * PID：进程的ID
    * USER：进程所有者
    * PR：进程的优先级别，越小越优先被执行
    * NInice：值
    * VIRT：进程占用的虚拟内存
    * RES：进程占用的物理内存
    * SHR：进程使用的共享内存
    * S：进程的状态。S表示休眠，R表示正在运行，Z表示僵死状态，N表示该进程优先值为负数
    * %CPU：进程占用CPU的使用率
    * %MEM：进程使用的物理内存和总内存的百分比
    * TIME+：该进程启动后占用的总的CPU时间，即占用CPU使用时间的累加值。
    * COMMAND：进程启动命令名称

top命令交互操作指令
-------------------------------
下面列出一些常用的 top命令操作指令

	* q：退出top命令
	* <Space>：立即刷新
	* s：设置刷新时间间隔
	* c：显示命令完全模式
	* t:：显示或隐藏进程和CPU状态信息
	* m：显示或隐藏内存状态信息
	* l：显示或隐藏uptime信息
	* f：增加或减少进程显示标志
	* S：累计模式，会把已完成或退出的子进程占用的CPU时间累计到父进程的MITE+
	* P：按%CPU使用率排行
	* T：按MITE+排行
	* M：按%MEM排行
	* u：指定显示用户进程
	* r：修改进程renice值
	* kkill：进程
	* i：只显示正在运行的进程
	* W：保存对top的设置到文件^/.toprc，下次启动将自动调用toprc文件的设置。
	* h：帮助命令。
	* q：退出

注：强调一下，使用频率最高的是P、T、M，因为通常使用top，我们就想看看是哪些进程最耗cpu资源、占用的内存最多；
注：通过”shift + >”或”shift + <”可以向右或左改变排序列
如果只需要查看内存：可用free命令。只查看uptime信息（第一行），可用uptime命令；


实例
----------
实例1：多核CPU监控
^^^^^^^^^^^^^^^^^^^^^^^
在top基本视图中，按键盘数字“1”，可监控每个逻辑CPU的状况；
::

	[rdtfr@bl685cb4-t ^]$ top
	top - 09:10:44 up 20 days, 16:51,  4 users,  load average: 3.82, 4.40, 4.40
	Tasks: 1201 total,  10 running, 1189 sleeping,   0 stopped,   2 zombie
	Cpu0  :  1.3%us,  2.3%sy,  0.0%ni, 96.4%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
	Cpu1  :  1.3%us,  2.6%sy,  0.0%ni, 96.1%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
	Cpu2  :  1.0%us,  2.0%sy,  0.0%ni, 92.5%id,  0.0%wa,  0.0%hi,  4.6%si,  0.0%st
	Cpu3  :  3.9%us,  7.8%sy,  0.0%ni, 83.2%id,  0.0%wa,  0.0%hi,  5.2%si,  0.0%st
	Cpu4  :  4.2%us, 10.4%sy,  0.0%ni, 63.8%id,  0.0%wa,  0.0%hi, 21.5%si,  0.0%st
	Cpu5  :  6.8%us, 12.7%sy,  0.0%ni, 80.5%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
	Cpu6  :  2.9%us,  7.2%sy,  0.0%ni, 85.3%id,  0.0%wa,  0.0%hi,  4.6%si,  0.0%st
	Cpu7  :  6.2%us, 13.0%sy,  0.0%ni, 75.3%id,  0.0%wa,  0.0%hi,  5.5%si,  0.0%st
	Mem:  32943888k total, 32834216k used,   109672k free,   642704k buffers
	Swap: 35651576k total,  5761928k used, 29889648k free, 16611500k cached


实例2：高亮显示当前运行进程
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

	在top基本视图中,按键盘“b”（打开/关闭加亮效果）；


实例3：显示完整的程序命令
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
命令：top -c
::

	[rdtfr@bl685cb4-t ^]$ top -c
	top - 09:14:35 up 20 days, 16:55,  4 users,  load average: 5.77, 5.01, 4.64
	Tasks: 1200 total,   5 running, 1192 sleeping,   0 stopped,   3 zombie
	Cpu(s):  4.4%us,  6.0%sy,  0.0%ni, 83.8%id,  0.2%wa,  0.0%hi,  5.5%si,  0.0%st
	Mem:  32943888k total, 32842896k used,   100992k free,   591484k buffers
	Swap: 35651576k total,  5761808k used, 29889768k free, 16918824k cached
	PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
	2013 apache    18   0  403m  88m 5304 S 25.0  0.3   6:37.44 /usr/sbin/httpd
	18335 pubtest   22   0 65576  996  728 R  7.8  0.0   0:00.24 netstat -naltp
	16499 rdtfare   15   0 13672 2080  824 R  2.6  0.0   0:00.38 top -c
	29684 rdtfare   15   0 1164m 837m  14m S  2.3  2.6 148:47.54 ./autodata data1.txt
	12976 pubtest   18   0  238m 9000 1932 S  1.6  0.0 439:28.44 tscagent -s TOEV_P


实例4：显示指定的进程信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
命令：top -p pidid
::

	/opt/app/tdv1/config#top -p 17265
	top - 09:17:34 up 455 days, 17:55,  2 users,  load average: 3.76, 4.56, 4.46
	Tasks:   1 total,   0 running,   1 sleeping,   0 stopped,   0 zombie
	Cpu(s):  7.8%us,  1.9%sy,  0.0%ni, 89.2%id,  0.0%wa,  0.1%hi,  1.0%si,  0.0%st
	Mem:   8175452k total,  8103988k used,    71464k free,   268716k buffers
	Swap:  6881272k total,  4275424k used,  2605848k free,  6338184k cached
	PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
	17265 tdv1      15   0 56504  828  632 S  0.0  0.0 195:53.25 redis-server


指定进程信息有多个时，需要结合其它工具将回车替换为,（-p 支持pid,pid,pid语法）

命令：top -p `pgrep MULTI_PROCESS | tr "\\n" "," | sed 's/,$//'`

::

    /opt/app/tdv1$top -p `pgrep java | tr "\\n" "," | sed 's/,$//'`
    top - 14:05:31 up 53 days,  2:43,  9 users,  load average: 0.29, 0.34, 0.22
    Tasks:   3 total,   0 running,   3 sleeping,   0 stopped,   0 zombie
    Cpu(s):  5.9%us,  8.2%sy,  0.0%ni, 86.0%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
    Mem:  66082088k total, 29512860k used, 36569228k free,   756352k buffers
    Swap: 32767992k total,  1019900k used, 31748092k free, 15710284k cached

      PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND                                          27855 rdtfare   20   0 4454m 1.3g 5300 S  0.7  2.0 338:31.37 java                         
     2034 jenkins   20   0 18.3g 5.2g 5284 S  0.3  8.2  56:02.38 java                                             12156 rdtfare   20   0 4196m 1.2g  12m S  0.3  2.0  86:34.62 java  

更强大的工具
---------------
htop
^^^^^^^^^^^^^^^^^^^^
htop 是一个 Linux 下的交互式的进程浏览器，可以用来替换Linux下的top命令。

与Linux传统的top相比，htop更加人性化。它可让用户交互式操作，支持颜色主题，可横向或纵向滚动浏览进程列表，并支持鼠标操作。

与top相比，htop有以下优点：

- 可以横向或纵向滚动浏览进程列表，以便看到所有的进程和完整的命令行。
- 在启动上，比top 更快。
- 杀进程时不需要输入进程号。
- htop 支持鼠标操作。
    
