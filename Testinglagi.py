import tkinter as tk
from tkinter import messagebox
import random

class PrediksiProdiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Prediksi Prodi Pilihan")
        self.root.geometry("600x800")  # Tinggi diperbesar agar tidak terlalu padat

        # Canvas sebagai background dengan pola bunga lucu
        self.canvas = tk.Canvas(root, width=600, height=800, bg="#FFE4E1", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Tambahkan pola bunga menggunakan emoji di posisi acak
        flowers = ["🌸", "🌼", "🌺", "🌻", "🌷", "💐", "🌹", "🥀"]
        for _ in range(50):  # 50 bunga untuk kesan penuh
            x = random.randint(0, 600)
            y = random.randint(0, 800)
            flower = random.choice(flowers)
            self.canvas.create_text(x, y, text=flower, font=("Arial", 20), fill="#FFB6C1")

        # Judul di tengah atas, posisi lebih atas
        self.title_label = tk.Label(self.canvas, text="🎓✨ Aplikasi Prediksi Prodi Pilihan 🎀🌟", 
                                    font=("Comic Sans MS", 20, "bold"), bg="#FFE4E1", fg="#FF69B4")  # Font sedikit dikecilkan
        self.canvas.create_window(300, 40, window=self.title_label)  # Posisi y lebih atas

        # Frame untuk input nilai, diposisikan di tengah dengan jarak lebih
        input_frame = tk.Frame(self.canvas, bg="#E0FFFF", relief="ridge", bd=3)
        self.canvas.create_window(300, 200, window=input_frame)  # Posisi y dinaikkan

        # Input nilai (10 entries) dengan label lucu
        self.entries = []
        colors = ["#FFB6C1", "#87CEEB", "#DDA0DD", "#F0E68C", "#FFA07A", "#98FB98", "#FFD700", "#FF6347", "#40E0D0", "#EE82EE"]
        for i in range(10):
            label = tk.Label(input_frame, text=f"🌸 Nilai {i+1} 🌸", font=("Comic Sans MS", 12, "bold"), bg=colors[i], fg="white", relief="raised", bd=2)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            entry = tk.Entry(input_frame, font=("Comic Sans MS", 12), width=20, bg="#FFFACD", fg="#FF69B4")
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        # Tombol Prediksi di tengah, dengan jarak lebih
        self.predict_button = tk.Button(self.canvas, text="🔮 Hasil Prediksi 💡✨", command=self.predict, 
                                        font=("Comic Sans MS", 16, "bold"), bg="#FF69B4", fg="#FFFACD", relief="raised", bd=8, activebackground="#FFB6C1")
        self.canvas.create_window(300, 500, window=self.predict_button)  # Posisi y dinaikkan

        # Label hasil di tengah bawah, dengan jarak lebih
        self.result_label = tk.Label(self.canvas, text="", font=("Comic Sans MS", 14, "bold"), bg="#FFE4E1", fg="#87CEEB", wraplength=400)
        self.canvas.create_window(300, 570, window=self.result_label)  # Posisi y dinaikkan

        # Label kredit di tengah bawah, agak gede, dengan jarak lebih
        credit_label = tk.Label(self.canvas, text="Akhmad Rezky Utama 20240140261", font=("Comic Sans MS", 16, "bold"), bg="#FFE4E1", fg="#DDA0DD")
        self.canvas.create_window(300, 700, window=credit_label)  # Posisi y dinaikkan

        credit_label2 = tk.Label(self.canvas, text="Maaf pake AI", font=("Comic Sans MS", 12, "italic"), bg="#FFE4E1", fg="#DDA0DD")
        self.canvas.create_window(300, 730, window=credit_label2)  # Posisi y dinaikkan

    def predict(self):
        # Cek apakah semua entry terisi
        all_filled = all(entry.get().strip() for entry in self.entries)
        
        if not all_filled:
            messagebox.showwarning("Peringatan", "Harap isi semua nilai dulu yaa 🩷💕")
            return
        
        # Jika semua terisi, tampilkan hasil dan ubah tampilan menjadi lebih ceria
        self.result_label.config(text="👉 Selamat! Prodi kamu adalah Teknologi Informasi 💻✨🎉", fg="#4169E1")
        self.canvas.config(bg="#FFB6C1")  # Ubah bg canvas ke pink muda
        self.title_label.config(bg="#FFB6C1")
        self.result_label.config(bg="#FFB6C1")
        self.predict_button.config(bg="#FFD700", fg="#FF69B4")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrediksiProdiApp(root)
    root.mainloop()
