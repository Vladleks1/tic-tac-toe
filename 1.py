from tkinter import *
from tkinter import messagebox
import random
class Tic_toe:
    def __init__(self):
        #Поле
        self.root=Tk()
        self.root.title('игра в крестики нолики')
        self.root.geometry('1280x720')
        self.root.protocol('WM_DELETE_WINDOW', self.on_delet)
        #Игровые переменные
        self.pole1=[]
        self.count_x_o=1
        self.O_X=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.but_tab=None
        self.characteristic="None"
        self.win_kode = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        #запуск меню
        self.show_main_menu()
    def clear_window(self):#Удаление предыдущих виджетов
        for widget in self.root.winfo_children():
            widget.destroy()
    def on_delet(self):#Закрытие окна полностью
        if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры"):
            self.root.destroy()
    def show_main_menu(self):#Начальное меню
        self.clear_window()
        but1 = Button(self.root, width=15, height=5, text="играть", command=self.start_game_with_friend)
        but1.place(x=560, y=300)
        but2 = Button(self.root, width=15, height=5, text="уровни", command=self.show_levels_menu)
        but2.place(x=560, y=200)
    def show_levels_menu(self):#выбор уровней сложностей
        self.clear_window()
        but3 = Button(self.root, width=15, height=5, text="уровень 1", command=self.start_bot_game_easy)
        but3.place(x=400, y=300)
        but4 = Button(self.root, width=15, height=5, text="уровень 2", command=self.start_bot_game_medium)
        but4.place(x=550, y=300)
        but5 = Button(self.root, width=15, height=5, text="уровень 3", command=self.start_bot_game_hard)
        but5.place(x=700, y=300)
    def draw_navigation_top(self):#верхнии кнопки
        but6 = Button(self.root, text="играть с другом", command=self.start_game_with_friend)
        but6.place(x=637, y=0)
        but7 = Button(self.root, text="назад", command=self.show_levels_menu)
        but7.place(x=777, y=0)
    def start_game_with_friend(self):  # игра с другом
        self.clear_window()
        self.characteristic = "None"
        self.init_game_board()
        but8 = Button(self.root, text="уровни", command=self.show_levels_menu)
        but8.place(x=637, y=0)
    def start_bot_game_easy(self):#игра против бота легкого
        self.clear_window()
        self.draw_navigation_top()
        self.characteristic = "Easy"
        self.init_game_board()
    def start_bot_game_medium(self):#игра против бота среднего
        self.clear_window()
        self.draw_navigation_top()
        self.characteristic = "Medium"
        self.init_game_board()
    def start_bot_game_hard(self):#игра против бота сложного
        self.clear_window()
        self.draw_navigation_top()
        self.characteristic="Hard"
        self.init_game_board()
    def init_game_board(self):#игровое поле
        self.count_x_o = 1
        self.O_X = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.pole1 = [Button(self.root, width=15, height=5, command=lambda x=h: self.make_move(x)) for h in range(9)]
        positions = [(400, 200), (550, 200), (700, 200),(400, 300), (550, 300), (700, 300),(400, 400), (550, 400), (700, 400)]
        for idx,(x,y) in enumerate(positions):
            self.pole1[idx].place(x=x,y=y)
        # Информационное табло
        self.but_tab = Button(self.root, width=54, height=5, state="disabled")
        self.but_tab.place(x=400, y=35)
        # сброс игры
        but_reset = Button(self.root, text="новая игра", command=self.reset_game)
        but_reset.place(x=533, y=0)
    def make_move(self, idx):#механика нажатия клавишь
        if self.characteristic=="None":
            if self.count_x_o % 2 != 0:
                self.x(idx)
            else:
                self.o(idx)
        elif self.characteristic=="Hard":#Кривой надо исправить
            self.x(idx)
            if self.O_X.count("X")!=self.O_X.count("O"):
                self.o(self.best_move())
        elif self.characteristic=="Medium":
            self.x(idx)
            if random.random()<=0.6:
                self.o(self.best_move())
            else:
                self.o(random.choice(self.is_cell_free()))
        elif self.characteristic=="Easy":
            self.x(idx)
            if random.random() <= 0.3:
                self.o(self.best_move())
            else:
                self.o(random.choice(self.is_cell_free()))
        if self.check_winner() != None:
            self.but_tab.config(text=self.check_winner())
    def is_cell_free(self):#ищет свободные клетки
        if self.check_winner() != None:
            self.but_tab.config(text=self.check_winner())
        return [i for i in self.O_X if i != "X" and i != "O"]
    def best_move(self):#находин наилучший ход
        if self.check_winner() != None:
            self.but_tab.config(text=self.check_winner())
        best_socer = -float("inf")
        move = None
        for j in range(0,9):
            count = 0
            for i in self.win_kode:
                if j!=self.O_X[j]:
                    continue
                if j in i:
                    count += 1
            if count > best_socer:
                best_socer = count
                move = j
        for j in self.win_kode:#выйгрыш или поражение
            count_lose=0
            count_win=0
            free_cell=[]
            blocking=[]
            for i in j:
                if self.O_X[i]=="X":
                    count_lose+=1
                elif self.O_X[i]=="O":
                    count_win+=1
                else:
                    free_cell.append(i)
                if (count_win==2 and len(free_cell)==1):
                    move=free_cell[0]
                    return move
                elif (count_lose==2 and len(free_cell)==1):
                    move=free_cell[0]
                    blocking.append(move)
        if len(blocking)>0:
            return blocking[0]
        return move
    def x(self,idx):
        if  self.O_X[idx]!="X" and self.O_X[idx]!="O":
            self.pole1[idx].config(text="X", state="disabled")
            self.count_x_o+=1
            self.O_X[idx] = "X"
    def o(self,idx):
        if self.check_winner() != None:
            self.but_tab.config(text=self.check_winner())
            idx=None
        if self.O_X[idx] != "X" and self.O_X[idx] != "O":
            self.pole1[idx].config(text="O", state="disabled")
            self.count_x_o+=1
            self.O_X[idx] = "O"
    def check_winner(self):#проверка выйграша
        for combo in self.win_kode:
            if self.O_X[combo[0]] == self.O_X[combo[1]] == self.O_X[combo[2]]:
                for idx in range(9):
                    self.pole1[idx].config(state="disabled")
                return "Победил:", self.O_X[combo[0]]
        if self.count_x_o == 10:
            return "ничья"
    def reset_game(self):#сброс игры
        for idx in range(0, 9):
            self.O_X[idx] = idx
            self.pole1[idx].config(text="", state="normal")
        self.but_tab.config(text='')
        self.count_x_o=1
    def run(self):#запуск игры
        self.root.mainloop()
if __name__=="__main__":#запуск кода
    app=Tic_toe()
    app.run()
