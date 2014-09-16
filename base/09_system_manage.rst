.. _09_system_manage:


系统管理、硬件管理及IPC资源管理
=================================

查看Linux系统版本：
uname -a
lsb_release -a
查看Unix系统版本：操作系统版本
more /etc/release

POSIX与V系统的区别
P为每个对象使用一个文件描述符 一切皆文件


查看CPU使用情况
$sar -u 5 10

查询CPU信息
$cat /proc/cpuinfo

查看CPU的核的个数
$cat /proc/cpuinfo | grep processor | wc -l

查看内存信息
$cat /proc/meminfo

显示内存page大小（以KByte为单位）
$pagesize


显示架构

$arch

IPC资源占用
查看IPCKEY被占用：
有个IPCKEY：51036 ，需要查询其是否被占用；
首先通过计算器将其转为十六进制：
如果知道是否共享内存见占用：
/opt/app/todeav3/bin$ipcs -m | grep c75c
0x0000c75c 40403197   todeav3    666        536870912  2
如果不确定，则直接查找：
/opt/app/todeav3/bin$ipcs | grep c75c
0x0000c75c 40403197   todeav3    666        536870912  2
0x0000c75c 5079070    todeav3    666        4

ulimit 检测和设置系统资源限制


设置系统时间
--------------------
需要通过root用户设置；


date 显示当前系统时间
date -s 设置系统日期和时间：格式为2014-09-15 17:05:00
clock -w 这个命令强制把系统时间写入CMOS（这样，重启后时间也正确了）

/root$date -s 2014-09-15
Mon Sep 15 00:00:00 CST 2014
/root$date
Mon Sep 15 00:00:03 CST 2014
/root$date -s 17:05:00
Mon Sep 15 17:05:00 CST 2014
/root$date
Mon Sep 15 17:05:04 CST 2014
/root$clock -w
