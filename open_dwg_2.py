from tkinter import *
from tkinter import messagebox
from subprocess import Popen 
import re,os

#載入config資訊
try:
    with open(f'{os.getcwd()}\\open_dwg_config.txt','r',encoding='utf-8') as fin:
        file_list_path = fin.readlines()[1].strip()
except:
    messagebox.showerror('錯誤','找不到config檔案')
    messagebox.showinfo('訊息',f'請將config檔放在{os.getcwd()}')
    exit()
#產生品號路徑字典

file_list_path = f"{os.getcwd()}\\file_list.txt"

with open(file_list_path,encoding='utf-8') as fin:
    file_list = fin.readlines()
      
    folder = ''
    result = {}

    for s in file_list:
        if s[0] == '@':
            folder = s[1:-1]
    
        elif s[-4:-1].upper() == 'DWG':
            result.setdefault(s[:-1],f'{folder}\\{s[:-1]}')
                
        else:
            pass

#按鈕 -搜尋- 動作
def search_start():
    search = ent_input.get()
    out_path = []
    partRegex = re.compile(search)
    for i in result.keys():
        if partRegex.search(i) != None:
            out_path.append(i)
    out_path = sorted(out_path)
    lab_2.config(text='搜尋到{:5}筆'.format(len(out_path)))
    lb_file.delete(0,END)
    for s in out_path:
        lb_file.insert(END,s)

    
#雙擊 -搜尋列表清單- 動作
def open_dwg(event):
    indexs = lb_file.curselection()
    Popen(['start',lb_file.get(indexs)],shell=True)
    print(result[lb_file.get(indexs)])

root = Tk()

root.title('OpenDwg 2.1')

font_style = '標楷體 16'
lab_1 = Label(root,text ='輸入:',font=font_style)
ent_input = Entry(root,font=font_style)
btn_1 = Button(root,text='搜尋',command=search_start,font=font_style)

lab_2 = Label(root,text ='請輸入搜尋料號',anchor='w',font=font_style,width=30)

lb_file = Listbox(root,selectmode=SINGLE,font='標楷體 12',width=45)
lb_file.bind("<Double-Button-1>",open_dwg)

#表單輸出
lab_1.grid(row=0,column=0,padx=5,pady=5) #輸入 文字方塊
ent_input.grid(row=0,column=1,columnspan=4,padx=5,pady=5)  #輸入方塊
btn_1.grid(row=0,column=5,padx=5,pady=5)  #按鈕 搜尋
lab_2.grid(row=1,column=0,columnspan=6,padx=5,pady=5) #搜尋筆數
lb_file.grid(row=2,column=0,columnspan=6,padx=5,pady=5) #輸出列表
root.mainloop()