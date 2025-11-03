from tkinter import *

# Fungsi untuk tombol Hasil Prediksi (selalu menampilkan "Teknologi Informasi")
def hasil_prediksi():
    label_hasil.config(text="Teknologi Informasi")

# Buat jendela utama
root = Tk()
root.title("Prediksi Prodi")
root.geometry("400x500")  # Ukuran jendela, sesuaikan jika perlu

# Label judul
label_judul = Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.grid(row=0, column=0, columnspan=10, pady=50)

# List untuk menyimpan Entry (meskipun tidak digunakan di fungsi, ini untuk struktur)
entries = []

# Loop untuk membuat 10 label dan entry
for i in range(1, 11):
    label = Label(root, text=f"Mata Pelajaran {i}: ")
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Button Hasil Prediksi
button = Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk hasil
label_hasil = Label(root, text="", font=("Arial", 12))
label_hasil.grid(row=12, column=0, columnspan=2, pady=10)

# Jalankan GUI
root.mainloop()
