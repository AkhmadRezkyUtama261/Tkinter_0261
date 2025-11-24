import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk membuat koneksi ke database SQLite dan membuat tabel jika belum ada
def create_table():
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai tertinggi
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        # Jika ada nilai yang sama, pilih berdasarkan prioritas: Biologi > Fisika > Inggris
        if biologi >= fisika and biologi >= inggris:
            return "Kedokteran"
        elif fisika >= inggris:
            return "Teknik"
        else:
            return "Bahasa"

# Fungsi untuk menyimpan data ke database
def submit_nilai():
    nama = entry_nama.get()
    try:
        biologi = int(entry_biologi.get())
        fisika = int(entry_fisika.get())
        inggris = int(entry_inggris.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return
    
    # Tentukan prediksi
    prediksi = prediksi_fakultas(biologi, fisika, inggris)
    
    # Simpan ke database
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi))
    conn.commit()
    conn.close()
    
    # Tampilkan pesan sukses
    messagebox.showinfo("Sukses", f"Data siswa {nama} berhasil disimpan. Prediksi Fakultas: {prediksi}")
    
    # Clear entries
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Buat tabel saat aplikasi dimulai
create_table()

# Buat GUI dengan Tkinter
root = tk.Tk()
root.title("Prediksi Fakultas Siswa")

# Label dan Entry untuk Nama Siswa
tk.Label(root, text="Nama Siswa:").grid(row=0, column=0, padx=10, pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=5)

# Label dan Entry untuk Nilai Biologi
tk.Label(root, text="Nilai Biologi:").grid(row=1, column=0, padx=10, pady=5)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1, padx=10, pady=5)

# Label dan Entry untuk Nilai Fisika
tk.Label(root, text="Nilai Fisika:").grid(row=2, column=0, padx=10, pady=5)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1, padx=10, pady=5)

# Label dan Entry untuk Nilai Inggris
tk.Label(root, text="Nilai Inggris:").grid(row=3, column=0, padx=10, pady=5)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1, padx=10, pady=5)

# Button Submit
tk.Button(root, text="Submit Nilai", command=submit_nilai).grid(row=4, column=0, columnspan=2, pady=10)

# Jalankan aplikasi
root.mainloop()
