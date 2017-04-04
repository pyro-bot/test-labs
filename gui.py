
import tkinter as tk
from factorial import factorial
def calc():
    o=factorial(int(num.get()))
    print(o)
    out.delete(0)
    out.insert(0,str(o))

def test():
    import subprocess
    import threading as th
    def test_t():
        result = subprocess.run(['cmd.exe','/c', 'python test.py'], stdout=subprocess.PIPE)
        o=result.stdout
        print(o)
        test_text.delete('1.0')
        test_text.insert('1.0',str(o))
    t=th.Thread(target=test_t)
    t.start()

if __name__=='__main__':
    root=tk.Tk('GUI')
    num=tk.Entry(root)
    num.grid(row=0,column=0,columnspan=3,rowspan=1)
    tk.Button(root,text='Найти',command=calc).grid(row=2,column=0,columnspan=1,rowspan=1)
    
    tk.Label(root,text='Ответ:').grid(row=3,column=0,rowspan=1,columnspan=2)
    out=tk.Entry(root)
    out.grid(row=3,column=3,rowspan=1,columnspan=4)

    test_btn=tk.Button(root,text='Тесты',command=test)
    test_btn.grid(row=4,column=2)
    test_text=tk.Text(root)
    test_text.grid(row=5,column=0,rowspan=4,columnspan=4)

    root.mainloop()