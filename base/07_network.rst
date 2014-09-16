.. _07_network:

网络工具
====================


网络：
查看网络的联机状态：netstat -a

网络
$ifconfig

显示网络接口以及相应的IP地址。ifconfig可用于设置网络接口

$ifup eth0

运行eth0接口

$ifdown eth0

关闭eth0接口

$iwconfig

显示无线网络接口

$route

显示路由表。route还可以用于修改路由表

$netstat


查询7902端口现在运行什么程序
::

	/home/tuxapp>lsof -i:7902
	COMMAND   PID   USER   FD   TYPE    DEVICE SIZE NODE NAME
	WSL     30294 tuxapp    4u  IPv4 447684086       TCP 10.6.50.37:tnos-dp (LISTEN)


使用netstat -antp | grep 11005
:: 

    /root$lsof -i:11005
    COMMAND   PID    USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
    todewsl 11554 todeav5    3u  IPv4 7528480      0t0  TCP pricing:11005 (LISTEN)
    /root$netstat -antp | grep 11005
    tcp        0      0 172.27.19.103:11005         0.0.0.0:*                   LISTEN      11554/todewsl       
    /root$ps 11554
      PID TTY      STAT   TIME COMMAND
    11554 ?        S     70:50 todewsl -k 43476
    /root$ps -fe | grep 11554
    todeav5  11554 26160  0 Sep10 ?        01:10:50 todewsl -k 43476
    root     22781 22698  0 00:54 pts/20   00:00:00 grep 11554



显示当前的网络连接状态

$ping IP

发送ping包到地址IP

$traceroute IP

探测前往地址IP的路由路径

$dhclient

向DHCP主机发送DHCP请求，以获得IP地址以及其他设置信息。

$host domain

DNS查询，寻找域名domain对应的IP

$host IP

反向DNS查询

$wget url

使用wget下载url指向的资源

$wget -m url

镜像下载

网站下载
wget url：直接下载文件或者网页；
--limit-rate :下载限速，别太快
-o：指定日志文件；输出都写入日志；
-c：断点续传


端口被占用后查看：
netstat -anp| grep 33554
/root$netstat -anp| grep 33554
tcp        0      0 127.0.0.1:33554             0.0.0.0:*                   LISTEN      13398/todebridge    

进一步查看是那个进程占用的：
/root$ps -fe| grep 13398
msgav8   13398 13394  0 19:32 ?        00:00:15 todebridge -k 222558 -p 0
root     17915 17873  0 22:25 pts/3    00:00:00 grep 13398

找到msgav8


ftp sftp ssh
================

SSH登陆与文件传输
$ssh ID@host

ssh登陆远程服务器host，ID为用户名。

$sftp ID@host

登陆服务器host，ID为用户名。sftp登陆后，可以使用下面的命令进一步操作：

get filename    # 下载文件

put filename    # 上传文件

ls              # 列出host上当前路径的所有文件

cd              # 在host上更改当前路径

lls             # 列出本地主机上当前路径的所有文件

lcd             # 在本地主机更改当前路径

$scp localpath ID@host:path

将本地localpath指向的文件上传到远程主机的path路径

$scp -r ID@site:path localpath

以ssh协议，遍历下载path路径下的整个文件系统，到本地的localpath

