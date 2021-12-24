import re
import time

# 以下两行代码是吧启动路径改为当前文件夹，加上后在 vscode 里面可以使用相对路径了
# import os, sys
# os.chdir(sys.path[0])

start = time.time()

with open("comodo.txt", mode="r", encoding="UTF-8") as f1:
    txt = f1.read()
f1.close()
obj = re.compile(r'<Pattern Type="1" Name="(?P<site>.*?)" />', re.S)
res = obj.finditer(txt)

with open("comodo_res.txt", mode="w", encoding="UTF-8") as f2:
    for r in res:
        f2.writelines(r.group("site") + '\n')
f2.close()

end = time.time()
print(end-start)
