.. _08_user_manage:

用户管理工具
====================

.. contents:: 目录

用户
---------------------

添加用户
^^^^^^^^^^^^^^^^^^^^

::

    $useradd -m username

该命令为用户创建相应的帐号和用户目录/home/username；

用户添加之后，设置密码：

密码以交互方式创建::

    $passwd username


删除用户
^^^^^^^^^^^^^^^^^^^^

::

    $userdel -r username
不带选项使用 userdel，只会删除用户。用户的家目录将仍会在/home目录下。要完全的删除用户信息，使用-r选项；

帐号切换
登录帐号为userA用户状态下，切换到userB用户帐号工作::

    $su userB
进入交互模型，输入密码授权进入；

用户的组
--------------------

将用户加入到组
^^^^^^^^^^^^^^^^^^^^
默认情况下，添加用户操作也会相应的增加一个同名的组，用户属于同名组；
查看当前用户所属的组::

    $groups

一个用户可以属于多个组，将用户加入到组::

    $usermod -G groupNmame username

变更用户所属的根组(将用加入到新的组，并从原有的组中除去）::

    $usermod -g groupName username

查看系统所有组
^^^^^^^^^^^^^^^^^^^^
系统的所有用户及所有组信息分别记录在两个文件中：/etc/passwd , /etc/group
默认情况下这两个文件对所有用户可读：

查看所有用户及权限::

    $more /etc/passwd

查看所有的用户组及权限::

    $more /etc/group

用户权限
-----------------
使用ls -l可查看文件的属性字段，文件属性字段总共有10个字母组成，第一个字母表示文件类型，如果这个字母是一个减号"-",则说明该文件是一个普通文件。字母"d"表示该文件是一个目录，字母"d",是dirtectory(目录)的缩写。
后面的9个字母为该文件的权限标识，3个为一组，分别表示文件所属用户、用户所在组、其它用户的读写和执行权限；
例如:
::

	[/home/weber#]ls -l /etc/group
	-rwxrw-r-- colin king 725 2013-11-12 15:37 /home/colin/a

表示这个文件对文件拥有者colin这个用户可读写、可执行；对colin所在的组（king）可读可写；对其它用户只可读；

更改读写权限
^^^^^^^^^^^^^^^^^^^^
使用chmod命令更改文件的读写权限，更改读写权限有两种方法，一种是字母方式，一种是数字方式

字母方式::

    $chmod userMark(+|-)PermissionsMark
userMark取值：

- u：用户  
- g：组 
- o：其它用户 
- a：所有用户
PermissionsMark取值：

- r:读  
- w：写   
- x：执行

例如::

    $chmod a+x main         对所有用户给文件main增加可执行权限
    $chmod g+w blogs        对组用户给文件blogs增加可写权限

数字方式：

数字方式直接设置所有权限，相比字母方式，更加简洁方便；

使用三位八进制数字的形式来表示权限，第一位指定属主的权限，第二位指定组权限，第三位指定其他用户的权限，每位通过4(读)、2(写)、1(执行)三种数值的和来确定权限。如6(4+2)代表有读写权，7(4+2+1)有读、写和执行的权限。

例如::

    $chmod 740 main     将main的用户权限设置为rwxr-----


更改文件或目录的拥有者
^^^^^^^^^^^^^^^^^^^^^^
::

    $chown username dirOrFile
使用-R选项递归更改该目下所有文件的拥有者::

    $chown -R weber server/


环境变量
--------------------
bashrc与profile都用于保存用户的环境信息，bashrc用于交互式non-loginshell，而profile用于交互式login shell。

| /etc/profile，/etc/bashrc 是系统全局环境变量设定
| ~/.profile，~/.bashrc用户目录下的私有环境变量设定
| 

当登入系统获得一个shell进程时，其读取环境设置脚本分为三步:

1. 首先读入的是全局环境变量设置文件/etc/profile，然后根据其内容读取额外的文档，如/etc/profile.d和/etc/inputrc
#. 读取当前登录用户Home目录下的文件~/.bash_profile，其次读取~/.bash_login，最后读取~/.profile，这三个文档设定基本上是一样的，读取有优先关系
#. 读取~/.bashrc

~/.profile与~/.bashrc的区别:

- 这两者都具有个性化定制功能
- ~/.profile可以设定本用户专有的路径，环境变量，等，它只能登入的时候执行一次
- ~/.bashrc也是某用户专有设定文档，可以设定路径，命令别名，每次shell script的执行都会使用它一次

例如，我们可以在这些环境变量中设置自己经常进入的文件路径，以及命令的快捷方式：
::

	.bashrc
	alias m='more'
	alias cp='cp -i'
	alias mv='mv -i'
	alias ll='ls -l'
	alias lsl='ls -lrt'
	alias lm='ls -al|more'
	
	log=/opt/applog/common_dir
	unit=/opt/app/unittest/common
	
	.bash_profile
	. /opt/app/tuxapp/openav/config/setenv.prod.sh.linux
	export PS1='$PWD#'

通过上述设置，我们进入log目录就只需要输入cd $log即可；

总结
--------------------
useradd passwd userdel usermod chmod chown .bashrc .bash_profile
