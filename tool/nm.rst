目标文件格式分析工具系列（nm、objdump、readelf）
nm:
用途：
显示关于对象文件、可执行文件以及对象文件库里的符号信息。

eg：
有时会碰到一个编译了但没有链接的代码，那是因为它缺失了标识符；这种情况，可以用nm和objdump、readelf命令来查看程序的符号表；所有这些命令做的工作基本一样；
比如连接器报错有未定义的标识符；大多数情况下，会发生在库的缺失或企图链接一个i额错误版本的库的时候；要浏览目标代码来寻找一个特殊标识符的引用：可以使用
nm -uCA *.o | grep foo
-u选项限制了每个目标文件中未定义标识符的输出。-A选项用于显示每个标识符的文件名信息；对于C++代码，常用的还有-C选项，它也为解码这些标识符；

objdump、readld命令可以完成同样的任务。等效命令为：
objdump  -t
readelf -s
查看.o文件是否编入了调试信息（编译的时候是否加了-g):
readelf -S ShmNpos.o | grep debug


关于nm的更多详细用法请参考：
http://blog.chinaunix.net/uid-28458801-id-3475711.html


objdump
作用：显示二进制文件的信息。用来解剖二进制文件；

eg：
查看本机目标机构（使用大端还是小端存储）：objdump -i

反汇编程序：objdump -d mian.o
/opt/app/todeav1/test$objdump -d main.o
显示符号表入口：objdump  -t main.o
希望显示可用的简洁帮助信息，直接输入objdump即可；（objdump -H)
更多详解参考：http://quietheart.blog.51cto.com/1933493/620069


