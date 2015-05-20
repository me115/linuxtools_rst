.. _04_disk:

磁盘管理
========

.. contents:: 目录


日程磁盘管理中，我们最常用的有查看当前磁盘使用情况，查看当前目录所占大小，以及打包压缩与解压缩；


查看磁盘空间
-----------------------
查看磁盘空间利用大小::

    df -h
-h: human缩写，以易读的方式显示结果（即带单位：比如M/G，如果不加这个参数，显示的数字以B为单位）

::

	$df -h
	/opt/app/todeav/config#df -h
	Filesystem            Size  Used Avail Use% Mounted on
	/dev/mapper/VolGroup00-LogVol00
	2.0G  711M  1.2G  38% /
	/dev/mapper/vg1-lv2    20G  3.8G   15G  21% /opt/applog
	/dev/mapper/vg1-lv1    20G   13G  5.6G  70% /opt/app
	


查看当前目录所占空间大小::

    du -sh

- -h 人性化显示
- -s 递归整个目录的大小

::

	$du -sh
	653M


查看当前目录下所有子文件夹排序后的大小::

    for i in `ls`; do du -sh $i; done | sort
    或者：
    du -sh `ls` | sort


打包/ 压缩
-------------------
在linux中打包和压缩和分两步来实现的；

**打包**

打包是将多个文件归并到一个文件::

    tar -cvf etc.tar /etc <==仅打包，不压缩！

- -c :打包选项
- -v :显示打包进度
- -f :使用档案文件
注：有的系统中指定参数时不需要在前面加上-，直接使用tar xvf

示例：用tar实现文件夹同步，排除部分文件不同步::

    tar --exclude '*.svn' -cvf - /path/to/source | ( cd /path/to/target; tar -xf -)

**压缩**
::

    $gzip demo.txt
生成 demo.txt.gz

解包/解压缩
---------------------
**解包**
::

    tar -xvf demo.tar
-x 解包选项

解压后缀为 .tar.gz的文件
1. 先解压缩，生成**.tar::

    $gunzip    demo.tar.gz
2. 解包::

    $tar -xvf  demo.tar
    $bzip2 -d demo.tar.bz2

bz2解压::

    tar jxvf demo.tar.bz2
如果tar 不支持j，则同样需要分两步来解包解压缩，使用bzip2来解压，再使用tar解包::

    bzip2 -d  demo.tar.bz2
    tar -xvf  demo.tar
-d decompose,解压缩

tar解压参数说明：

- -z 解压gz文件
- -j 解压bz2文件
- -J 解压xz文件

总结
-----------
查看磁盘空间 df -h

查看目录大小 du -sh

打包  tar -cvf

解包 tar -xvf

压缩 gzip

解压缩 gunzip bzip
