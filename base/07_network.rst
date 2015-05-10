.. _07_network:

网络工具
====================

.. contents:: 目录

查询网络服务和端口
--------------------
netstat 命令用于显示各种网络相关信息，如网络连接，路由表，接口状态 (Interface Statistics)，masquerade 连接，多播成员 (Multicast Memberships) 等等。


列出所有端口 (包括监听和未监听的)::

    netstat -a

列出所有 tcp 端口::
    
    netstat -at

列出所有有监听的服务状态::

    netstat -l

使用netstat工具查询端口:: 

    $netstat -antp | grep 6379
    tcp        0      0 127.0.0.1:6379          0.0.0.0:*               LISTEN      25501/redis-server
    
    $ps 25501
      PID TTY      STAT   TIME COMMAND
    25501 ?        Ssl   28:21 ./redis-server ./redis.conf
    
lsof（list open files）是一个列出当前系统打开文件的工具。在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。所以如传输控制协议 (TCP) 和用户数据报协议 (UDP) 套接字等；
在查询网络端口时，经常会用到这个工具。

查询7902端口现在运行什么程序::

    #分为两步
    #第一步，查询使用该端口的进程的PID；
	$lsof -i:7902
	COMMAND   PID   USER   FD   TYPE    DEVICE SIZE NODE NAME
	WSL     30294 tuapp    4u  IPv4 447684086       TCP 10.6.50.37:tnos-dp (LISTEN)
    
    #查到30294
    #使用ps工具查询进程详情：
    $ps -fe | grep 30294
    tdev5  30294 26160  0 Sep10 ?        01:10:50 tdesl -k 43476
    root     22781 22698  0 00:54 pts/20   00:00:00 grep 11554

.. note::
    
    以上介绍lsof关于网络方面的应用，这个工具非常强大，需要好好掌握，详见 :ref:`lsof` ;


网络路由
--------------------
查看路由状态::

    $route -n

发送ping包到地址IP::

    $ping IP

探测前往地址IP的路由路径::
    
    $traceroute IP

DNS查询，寻找域名domain对应的IP::

    $host domain

反向DNS查询::

    $host IP

镜像下载
--------------------
直接下载文件或者网页::
    
    wget url

常用选项:

- --limit-rate :下载限速
- -o：指定日志文件；输出都写入日志；
- -c：断点续传


ftp sftp lftp ssh
--------------------

SSH登陆::

    $ssh ID@host
ssh登陆远程服务器host，ID为用户名。


ftp/sftp文件传输::

    $sftp ID@host

登陆服务器host，ID为用户名。sftp登陆后，可以使用下面的命令进一步操作：

- get filename    # 下载文件
- put filename    # 上传文件
- ls              # 列出host上当前路径的所有文件
- cd              # 在host上更改当前路径
- lls             # 列出本地主机上当前路径的所有文件
- lcd             # 在本地主机更改当前路径

lftp同步文件夹(类似rsync工具)::

    lftp -u user:pass host
    lftp user@host:~> mirror -n
    

网络复制
--------------------
将本地localpath指向的文件上传到远程主机的path路径::

    $scp localpath ID@host:path

以ssh协议，遍历下载path路径下的整个文件系统，到本地的localpath::

    $scp -r ID@site:path localpath

总结
--------------------
netstat lsof route ping host wget  sftp scp 
