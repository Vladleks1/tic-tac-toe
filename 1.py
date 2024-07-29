from tkinter import *

from tkinter import messagebox

def on_delet():
    if messagebox.askokcancel("Выход из игры","Хотите выйти из игры"):
        root.destroy()
def pole(roott):
    global pole1
    global X_O
    global O_X
    global but111
    global but222
    X_O=[1]
    O_X = [1,2,3,4,5,6,7,8,9]
    pole1=[Button(roott, width=15, height=5,command=lambda x=h:ugrok_X_0(x)) for h in range(9)]
    pole1[0].place(x=400, y=300)
    pole1[1].place(x=550, y=300)
    pole1[2].place(x=700, y=300)
    pole1[3].place(x=400, y=400)
    pole1[4].place(x=550, y=400)
    pole1[5].place(x=700, y=400)
    pole1[6].place(x=400, y=200)
    pole1[7].place(x=550, y=200)
    pole1[8].place(x=700, y=200)
    but111=Button(roott,width=54,height=5,state="disabled")
    but111.place(x=400,y=30)
    but222=Button(roott,text="новая игра",command=reset)
    but222.place(x=533,y=0)
def ugrok_X_0(b):
    while True:
        if len(X_O) % 2 != 0:
            pole1[b].config(text="X", state="disabled")
            X_O.append(2)
            O_X[b] = "X"
            break
        else:
            pole1[b].config(text="O",state="disabled")
            X_O.append(2)
            O_X[b]="O"
            break
    if win()!=None:
        but111.config(text=win())
def win():
    win_kode = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (1, 3, 8), (1, 5, 6))
    for i in win_kode:
        if O_X[i[0]] == O_X[i[1]] == O_X[i[2]]:
            for h in range(9):
                pole1[h].config(state="disabled")
            return "Победил:",O_X[i[0]]
    if len(X_O) == 10:
        return "ничья"




def start_but1(root90):#кнопка для игры с другом
    root90.destroy()
    root1 =Tk()
    root1.geometry('1280x720')
    pole(root1)
    du = Button(root1, text="уровни", command=lambda x=root1:start_but2(x))
    du.place(x=637,y=0)
def start_but2(root91):#кнопка для игры с нейросетью
    root91.destroy()
    root2 =Tk()
    root2.geometry('1280x720')
    but3=Button(root2,width=15,height=5,text="уровень 1",command=lambda x=root2:start_but3(x))
    but3.place(x=400,y=300)
    but4 = Button(root2, width=15, height=5, text="уровень 2",command=lambda x=root2:start_but4(x))
    but4.place(x=550, y=300)
    but5 = Button(root2, width=15, height=5, text="уровень 3",command=lambda x=root2:start_but5(x))
    but5.place(x=700, y=300)
def start_but3(root92):#кнопка для игры с нейросетью
    root92.destroy()
    root3 =Tk()
    root3.geometry('1280x720')
    start_3_5(root3)
    pole(root3)
def start_but4(root93):#кнопка для игры с нейросетью
    root93.destroy()
    root4 =Tk()
    root4.geometry('1280x720')
    start_3_5(root4)
    pole(root4)
def start_but5(root94):#кнопка для игры с нейросетью
    root94.destroy()
    root5 =Tk()
    root5.geometry('1280x720')
    start_3_5(root5)
    pole(root5)
def start_3_5(roottt):
    du = Button(roottt, text="играть с другом", command=lambda x=roottt:start_but1(x))
    du.place(x=637,y=0)
    du1=Button(roottt,text="назад",command=lambda x=roottt:start_but2(x))
    du1.place(x=777,y=0)
def reset():
    for i in range(1,10):
        O_X[i-1]=i
        pole1[i-1].config(text="",state="normal")
    but111.config(text='')
    for i in range(len(X_O)-1):
        X_O.remove(2)

root = Tk()
root.protocol('WM_DELETE_WINDOW', on_delet)
root.title('игра в крестики нолики')
root.geometry('1280x720')
but1 = Button(root, width=15, height=5, text="играть", command=lambda x=root:start_but1(x))
but1.place(x=560, y=300)
but2 = Button(root, width=15, height=5, text="уровни", command=lambda x=root:start_but2(x))
but2.place(x=560, y=200)
root.mainloop()