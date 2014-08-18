进程管理工具
=====================
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


综合运用
----------------
将用户colin115下的所有进程名以av_开头的进程终止：
::

	ps -u colin115 |  awk '/av_/ {print "kill -9 " $1}' | sh


总结
----------
ps top lsof kill
