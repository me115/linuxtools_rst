文件及目录管理
==========================
文件管理不外乎文件或目录的创建、删除、查询、移动，有mkdir/rm/mv

文件查询是重点，用find来进行查询；find的参数丰富，也非常强大；

查看文件内容是个大的话题，文本的处理有太多的工具供我们使用，在本章中只是点到即止，后面会有专门的一章来介绍文本的处理工具；

有时候，需要给文件创建一个别名，我们需要用到ln，使用这个别名和使用原文件是相同的效果；

创建和删除
--------------------
创建：mkdir
删除：rm   删除非空目录：rm -rf file目录
删除日志
$rm *log

等价: $find ./ -name "*log" -exec rm {} \;

查看当前目录下文件个数
$find ./ | wc -l
移动：mv
复制：cp   复制目录：cp -r
eg：$cp -r source_dir  dest_dir

目录切换
-------------------
找到文件/目录位置：cd
切换到上一个工作目录： cd -
切换到home目录： cd  or  cd ~
$pwd
显示当前路径
$cd path
更改当前工作路径为path

列出目录项
--------------------
显示当前目录下的文件 ls
按时间排序，以列表的方式显示目录项 ls -lrt
以上这个命令用到的频率如此之高，以至于我们需要为它建立一个快捷命令方式:
在.bashrc 中设置命令别名：
alias lsl='ls -lrt'
alias lm='ls -al|more'
这样，使用lsl，就可以显示目录中的文件按照修改时间排序；以列表方式显示；
注：.bashrc 在/home/你的用户名/ 文件夹下，以隐藏文件的方式存储；可使用 ls -a 查看；

查找目录及文件 find/locate
----------------------------------------
搜寻文件或目录：
$find ./ -name "core*" | xargs file
查找目标文件夹中是否有obj文件：
$find ./ -name '*.o'
递归当前目录及子目录删除所有.o文件：
$find ./ -name "*.o" -exec rm {} \;

find是实时查找，如果需要更快的查询，可试试locate；locate会为文件系统建立索引数据库，如果有文件更新，需要定期执行更新命令来更新索引库；
$locate string
寻找包含有string的路径
$updatedb
与find不同，locate并不是实时查找。你需要更新数据库，以获得最新的文件索引信息。

查看文件内容
-----------------------
查看文件：cat vi head tail more
$cat -n：显示时同时显示行号
$ls -al |more:一页一页显示列表内容；
$head - 10 **:只看前10行
$head -1 filename 显示文件第一行
$tail -5 filename 显示文件倒数第五行
$diff file1 file2 查看两个文件间的差别
$tail -f crawler.log 动态显示文本最新信息

查找文件内容
-----------------------
egrep '03.1\/CO\/AE' TSF_STAT_111130.log.012
egrep 'A_LSHA777:C' TSF_STAT_111130.log.035 > co.out2
co.out35:  egrep 'A_LSHA777:C' TSF_STAT_111130.log.035 > co.out35

文件与目录权限修改
--------------------------------
chown：改变文件的拥有者
chmod：改变文件读、写、执行等属性
递归子目录修改： chown -R tuxapp source/
增加脚本可执行权限： chmod a+x  myscript


给文件增加别名
--------------------------
创建符号链接/硬链接：
ln cc ccAgain :硬连接；删除一个，将仍能找到；
ln -s cc ccTo :符号链接(软链接)；删除源，另一个无法使用；（后面一个ccTo 为新建的文件）


管道和重定向
-----------------------
批处理命令连接执行：
串联: 使用分号 ;
前面成功，则执行后面一条，否则，不执行:&&
前面失败，则后一条执行:    ||
eg：
ls /proc && echo  suss! || echo failed.
能够提示命名是否执行成功or失败；
与上述相同效果的是：
if ls /proc; then echo suss; else echo fail; fi
重定向：
ls  proc/*.c > list > &l 将结果输出到list，将错误输出到同一个文件末尾；
等价的是：ls  proc/*.c &> list
ls list1 list2：可同时列出多个文件；

清空文件：   :> a.txt
重定向：最佳文本：  echo  aa >> a.txt

设置环境变量
-----------------------
启动帐号后自动执行的是 文件为 .profile，然后通过这个文件可设置自己的环境变量；
安装的软件路径一般需要加入到path中：
PATH=$APPDIR:/opt/app/soft/bin:$PATH:/usr/local/bin:$TUXDIR/bin:$ORACLE_HOME/bin;export PATH

Bash快捷输入或删除
------------------------------
快捷键：
Ctl-U   删除光标到行首的所有字符,在某些设置下,删除全行
Ctl-W   删除当前光标到前边的最近一个空格之间的字符
Ctl-H   backspace,删除光标前边的字符
Ctl-R： 匹配最相近的一个文件，然后输出

综合应用
-----------------
cat -v record.log | grep AAA | grep -v BBB | wc -l
查找record.log中包含AAA，但不包含BBB的记录的总数

总结
-----------
文件管理，目录的创建、删除、查询、管理: mkdir rm mv
文件的查询和检索: find locate
查看文件内容：cat vi tail more
管道和重定向: ; | &&  >



Posted by: 大CC | 26MAY,2014
博客：[blog.me115.com](http://blog.me115.com)
微博：[新浪微博](http://weibo.com/bigcc115)
