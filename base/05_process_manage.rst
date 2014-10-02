.. _05_process_manage:

进程管理工具
=============

.. contents:: 目录


这一节我们介绍进程管理工具；

使用进程管理工具，我们可以查询程序当前的运行状态，或终止一个进程；

任何进程都与文件关联；我们会用到lsof工具（list opened files），作用是列举系统中已经被打开的文件。在linux环境中，任何事物都是文件，设备是文件，目录是文件，甚至sockets也是文件。用好lsof命令，对日常的linux管理非常有帮助。

查询进程
----------------

查询正在运行的进程信息
::

	$ps -ef

eg:查询归属于用户colin115的进程
::

	$ps -ef | grep colin115
	$ps -lu colin115


查询进程ID（适合只记得部分进程字段）
::

	$pgrep 查找进程
	
	eg:查询进程名中含有re的进程
	[/home/weber#]pgrep -l re
	2 kthreadd
	28 ecryptfs-kthrea
	29515 redis-server


以完整的格式显示所有的进程
::

	$ps -ajx


显示进程信息，并实时更新
::

	$top


查看端口占用的进程状态：
::

	lsof -i:3306


查看用户username的进程所打开的文件
::

	$lsof -u username


查询init进程当前打开的文件
::

	$lsof -c init


查询指定的进程ID(23295)打开的文件：
::

	$lsof -p 23295


查询指定目录下被进程开启的文件（使用+D 递归目录）：
::

	$lsof +d mydir1/


终止进程
----------------

杀死指定PID的进程 (PID为Process ID)
::

	$kill PID


杀死相关进程
::

	kill -9 3434


杀死job工作 (job为job number)
::

	$kill %job


进程监控
----------------
查看系统中使用CPU、使用内存最多的进程；
::

	$top
	(->)P

输入top命令后，进入到交互界面；接着输入字符命令后显示相应的进程状态：

对于进程，平时我们最常想知道的就是哪些进程占用CPU最多，占用内存最多。以下两个命令就可以满足要求::

    P：根据CPU使用百分比大小进行排序。
    M：根据驻留内存大小进行排序。
    i：使top不显示任何闲置或者僵死进程。

这里介绍最使用的几个选项,对于更详细的使用，详见 :ref:`top` ;


分析线程栈
-------------------
使用命令pmap，来输出进程内存的状况，可以用来分析线程堆栈；
::

	$pmap PID
	
	eg:
	[/home/weber#]ps -fe| grep redis
	weber    13508 13070  0 08:14 pts/0    00:00:00 grep --color=auto redis
	weber    29515     1  0  2013 ?        02:55:59 ./redis-server redis.conf
	[/home/weber#]pmap 29515
	29515:   ./redis-server redis.conf
	08048000    768K r-x--  /home/weber/soft/redis-2.6.16/src/redis-server
	08108000      4K r----  /home/weber/soft/redis-2.6.16/src/redis-server
	08109000     12K rw---  /home/weber/soft/redis-2.6.16/src/redis-server


综合运用
----------------
将用户colin115下的所有进程名以av_开头的进程终止::

	ps -u colin115 |  awk '/av_/ {print "kill -9 " $1}' | sh

将用户colin115下所有进程名中包含HOST的进程终止::

    ps -fe| grep colin115|grep HOST |awk '{print $2}' | xargs kill -9;


总结
----------
ps top lsof kill pmap
