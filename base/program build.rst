make
必须满足第一条规则，满足后停止
除第一条规则，其他无顺序
变量
所有全局
自变量
$@目标文件名
@^所有前提名，除副本
@＋所有前提名，含副本
@＜一个前提名
@？所有新于目标文件的前提名
@*目标文件的基名称
？
为什么有的是@，有的没有？
make -f ompdb.mf  :通过使用-f选项来确定

配置
./configure --help 查看可用的配置选项
CPPFLAGS -I标记 非标准头文件存放路径
LDFLAGS  -L标记 非标准库存放路径
链接多库，右边是左边的前提


g++ 使用
CC=gcc ./configure --prefix=/userhome/jhuang/openav
g++ 编译：选项说明 ：-o:指明生成的目标文件
g++ -o unixApp unixApp.o a.o b.o
生成中间文件（不直接生产目标文件）:.o
g++ -c a.o
-g：添加调试信息

查看软件安装路径： which gcc
查看gcc的动态连接库： ldd gcc
ldd，查询应用程序需要链接的库： ldd avetes

