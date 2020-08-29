from tkinter import *

bclick = True




win = Tk()
win.title("tic ❌ tac O toe")
win.geometry('500x500')

n = 9
btns = []


def ttt(button):
    global bclick
    print(button)
    if button["text"] == "" and bclick == True:
        print("if")
        button.config(text="x", state='disable')
        bclick = False

    elif button["text"] == "" and bclick == False:
        print("else")
        button.config(text="o", state='disable')


        bclick = True


for i in range(9):
    btns.append(Button(font=("bold", 20), bg='white', height=2, width=4))

row = 1
column = 0
index = 1
print(btns)
buttons = StringVar()

for i in btns:
    i.grid(row=row, column=column)
    i.config(command=lambda current_button=i: ttt(current_button))
    column += 1
    if index % 3 == 0:
        row += 1
        column = 0
    index += 1




win.mainloop()
