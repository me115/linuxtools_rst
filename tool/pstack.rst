.. _pstack:

pstack 跟踪进程栈
====================

此命令可显示每个进程的栈跟踪。pstack 命令必须由相应进程的属主或 root 运行。可以使用 pstack 来确定进程挂起的位置。此命令允许使用的唯一选项是要检查的进程的 PID。请参见 proc(1) 手册页。

这个命令在排查进程问题时非常有用，比如我们发现一个服务一直处于work状态（如假死状态，好似死循环），使用这个命令就能轻松定位问题所在；可以在一段时间内，多执行几次pstack，若发现代码栈总是停在同一个位置，那个位置就需要重点关注，很可能就是出问题的地方；

示例：查看bash程序进程栈::

    /opt/app/tdev1$ps -fe| grep bash
    tdev1   7013  7012  0 19:42 pts/1    00:00:00 -bash
    tdev1  11402 11401  0 20:31 pts/2    00:00:00 -bash
    tdev1  11474 11402  0 20:32 pts/2    00:00:00 grep bash
    /opt/app/tdev1$pstack 7013
    #0  0x00000039958c5620 in __read_nocancel () from /lib64/libc.so.6
    #1  0x000000000047dafe in rl_getc ()
    #2  0x000000000047def6 in rl_read_key ()
    #3  0x000000000046d0f5 in readline_internal_char ()
    #4  0x000000000046d4e5 in readline ()
    #5  0x00000000004213cf in ?? ()
    #6  0x000000000041d685 in ?? ()
    #7  0x000000000041e89e in ?? ()
    #8  0x00000000004218dc in yyparse ()
    #9  0x000000000041b507 in parse_command ()
    #10 0x000000000041b5c6 in read_command ()
    #11 0x000000000041b74e in reader_loop ()
    #12 0x000000000041b2aa in main ()

