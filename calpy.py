import tkinter as tk

disValue = 0
operator = {'+':1, '-':2, '/':3, '*':4, 'C':5, '=':6}
stoValue = 0
opPre = 0

def number_click(val):
    global disValue
    disValue = (disValue * 10) + val
    str_value.set(disValue)

def clear():
    global disValue, operator, stoValue, opPre
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(disValue)

def operator_click(val):
    global disValue, operator, stoValue, opPre
    op = operator[val]
    if op == 5: # C
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(disValue)
    elif op == 6: # =
        if opPre == 1:
            disValue += stoValue
        if opPre == 2:
            disValue -= stoValue
        if opPre == 3:
            disValue /= stoValue
        if opPre == 4:
            disValue *= stoValue

        str_value.set(disValue)
        disValue = 0
        stoValue = 0
        opPre = 0
    else:
        clear()

def button_click(val):
    print(val)
    try:
        val = int(val)
        number_click(val)
    except:
        operator_click(val)

win = tk.Tk()
win.title('claculator')

str_value = tk.StringVar()
str_value.set(str(disValue))
# str_value -> 계산기의 입력칸으로 들어온 것을 문자열로 반환해줌
dis = tk.Entry(win, textvariable=str_value, justify='right', bg='white', fg='red')
# justify -> 문자를 어디에 배치할 것이냐
dis.grid(column=0, row=0, columnspan=4, ipadx=80, ipady=30)
# columspan -> 4칸에 걸쳐 적당히 맞추라는 것
# ipadx -> x길이, ipady -> y길이

calitem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

for i, items in enumerate(calitem):
    for k, item in enumerate(items):
        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'
        bt = tk.Button(win,
            text=item,
            width=10,
            height=5,
            bg = color,
            fg = 'white',
            command = lambda cmd=item: button_click(cmd)
            )
        bt.grid(column=k, row=(i + 1))

# tk.Button(win, text='1', width=10, height=5).grid(column=0, row=1)
# tk.Button(win, text='2', width=10, height=5).grid(column=1, row=1)
# tk.Button(win, text='3', width=10, height=5).grid(column=2, row=1)
# tk.Button(win, text='4', width=10, height=5).grid(column=3, row=1)
#
# tk.Button(win, text='5', width=10, height=5).grid(column=0, row=2)
# tk.Button(win, text='6', width=10, height=5).grid(column=1, row=2)
# tk.Button(win, text='7', width=10, height=5).grid(column=2, row=2)
# tk.Button(win, text='8', width=10, height=5).grid(column=3, row=2)
#
# tk.Button(win, text='9', width=10, height=5).grid(column=0, row=3)
# tk.Button(win, text='0', width=10, height=5).grid(column=1, row=3)
# tk.Button(win, text='+', width=10, height=5).grid(column=2, row=3)
# tk.Button(win, text='-', width=10, height=5).grid(column=3, row=3)
#
# tk.Button(win, text='/', width=10, height=5).grid(column=0, row=4)
# tk.Button(win, text='*', width=10, height=5).grid(column=1, row=4)
# tk.Button(win, text='C', width=10, height=5).grid(column=2, row=4)
# tk.Button(win, text='=', width=10, height=5).grid(column=3, row=4)

win.mainloop()