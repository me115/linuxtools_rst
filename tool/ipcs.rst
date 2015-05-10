.. _ipcs:

ipcs 查询进程间通信状态
==========================

ipcs是Linux下显示进程间通信设施状态的工具。可以显示消息队列、共享内存和信号量的信息。对于程序员非常有用，普通的系统管理员一般用不到此指令。


IPC资源查询
--------------------
查看系统使用的IPC资源
^^^^^^^^^^^^^^^^^^^^^^
::

    $ipcs

    ------ Shared Memory Segments --------
    key        shmid      owner      perms      bytes      nattch     status      

    ------ Semaphore Arrays --------
    key        semid      owner      perms      nsems     
    0x00000000 229376     weber      600        1         

    ------ Message Queues --------
    key        msqid      owner      perms      used-bytes   messages    

分别查询IPC资源::
    
    $ipcs -m 查看系统使用的IPC共享内存资源
    $ipcs -q 查看系统使用的IPC队列资源
    $ipcs -s 查看系统使用的IPC信号量资源

查看IPC资源被谁占用
^^^^^^^^^^^^^^^^^^^^
示例：有个IPCKEY(51036)，需要查询其是否被占用；

1. 首先通过计算器将其转为十六进制::

    51036 -> c75c
2. 如果知道是被共享内存占用::

    $ipcs -m | grep c75c
    0x0000c75c 40403197   tdea3    666        536870912  2

3. 如果不确定，则直接查找::

    $ipcs | grep c75c
    0x0000c75c 40403197   tdea3    666        536870912  2
    0x0000c75c 5079070    tdea3    666        4

系统IPC参数查询
--------------------
::

     ipcs -l
           
     ------ Shared Memory Limits --------
     max number of segments = 4096
     max seg size (kbytes) = 4194303
     max total shared memory (kbytes) = 1073741824
     min seg size (bytes) = 1
   
     ------ Semaphore Limits --------
     max number of arrays = 128
     max semaphores per array = 250
     max semaphores system wide = 32000
     max ops per semop call = 32
     semaphore max value = 32767
   
     ------ Messages: Limits --------
     max queues system wide = 2048
     max size of message (bytes) = 524288
     default max size of queue (bytes) = 5242880

以上输出显示，目前这个系统的允许的最大内存为1073741824kb；最大可使用128个信号量，每个消息的最大长度为524288bytes；

修改IPC系统参数
--------------------
以linux系统为例，在root用户下修改/etc/sysctl.conf 文件，保存后使用sysctl -p生效::

     $cat /etc/sysctl.conf
     # 一个消息的最大长度
     kernel.msgmax = 524288
     
     # 一个消息队列上的最大字节数
     # 524288*10
     kernel.msgmnb = 5242880

     #最大消息队列的个数
     kernel.msgmni=2048
   
     #一个共享内存区的最大字节数
     kernel.shmmax = 17179869184
   
     #系统范围内最大共享内存标识数
     kernel.shmmni=4096
   
     #每个信号灯集的最大信号灯数 系统范围内最大信号灯数 每个信号灯支持的最大操作数 系统范围内最大信号灯集数
     #此参数为系统默认，可以不用修改
     #kernel.sem = <semmsl> <semmni>*<semmsl> <semopm> <semmni>
     kernel.sem = 250 32000 32 128


显示输入不带标志的 ipcs：的输出::

    $ipcs
    IPC status from /dev/mem as of Mon Aug 14 15:03:46 1989
    T    ID         KEY        MODE       OWNER     GROUP
    Message Queues:
    q       0    0x00010381 -Rrw-rw-rw-   root      system
    q   65537    0x00010307 -Rrw-rw-rw-   root      system
    q   65538    0x00010311 -Rrw-rw-rw-   root      system
    q   65539    0x0001032f -Rrw-rw-rw-   root      system
    q   65540    0x0001031b -Rrw-rw-rw-   root      system
    q   65541    0x00010339--rw-rw-rw-    root      system
    q       6    0x0002fe03 -Rrw-rw-rw-   root      system
    Shared Memory:
    m   65537    0x00000000 DCrw-------   root      system
    m  720898    0x00010300 -Crw-rw-rw-   root      system
    m   65539    0x00000000 DCrw-------   root      system
    Semaphores:
    s  131072    0x4d02086a --ra-ra----   root      system
    s   65537    0x00000000 --ra-------   root      system
    s 1310722    0x000133d0 --ra-------   7003      30720


清除IPC资源
--------------------
使用ipcrm 命令来清除IPC资源：这个命令同时会将与ipc对象相关联的数据也一起移除。当然，只有root用户，或者ipc对象的创建者才有这项权利；

ipcrm用法::

    ipcrm -M shmkey  移除用shmkey创建的共享内存段
    ipcrm -m shmid    移除用shmid标识的共享内存段
    ipcrm -Q msgkey  移除用msqkey创建的消息队列
    ipcrm -q msqid  移除用msqid标识的消息队列
    ipcrm -S semkey  移除用semkey创建的信号
    ipcrm -s semid  移除用semid标识的信号

清除当前用户创建的所有的IPC资源::

    ipcs -q | awk '{ print "ipcrm -q "$2}' | sh > /dev/null 2>&1;
    ipcs -m | awk '{ print "ipcrm -m "$2}' | sh > /dev/null 2>&1;
    ipcs -s | awk '{ print "ipcrm -s "$2}' | sh > /dev/null 2>&1;

综合应用
--------------------
查询user1用户环境上是否存在积Queue现象
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. 查询队列Queue::

    $ipcs -q

    ------ Message Queues --------
    key        msqid      owner      perms      used-bytes   messages    
    0x49060005 58261504   user1    660        0            0           
    0x4f060005 58294273   user1    660        0            0          
    ...

2. 找出第6列大于0的服务::

    $ ipcs -q |grep user1 |awk '{if($5>0) print $0}'
    0x00000000 1071579324 user1       644        1954530      4826        
    0x00000000 1071644862 user1       644        1961820      4844        
    0x00000000 1071677631 user1       644        1944810      4802        
    0x00000000 1071710400 user1       644        1961820      4844   

