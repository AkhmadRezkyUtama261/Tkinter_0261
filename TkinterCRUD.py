import tkinter as tk
from tkinter import messagebox
import random
import sqlite3


class NilaiSiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Nilai siswa")
        self.root.geometry("600x800")

        self.canvas = tk.Canvas(root, width=600, height=800, bg="#FFFFFF", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.title_label = tk.Label(self.canvas, text="Nilai Siswa", 
                                    font=("Comic Sans MS", 20, "bold"), bg="#FFFFFF", fg="#000000")
        self.canvas.create_window(300, 40, window=self.title_label)

        input_frame = tk.Frame(self.canvas, bg="#FFFFFF", relief="ridge", bd=3)
        self.canvas.create_window(300, 200, window=input_frame)

        self.entries = []
        nama =  str(input("Masukkan Nama anda"))
        colors = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
        entry = tk.Entry(input_frame, font=("Comic Sans MS", 12), width=20, bg="#FFFFFF", fg="#020202")
        entry.grid(row=i, column=1, padx=10, pady=5)
        self.entries.append(entry)

        self.entries = []
        Inggris =  int(input("Masukkan Nama anda"))
        colors = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
        entry = tk.Entry(input_frame, font=("Comic Sans MS", 12), width=20, bg="#FFFFFF", fg="#020202")
        entry.grid(row=i, column=1, padx=10, pady=5)
        self.entries.append(entry)

        self.entries = []
        fisika =  int(input("Masukkan Nama anda"))
        colors = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
        entry = tk.Entry(input_frame, font=("Comic Sans MS", 12), width=20, bg="#FFFFFF", fg="#020202")
        entry.grid(row=i, column=1, padx=10, pady=5)
        self.entries.append(entry)

        self.entries = []
        Biologi =  int(input("Masukkan Nama anda"))
        colors = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
        entry = tk.Entry(input_frame, font=("Comic Sans MS", 12), width=20, bg="#FFFFFF", fg="#020202")
        entry.grid(row=i, column=1, padx=10, pady=5)
        self.entries.append(entry)



        self.predict_button = tk.Button(self.canvas, text="Submit", command=self.predict, 
                                        font=("Comic Sans MS", 16, "bold"), bg="#FFFFFF", fg="#000000", relief="raised", bd=8, activebackground="#FFFFFF")
        self.canvas.create_window(300, 500, window=self.predict_button)

        # Label hasil di tengah bawah, dengan jarak lebih
        self.result_label = tk.Label(self.canvas, text="", font=("Comic Sans MS", 14, "bold"), bg="#FFFFFF", fg="#000000", wraplength=400)
        self.canvas.create_window(300, 570, window=self.result_label)  # Posisi y dinaikkan

        # Label kredit di tengah bawah, agak gede, dengan jarak lebih
        credit_label = tk.Label(self.canvas, text="Akhmad Rezky Utama 20240140261", font=("Comic Sans MS", 16, "bold"), bg="#FFFFFF", fg="#000000")
        self.canvas.create_window(300, 700, window=credit_label)  # Posisi y dinaikkan

    def predict(self):
        # Cek apakah semua entry terisi
        all_filled = all(entry.get().strip() for entry in self.entries)
        
        if not all_filled:
            messagebox.showwarning("Peringatan", "Harap isi semua nilai dulu yaa")
            return
        
        # Jika semua terisi, tampilkan hasil dan ubah tampilan menjadi lebih ceria
        self.result_label.config(text="Prediksi kamu adalah", fg="#000000")
        self.canvas.config(bg="#FFFFFF") 
        self.title_label.config(bg="#FFFFFF")
        self.result_label.config(bg="#FFFFFF")
        self.predict_button.config(bg="#FFFFFF", fg="#000000")

if __name__ == "__main__":
    root = tk.Tk()
    app = NilaiSiswa(root)
    root.mainloop()
