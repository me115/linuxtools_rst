#! /usr/bin/env python
#coding=utf-8
# markdown文件转换为rst文件
#author: colin 8/14/2014
import os,sys,re,traceback


class Md2rstConvertor:
    
    #change
    def convert(self,filename):
        lines = []
        isCodeLine = False
        datafile = open(filename,"r")
        for line in datafile:
            # 识别代码段
            m = re.match(r'`{3}[ ]*',line)  
            if m is not None:
                if isCodeLine == False:
                    lines.append('::\n\n')
                    isCodeLine = True
                else:
                    isCodeLine = False # code块结束
                    lines.append('\n')
                continue
            
            if isCodeLine == True:
                lines.append('\t' + line.strip() + '\n')
                continue
            else:
                # 识别一级标题
                m = re.match(r'[ ]*#{1}[^#]+',line)  
                if m is not None:
                    lines.append(line.strip('# \r\n') + '\n')
                    lines.append('=' * len(line) + '\n')
                    continue
                
                # 识别二级标题
                m = re.match(r'[ ]*#{2}[^#]+',line)  
                if m is not None:
                    lines.append(line.strip('# \r\n') + '\n')
                    lines.append('-' * len(line) + '\n')
                    continue
                
                # 识别三级标题
                m = re.match(r'[ ]*#{3}[^#]+',line)  
                if m is not None:
                    lines.append(line.strip('# \r\n') + '\n')
                    lines.append('~' * len(line) + '\n')
                    continue
                
                lines.append(line.strip() + '\n')

            
        
        rstFile = '%s.rst' % filename.split('.')[0]
        fw = open(rstFile,'w')
        for str in lines:
            fw.writelines(str )
        fw.close()
        
        

if __name__ == '__main__':

    convertor = Md2rstConvertor()
    try:
        if len(sys.argv) <= 1:
            print "please input file name to convert :('all' for all file in cur dir)"
            exit()
        
        arg = sys.argv[1]
        if arg == 'all':
            # 转换当前文件夹下所有md文件
            for filename in os.listdir('./'):
                if os.path.isfile(filename): # 过滤文件夹
                    fix = filename.split('.')[-1]
                    if  fix.upper() == "MD" :
                        convertor.convert(filename)
        else:
            convertor.convert(arg)
        
    except Exception, ex:

        exc = traceback.format_exc()
        sys.stderr.write("trace =%s \n" % exc)
        sys.stderr.write("ex=%s \n" % str(ex))
