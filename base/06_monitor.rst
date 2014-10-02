.. _06_monitor:

性能监控
=========

.. contents:: 目录


在使用操作系统的过程中，我们经常需要查看当前的性能如何，需要了解CPU、内存和硬盘的使用情况；
本节介绍的这几个工具能满足日常工作要求；

监控CPU
-------------
查看CPU使用率
::

	$sar -u
	
	eg:
	$sar -u 1 2
	[/home/weber#]sar -u 1 2
	Linux 2.6.35-22-generic-pae (MyVPS) 	06/28/2014 	_i686_	(1 CPU)
	
	09:03:59 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
	09:04:00 AM     all      0.00      0.00      0.50      0.00      0.00     99.50
	09:04:01 AM     all      0.00      0.00      0.00      0.00      0.00    100.00

后面的两个参数表示监控的频率，比如例子中的1和2，表示每秒采样一次，总共采样2次；

查看CPU平均负载
::

	$sar -q 1 2

sar指定-q后，就能查看运行队列中的进程数、系统上的进程大小、平均负载等；


查询内存
----------------
查看内存使用状况
sar指定-r之后，可查看内存使用状况;
::

	$sar -r 1 2
	09:08:48 AM kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit  kbactive   kbinact
	09:08:49 AM     17888    359784     95.26     37796     73272    507004     65.42    137400    150764
	09:08:50 AM     17888    359784     95.26     37796     73272    507004     65.42    137400    150764
	Average:        17888    359784     95.26     37796     73272    507004     65.42    137400    150764


查看内存使用量
::

	$free -m


查询页面交换
----------------------
查看页面交换发生状况
页面发生交换时，服务器的吞吐量会大幅下降；服务器状况不良时，如果怀疑因为内存不足而导致了页面交换的发生，可以使用sar -W这个命令来确认是否发生了大量的交换；
::

	$sar -W 1 3


查询硬盘使用
----------------------
查看磁盘空间利用情况
::

	$df -h

查询当前目录下空间使用情况
::

	du -sh  -h是人性化显示 s是递归整个目录的大小


查看该目录下所有文件夹的排序后的大小
::

	for i in `ls`; do du -sh $i; done | sort
	或者
	du -sh `ls`



综合应用
----------------
当系统中sar不可用时，可以使用以下工具替代：linux下有 vmstat、Unix系统有prstat

eg：
查看cpu、内存、使用情况：
vmstat n m （n 为监控频率、m为监控次数）
::

	[/home/weber#]vmstat 1 3
	procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu----
	r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa
	0  0  86560  42300   9752  63556    0    1     1     1    0    0  0  0 99  0
	1  0  86560  39936   9764  63544    0    0     0    52   66   95  5  0 95  0
	0  0  86560  42168   9772  63556    0    0     0    20  127  231 13  2 84  0



使用watch 工具监控变化
当需要持续的监控应用的某个数据变化时，watch工具能满足要求；
执行watch命令后，会进入到一个界面，输出当前被监控的数据，一旦数据变化，便会高亮显示变化情况；


eg：操作redis时，监控内存变化：
::

	$watch -d -n 1 './redis-cli info | grep memory'
	(以下为watch工具中的界面内容，一旦内存变化，即实时高亮显示变化）
	Every 1.0s: ./redis-cli info | grep memory                                                                  Mon Apr 28 16:10:36 2014
	
	used_memory:45157376
	used_memory_human:43.07M
	used_memory_rss:47628288
	used_memory_peak:49686080
	used_memory_peak_human:47.38M


总结
----------
top / sar / free / watch

附录
----------
关于sar的使用详解参考：:ref:`sar`
