.. _iostat:

iostat 监视I/O子系统
====================

iostat是I/O statistics（输入/输出统计）的缩写，用来动态监视系统的磁盘操作活动。


命令格式
----------------
iostat[参数][时间][次数]

命令功能
----------------
通过iostat方便查看CPU、网卡、tty设备、磁盘、CD-ROM 等等设备的活动情况,	负载信息。

命令参数
----------------
- -C 显示CPU使用情况
- -d 显示磁盘使用情况
- -k 以 KB 为单位显示
- -m 以 M 为单位显示
- -N 显示磁盘阵列(LVM) 信息
- -n 显示NFS 使用情况
- -p[磁盘] 显示磁盘和分区的情况
- -t 显示终端和CPU的信息
- -x 显示详细信息
- -V 显示版本信息


工具实例
----------------
实例1：显示所有设备负载情况
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	/root$iostat
	Linux 2.6.32-279.el6.x86_64 (colin)   07/16/2014      _x86_64_        (4 CPU)
	
	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
	10.81    0.00   14.11    0.18    0.00   74.90
	
	Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
	sda               1.95         1.48        70.88    9145160  437100644
	dm-0              3.08         0.55        24.34    3392770  150087080
	dm-1              5.83         0.93        46.49    5714522  286724168
	dm-2              0.01         0.00         0.05      23930     289288


cpu属性值说明：
    * %user：CPU处在用户模式下的时间百分比。
    * %nice：CPU处在带NICE值的用户模式下的时间百分比。
    * %system：CPU处在系统模式下的时间百分比。
    * %iowait：CPU等待输入输出完成时间的百分比。
    * %steal：管理程序维护另一个虚拟处理器时，虚拟CPU的无意识等待时间百分比。
    * %idle：CPU空闲时间百分比。

注：如果%iowait的值过高，表示硬盘存在I/O瓶颈，%idle值高，表示CPU较空闲，如果%idle值高但系统响应慢时，有可能是CPU等待分配内存，此时应加大内存容量。%idle值如果持续低于10，那么系统的CPU处理能力相对较低，表明系统中最需要解决的资源是CPU。

disk属性值说明：
    * rrqm/s:  每秒进行 merge 的读操作数目。即 rmerge/s
    * wrqm/s:  每秒进行 merge 的写操作数目。即 wmerge/s
    * r/s:  每秒完成的读 I/O 设备次数。即 rio/s
    * w/s:  每秒完成的写 I/O 设备次数。即 wio/s
    * rsec/s:  每秒读扇区数。即 rsect/s
    * wsec/s:  每秒写扇区数。即 wsect/s
    * rkB/s:  每秒读K字节数。是 rsect/s 的一半，因为每扇区大小为512字节。
    * wkB/s:  每秒写K字节数。是 wsect/s 的一半。
    * avgrq-sz:  平均每次设备I/O操作的数据大小 (扇区)。
    * avgqu-sz:  平均I/O队列长度。
    * await:  平均每次设备I/O操作的等待时间 (毫秒)。
    * svctm: 平均每次设备I/O操作的服务时间 (毫秒)。
    * %util:  一秒中有百分之多少的时间用于 I/O 操作，即被io消耗的cpu百分比

备注：如果 %util 接近 100%，说明产生的I/O请求太多，I/O系统已经满负荷，该磁盘可能存在瓶颈。如果 svctm 比较接近 await，说明 I/O 几乎没有等待时间；如果 await 远大于 svctm，说明I/O 队列太长，io响应太慢，则需要进行必要优化。如果avgqu-sz比较大，也表示有当量io在等待。


实例2：定时显示所有信息
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	/root$iostat 2 3
	Linux 2.6.32-279.el6.x86_64 (colin)   07/16/2014      _x86_64_        (4 CPU)
	
	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
	10.81    0.00   14.11    0.18    0.00   74.90
	
	Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
	sda               1.95         1.48        70.88    9145160  437106156
	dm-0              3.08         0.55        24.34    3392770  150088376
	dm-1              5.83         0.93        46.49    5714522  286728384
	dm-2              0.01         0.00         0.05      23930     289288
	
	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
	22.62    0.00   19.67    0.26    0.00   57.46
	
	Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
	sda               2.50         0.00        28.00          0         56
	dm-0              0.00         0.00         0.00          0          0
	dm-1              3.50         0.00        28.00          0         56
	dm-2              0.00         0.00         0.00          0          0
	
	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
	22.69    0.00   19.62    0.00    0.00   57.69
	
	Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
	sda               0.00         0.00         0.00          0          0
	dm-0              0.00         0.00         0.00          0          0
	dm-1              0.00         0.00         0.00          0          0
	dm-2              0.00         0.00         0.00          0          0
	

说明：每隔 2秒刷新显示，且显示3次

实例3：查看TPS和吞吐量
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	/root$iostat -d -k 1 1
	Linux 2.6.32-279.el6.x86_64 (colin)   07/16/2014      _x86_64_        (4 CPU)
	
	Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
	sda               1.95         0.74        35.44    4572712  218559410
	dm-0              3.08         0.28        12.17    1696513   75045968
	dm-1              5.83         0.46        23.25    2857265  143368744
	dm-2              0.01         0.00         0.02      11965     144644


