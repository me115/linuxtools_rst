ldd
作用：用来查看程式运行所需的共享库,常用来解决程式因缺少某个库文件而不能运行的一些问题。
eg：查看test程序运行所依赖的库：
::

	/opt/app/todeav1/test$ldd test
	libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00000039a7e00000)
	libm.so.6 => /lib64/libm.so.6 (0x0000003996400000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00000039a5600000)
	libc.so.6 => /lib64/libc.so.6 (0x0000003995800000)
	/lib64/ld-linux-x86-64.so.2 (0x0000003995400000)


如果依赖的某个库找不到，通过这个命令则一目了然；
原理：
ldd不是个可执行程式，而只是个shell脚本；
ldd显示可执行模块的dependency的工作原理，其实质是通过ld-linux.so（elf动态库的装载器）来实现的。ld-linux.so模块会先于executable模块程式工作，并获得控制权，因此当上述的那些环境变量被设置时，ld-linux.so选择了显示可执行模块的dependency。

