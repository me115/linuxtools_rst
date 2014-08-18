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