- tps：该设备每秒的传输次数（Indicate the number of transfers per second that were issued to the device.）。“一次传输”意思是“一次I/O请求”。多个逻辑请求可能会被合并为“一次I/O请求”。“一次传输”请求的大小是未知的。
- kB_read/s：每秒从设备（drive expressed）读取的数据量；
- kB_wrtn/s：每秒向设备（drive expressed）写入的数据量；
- kB_read：读取的总数据量；kB_wrtn：写入的总数量数据量；

这些单位都为Kilobytes。

上面的例子中，我们可以看到磁盘sda以及它的各个分区的统计数据，当时统计的磁盘总TPS是1.95，下面是各个分区的TPS。（因为是瞬间值，所以总TPS并不严格等于各个分区TPS的总和）


实例4：查看设备使用率（%util）和响应时间（await）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	/root$iostat -d -x -k 1 1
	Linux 2.6.32-279.el6.x86_64 (colin)   07/16/2014      _x86_64_        (4 CPU)
	
	Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await  svctm  %util
	sda               0.02     7.25    0.04    1.90     0.74    35.47    37.15     0.04   19.13   5.58   1.09
	dm-0              0.00     0.00    0.04    3.05     0.28    12.18     8.07     0.65  209.01   1.11   0.34
	dm-1              0.00     0.00    0.02    5.82     0.46    23.26     8.13     0.43   74.33   1.30   0.76
	dm-2              0.00     0.00    0.00    0.01     0.00     0.02     8.00     0.00    5.41   3.28   0.00

- rrqm/s：  每秒进行 merge 的读操作数目.即 delta(rmerge)/s
- wrqm/s： 每秒进行 merge 的写操作数目.即 delta(wmerge)/s
- r/s：  每秒完成的读 I/O 设备次数.即 delta(rio)/s
- w/s：  每秒完成的写 I/O 设备次数.即 delta(wio)/s
- rsec/s：  每秒读扇区数.即 delta(rsect)/s
- wsec/s： 每秒写扇区数.即 delta(wsect)/s
- rkB/s：  每秒读K字节数.是 rsect/s 的一半,因为每扇区大小为512字节.(需要计算)
- wkB/s：  每秒写K字节数.是 wsect/s 的一半.(需要计算)
- avgrq-sz：平均每次设备I/O操作的数据大小 (扇区).delta(rsect+wsect)/delta(rio+wio)
- avgqu-sz：平均I/O队列长度.即 delta(aveq)/s/1000 (因为aveq的单位为毫秒).
- await：  平均每次设备I/O操作的等待时间 (毫秒).即 delta(ruse+wuse)/delta(rio+wio)
- svctm： 平均每次设备I/O操作的服务时间 (毫秒).即 delta(use)/delta(rio+wio)
- %util： 一秒中有百分之多少的时间用于 I/O 操作,或者说一秒中有多少时间 I/O 队列是非空的，即 delta(use)/s/1000 (因为use的单位为毫秒)

如果 %util 接近 100%，说明产生的I/O请求太多，I/O系统已经满负荷，该磁盘可能存在瓶颈。
idle小于70% IO压力就较大了，一般读取速度有较多的wait。
同时可以结合vmstat 查看查看b参数(等待资源的进程数)和wa参数(IO等待所占用的CPU时间的百分比，高过30%时IO压力高)。

另外 await 的参数也要多和 svctm 来参考。差的过高就一定有 IO 的问题。

avgqu-sz 也是个做 IO 调优时需要注意的地方，这个就是直接每次操作的数据的大小，如果次数多，但数据拿的小的话，其实 IO 也会很小。如果数据拿的大，才IO 的数据会高。也可以通过 avgqu-sz × ( r/s or w/s ) = rsec/s or wsec/s。也就是讲，读定速度是这个来决定的。

svctm 一般要小于 await (因为同时等待的请求的等待时间被重复计算了)，svctm 的大小一般和磁盘性能有关，CPU/内存的负荷也会对其有影响，请求过多也会间接导致 svctm 的增加。await 的大小一般取决于服务时间(svctm) 以及 I/O 队列的长度和 I/O 请求的发出模式。如果 svctm 比较接近 await，说明 I/O 几乎没有等待时间；如果 await 远大于 svctm，说明 I/O 队列太长，应用得到的响应时间变慢，如果响应时间超过了用户可以容许的范围，这时可以考虑更换更快的磁盘，调整内核 elevator 算法，优化应用，或者升级 CPU。

队列长度(avgqu-sz)也可作为衡量系统 I/O 负荷的指标，但由于 avgqu-sz 是按照单位时间的平均值，所以不能反映瞬间的 I/O 洪水。

形象的比喻：
    * r/s+w/s 类似于交款人的总数
    * 平均队列长度(avgqu-sz)类似于单位时间里平均排队人的个数
    * 平均服务时间(svctm)类似于收银员的收款速度
    * 平均等待时间(await)类似于平均每人的等待时间
    * 平均I/O数据(avgrq-sz)类似于平均每人所买的东西多少
    * I/O 操作率 (%util)类似于收款台前有人排队的时间比例

设备IO操作:总IO(io)/s = r/s(读) +w/s(写)

平均等待时间=单个I/O服务器时间*(1+2+...+请求总数-1)/请求总数

每秒发出的I/0请求很多,但是平均队列就4,表示这些请求比较均匀,大部分处理还是比较及时。
