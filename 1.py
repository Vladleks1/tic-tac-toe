from tkinter import *
from tkinter import messagebox
class Tic_toe:
    def __init__(self):
        #Поле
        self.root=Tk()
        self.root.title('игра в крестики нолики')
        self.root.geometry('1280x720')
        self.root.protocol('WM_DELETE_WINDOW', self.on_delet)
        #Игровые переменные
        self.pole1=[]
        self.X_O=[1]
        self.O_X=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.but111=None
        self.but222 =None
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
        but3 = Button(self.root, width=15, height=5, text="уровень 1", command=self.start_bot_game)
        but3.place(x=400, y=300)
        but4 = Button(self.root, width=15, height=5, text="уровень 2", command=self.start_bot_game)
        but4.place(x=550, y=300)
        but5 = Button(self.root, width=15, height=5, text="уровень 3", command=self.start_bot_game)
        but5.place(x=700, y=300)
    def draw_navigation_top(self):#верхнии кнопки
        du = Button(self.root, text="играть с другом", command=self.start_game_with_friend)
        du.place(x=637, y=0)
        du1 = Button(self.root, text="назад", command=self.show_levels_menu)
        du1.place(x=777, y=0)
    def start_game_with_friend(self):  # игра с другом
        self.clear_window()
        self.init_game_board()
        du = Button(self.root, text="уровни", command=self.show_levels_menu)
        du.place(x=637, y=0)
    def start_bot_game(self):#игра против нейросети
        self.clear_window()
        self.draw_navigation_top()
        self.init_game_board()
    def init_game_board(self):#игровое поле
        self.X_O = [1]
        self.O_X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.pole1 = [Button(self.root, width=15, height=5, command=lambda x=h: self.make_move(x)) for h in range(9)]
        positions = [(400, 300), (550, 300), (700, 300),(400, 400), (550, 400), (700, 400),(400, 200), (550, 200), (700, 200)]
        for idx,(x,y) in enumerate(positions):
            self.pole1[idx].place(x=x,y=y)
        # Информационное табло
        self.but111 = Button(self.root, width=54, height=5, state="disabled")
        self.but111.place(x=400, y=30)
        # сброс игры
        self.but222 = Button(self.root, text="новая игра", command=self.reset_game)
        self.but222.place(x=533, y=0)
    def make_move(self, idx):#механика нажатия клавишь
        while True:
            if len(self.X_O) % 2 != 0:
                self.pole1[idx].config(text="X", state="disabled")
                self.X_O.append(2)
                self.O_X[idx] = "X"
                break
            else:
                self.pole1[idx].config(text="O", state="disabled")
                self.X_O.append(2)
                self.O_X[idx] = "O"
                break
        if self.check_winner() != None:
            self.but111.config(text=self.check_winner())
    def check_winner(self):#проверка выйграша
        win_kode = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (1, 3, 8), (1, 5, 6))
        for combo in win_kode:
            if self.O_X[combo[0]] == self.O_X[combo[1]] == self.O_X[combo[2]]:
                for h in range(9):
                    self.pole1[h].config(state="disabled")
                return "Победил:", self.O_X[combo[0]]
        if len(self.X_O) == 10:
            return "ничья"
    def reset_game(self):#сброс игры
        for i in range(1, 10):
            self.O_X[i - 1] = i
            self.pole1[i - 1].config(text="", state="normal")
        self.but111.config(text='')
        for i in range(len(self.X_O) - 1):
            self.X_O.remove(2)
    def run(self):#запуск игры
        self.root.mainloop()
if __name__=="__main__":#запуск кода
    app=Tic_toe()
    app.run()
