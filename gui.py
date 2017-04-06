
import tkinter as tk
from factorial import factorial
def calc():
    o=factorial(int(num.get()))
    print(o)
    out.delete(0,len(out.get()))
    out.insert(0,str(o))

def test():
    import subprocess
    import threading as th
    def test_t():
        test_text.delete('1.0',tk.END)
        test_text.insert(tk.END,'Выполняется тест программы.....')
        result = subprocess.run(['python', 'test.py','3>&2'], stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        sout=result.stdout.decode('1251')
        serr=result.stderr.decode('1251')
        o=sout+serr
        print(o)
        test_text.delete('1.0',tk.END)
        test_text.insert(tk.END,str(o)+'\r\n')
    t=th.Thread(target=test_t)
    t.start()

if __name__=='__main__':
    root=tk.Tk('GUI')
    num=tk.Entry(root)
    num.grid(row=0,column=0)
    tk.Button(root,text='Найти',command=calc).grid(row=1)
    
    tk.Label(root,text='Ответ:').grid(row=2,column=0)
    out=tk.Entry(root)
    out.grid(row=3)

    test_btn=tk.Button(root,text='Тесты',command=test)
    test_btn.grid(row=4)
    test_text=tk.Text(root)
    test_text.grid(row=5)

    root.mainloop()