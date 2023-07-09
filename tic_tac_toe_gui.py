import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.current_player = "X"  # Başlangıçta X oyuncusu
        
        self.buttons = []
        '''
        Asagidaki kod ile ayni isi yapiyor
        self.board = [["" for _ in range(3)] for _ in range(3)]  # Oyun tahtası
        '''
        self.board = []  # Boş bir liste oluşturuyoruz
        
        '''
        i veya başka bir anlamlı değişken adı: Bu durumda, i gibi bir değişken adı, döngü değişkeninin değerini temsil eder 
        ve döngüdeki her bir adımda bu değeri kullanabilirsiniz. Bu, döngüdeki değerlerin anlamlı bir şekilde takip edilmesini sağlar 
        ve döngü içindeki işlemler için değişkeni kullanmanıza olanak sağlar. 


        _ (alt çizgi): _ yer tutucusu, döngü değişkeninin değerini kullanmadığınızı veya önemsiz olduğunu belirtmek için kullanılır. 
        Bu, döngüdeki değeri kullanmanız gerekmeyen durumlar için tercih edilebilir. 
        Yer tutucusu olarak kullanıldığında, değişkenin kendisiyle ilgili herhangi bir şey ifade etmez ve sadece döngü adımınızı belirtmek için kullanılır
        '''
        for _ in range(3):  #Burda _ bir placeholde (yer tutucu) değişken yerine kullanılıyor i gibi ama i de gene
            row = [""] * 3  # Her bir satırı boş bir dize ile dolduruyoruz
            self.board.append(row)  # Her bir satırı matrise ekliyoruz


        # Tahta üzerindeki butonları oluştur
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.window, text= "", width=10, height=5, command=lambda r=row, c=col: self.button_click(r, c))
                
                button.grid(row=row, column=col)
                button_row.append(button)

            self.buttons.append(button_row)
                
    def button_click(self, row, col):
        # Butona tıklama işlemi
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            
            # Oyunun durumunu kontrol et
            game_result = self.check_game_result()
            if game_result:
                messagebox.showinfo("Oyun Bitti", f"Kazanan: {game_result}")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Oyun Bitti", "Berabere!")
                self.reset_game()
            else:
                self.switch_players()
    
    def check_game_result(self):
        # Oyunun durumunu kontrol et
        # İlk kontrol: Yatayda aynı sembollerin olup olmadığını kontrol et
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return self.board[row][0]
        
        # İkinci kontrol: Dikeyde aynı sembollerin olup olmadığını kontrol et
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]
        
        # Üçüncü kontrol: Çaprazlarda aynı sembollerin olup olmadığını kontrol et
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        # Tahta dolu mu kontrol et
        for row in self.board:
            if "" in row:
                return False
        return True
    
    def switch_players(self):
        # Oyuncu değiştir
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
    
    def reset_game(self):
        # Oyunu sıfırla
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.configure(text="")
        
    
    
    
    
    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.start()





'''
from tkinter import *

tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Label")
tk.geometry("400x300")

Label(tk,text="Verdana",font="Verdana 12", bg="red", fg="white").pack()
Label(tk,text="Verdana Bold",font="Verdana 12 bold underline").pack()
Label(tk,text="Verdana italic",font="Verdana 12 italic").pack()
Label(tk,text="Verdana roman",font="Verdana 12 roman").pack()

Label(tk,text="Helvetica",font="Helvetica 12", bg="green", fg="yellow").pack()
Label(tk,text="Helvetica bold",font="Helvetica 12 bold").pack()
Label(tk,text="Helvetica italic",font="Helvetica 12 italic").pack()
Label(tk,text="Helvetica roman",font="Helvetica 12 roman").pack()

Label(tk,text="Times",font="Times 12", bg="black", fg="white").pack()
Label(tk,text="Times Bold",font="Times 12 bold").pack()
Label(tk,text="Times italic",font="Times 12 italic").pack()
Label(tk,text="Times roman",font="Times 12 roman").pack()

tk.mainloop()



def buton():
    lbl["text"] = "1. Butona Tıklandı"
def buton2():
    lbl["text"] = "2. Butona tıklandı"

btn = Button(tk,
            text="Buton",
            padx="20",pady="5",
            command=buton)
btn.pack()

btn2 = Button(tk,
            text = "Buton 2", font="Times 12 bold",
            padx="25", pady="10", 
            bg="red", fg="white", cursor="hand2",
            activeforeground="green", activebackground="black",
            command=buton2)
btn2.pack()

lbl = Label(tk)
lbl.pack()

tk.mainloop()

from tkinter import *
from tkinter import messagebox


# Tk sınıfını 'window'a atadık.
window = Tk()

# Pencere Başlığı
window.title("Kullanıcı Giriş Ekranı")

# Pencereye ikon ekleme


window.geometry("390x220")

# Pencerenin yeniden boyutlandırılmasını engelledik
window.resizable(width=False, height=False)





# Hata mesajımızı bu Label'e yazdıracaz
L3 = Label(window)
L3.place(x=148,y=200)

def giris():
    
    # E1 ve E2 adlı Entry'e girilen değeri, get() fonksiyonuyla çekip sorguluyoruz. 
    if (E1.get() == str("admin")) and (E2.get() == str("1234")):
        L3['text'] = ("Giriş Başarılı...")
        messagebox.showinfo("Başlık", "Giriş Başarılı")
        print("başarılı")
    else:
        L3['text'] = ("Hatalı Giriş !")
        messagebox.showerror("Hata Başlık", "Hatalı Giriş")

L1 = Label(window, text="Kullanıcı Adı")
L1.place(x=75, y=15)

E1 = Entry(window, width=25)
E1.place(x=77,y=45)

L2 = Label(window, text="Şifre")
L2.place(x=75, y=80)

E2 = Entry(window, textvariable=StringVar(),show='*', width=25)
E2.place(x=77, y=110)

bt = Button(window, text="Giriş Yap", padx="20",pady="5", command=giris)
bt.place(x=75,y=150)

window.mainloop()




'''