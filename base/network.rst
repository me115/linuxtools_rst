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


