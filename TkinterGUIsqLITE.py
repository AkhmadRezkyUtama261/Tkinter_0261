import tkinter as tk
import tkinter.messagebox as msg
import sqlite3
import random
top = tk.Tk()
top.title("My Tkinter Window")
top.geometry("400x300")
top.configure(bg="pink")
E1= tk.Entry(top, bd=5)
E1.pack()
E2=tk.Entry(top, bd=5)
E2.pack()
def simpanData():
    nama = E1.get()
    umur = E2.get()
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,"\
    "name TEXT, age INTEGER)")
    cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (nama, umur))
    con.commit()
    con.close()
    msg.showinfo("Sukses", "Data berhasil disimpan!")
    flowers = ["🌸", "🌼", "🌺", "🌻", "🌷", "💐", "🌹", "🥀"]
    for _ in range(50):  # 50 bunga untuk kesan penuh
        x = random.randint(0, 600)
        y = random.randint(0, 800)
        flower = random.choice(flowers)
        self.canvas.create_text(x, y, text=flower, font=("Arial", 20), fill="#FFB6C1")
tombolSimpan = tk.Button(top, text="Simpan Data", command=simpanData)
tombolSimpan.pack()
top.mainloop()
