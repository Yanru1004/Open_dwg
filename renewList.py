import os
path = input("請填入路徑")
out_path = input("請填入輸出檔路徑")
a=os.walk(path)

with open(f'{out_path}\\file_list.txt','w',encoding='utf-8') as fin:
    for s in list(a):
        print(f'@{s[0]}')
        fin.write(f'@{s[0]}\n')
        for i in s[2]:
            print(i)
            fin.write(f'{i}\n')