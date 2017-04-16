
import tkinter as tk
import calc as c


def calc():
    o = c.factorial(int(fact.get()))
    o = c.div(o, int(div.get()))
    o = c.minus(o, int(minus.get()))
    print(o)
    out.delete(0, len(out.get()))
    out.insert(0, str(o))


def test():
    import subprocess
    import threading as th

    def test_t():
        test_text.delete('1.0', tk.END)
        test_text.insert(tk.END, 'Выполняется тест программы.....')
        result = subprocess.run(['python', 'test.py', '3>&2'],
                                stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        sout = result.stdout.decode('1251')
        serr = result.stderr.decode('1251')
        o = sout + serr
        print(o)
        test_text.delete('1.0', tk.END)
        test_text.insert(tk.END, str(o) + '\r\n')
    t = th.Thread(target=test_t)
    t.start()


if __name__ == '__main__':
    root = tk.Tk('GUI')

    tk.Label(root, text='Факториал:').grid(row=0, column=0)
    fact = tk.Entry(root)
    fact.grid(row=0, column=1)

    tk.Label(root, text='Деление:').grid(row=0, column=2)
    div = tk.Entry(root)
    div.grid(row=0, column=3)

    tk.Label(root, text='Минус:').grid(row=0, column=4)
    minus = tk.Entry(root)
    minus.grid(row=0, column=5)

    tk.Button(root, text='Найти', command=calc).grid(row=1)

    tk.Label(root, text='Ответ:').grid(row=2, column=0)
    out = tk.Entry(root)
    out.grid(row=3)

    test_btn = tk.Button(root, text='Тесты', command=test)
    test_btn.grid(row=4)
    test_text = tk.Text(root)
    test_text.grid(row=5,columnspan=6)

    root.mainloop()
