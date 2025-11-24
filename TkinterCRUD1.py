import tkinter as tk
import tkinter.messagebox as msg
import sqlite3

top = tk.Tk()
top.title("Nilai_Siswa")
top.geometry("400x300")
top.configure(bg="pink")
E1= tk.Entry(top, bd=5)
E1.pack()
E2=tk.Entry(top, bd=5)
E2.pack()
E3=tk.Entry(top, bd=5)
E3.pack()
E4=tk.Entry(top, bd=5)
E4.pack()
def prediksikan():
    nama = E1.get()
    label = label(top, str(input("Masukkan Nama anda")))
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

    biologi = E2.get()
    label = label(top, int(input("Masukkan Nilai Biologi anda")))
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

    fisika = E3.get()
    label = label(top, int(input("Masukkan Nilai Fisika anda")))
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

    inggris = E4.get()
    label = label(top, int(input("Masukkan Nilai Inggrs anda")))
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

    hasil1 = biologi
    hasil2= inggris
    hasil3= fisika

    if hasil1 > 75:
        print ("Kedokteran")

    elif hasil2 > 75:
        print ("Bahasa")

    elif hasil3 > 75:
        print ("Teknik")
 
    else:
        print ("Isian nya membingungkan")

    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,"\
    "name TEXT, age INTEGER)")
    cur.execute("INSERT INTO students (Nama, Biologi, Fisika, Inggris) VALUES (?, ?)", (nama, biologi, fisika, inggris))
    con.commit()
    con.close()
    msg.showinfo("Sukses", "Data berhasil disimpan!")
tombolSimpan = tk.Button(top, text="Prediksi", command=prediksikan)
tombolSimpan.pack()
top.mainloop()
