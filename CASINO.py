import tkinter as tk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CasinoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Казино Взлет")
        
        self.balance = 1000  # начальный баланс
        self.bet = 0
        
        self.label_balance = tk.Label(root, text=f"Баланс: {self.balance}")
        self.label_balance.pack()
        
        self.entry_bet = tk.Entry(root)
        self.entry_bet.pack()
        self.entry_bet.insert(0, "Введите ставку")
        
        self.button_fly = tk.Button(root, text="Взлететь", command=self.fly)
        self.button_fly.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.height_label = tk.Label(root, text="Высота: 0")
        self.height_label.pack()
        
        self.percent_label = tk.Label(root, text="Вероятность падения: 50%")
        self.percent_label.pack()

        self.fig, self.ax = plt.subplots()
        self.height_data = []
        self.time_data = []

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()
        
    def fly(self):
        try:
            self.bet = int(self.entry_bet.get())
            if self.bet > self.balance or self.bet <= 0:
                raise ValueError("Некорректная ставка")
            
            self.balance -= self.bet
            self.label_balance.config(text=f"Баланс: {self.balance}")
            self.result_label.config(text="Взлетаем...")
            
            height = random.randint(1, 10)  
            fall_probability = random.randint(1, 100) 
           
            self.height_label.config(text=f"Высота: {height}")
            self.percent_label.config(text=f"Вероятность падения: {fall_probability}%")
            
            current_time = len(self.height_data) + 1
            self.height_data.append(height)
            self.time_data.append(current_time)
            
            self.ax.clear()
            self.ax.plot(self.time_data, self.height_data, marker='o')
            self.ax.set_title("Высота взлета")
            self.ax.set_xlabel("Время (секунды)")
            self.ax.set_ylabel("Высота")
            self.ax.set_ylim(0, 10) 
            
            self.canvas.draw()
            
            time.sleep(1)  
            
            if fall_probability < 50:  
                self.result_label.config(text="Упали! Вы проиграли ставку.")
            else:
                winnings = self.bet * (height + 1)
                self.balance += winnings
                self.label_balance.config(text=f"Баланс: {self.balance}")
                self.result_label.config(text=f"Вы взлетели на {height} и выиграли {winnings}!")
                
        except ValueError as e:
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    game = CasinoGame(root)
    root.mainloop()