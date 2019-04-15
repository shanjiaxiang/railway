1.打包方法： pyinstaller -F main.py 生成main.spec后修改 datas=[('data.txt','.'),('dest.txt','.')],
2.去除命令台，修改main.spec最下面console 为false