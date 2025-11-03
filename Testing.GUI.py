import tkinter as tk  # Import library Tkinter untuk membuat GUI

# Buat window utama aplikasi
root = tk.Tk()  # Membuat objek window utama
root.title("Aplikasi Prediksi Prodi")  # Memberi judul pada window

# Atur ukuran window dan posisikan di tengah layar
root.geometry("400x400")  # Set ukuran window (lebar x tinggi)
root.update_idletasks()  # Update window agar ukuran terdeteksi
screen_width = root.winfo_screenwidth()  # Dapatkan lebar layar
screen_height = root.winfo_screenheight()  # Dapatkan tinggi layar
x = (screen_width - 400) // 2  # Hitung posisi x untuk center
y = (screen_height - 400) // 2  # Hitung posisi y untuk center
root.geometry(f"400x400+{x}+{y}")  # Set posisi window di tengah

# Buat label judul aplikasi
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14))  # Buat label dengan teks dan font
title_label.grid(row=0, column=0, columnspan=2, pady=10)  # Tempatkan di baris 0, kolom 0-1, dengan padding vertikal

# Buat list untuk menyimpan 10 entry (input fields)
entries = []  # List kosong untuk menyimpan objek Entry
for i in range(10):  # Loop dari 0 sampai 9 (untuk 10 input)
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")  # Buat label untuk setiap input
    label.grid(row=i+1, column=0, sticky="e", padx=5)  # Tempatkan label di kolom 0, rata kanan
    entry = tk.Entry(root)  # Buat kotak input (Entry)
    entry.grid(row=i+1, column=1, padx=5, pady=2)  # Tempatkan entry di kolom 1
    entries.append(entry)  # Tambahkan entry ke list untuk akses nanti

# Buat label untuk output hasil prediksi (awalnya kosong)
result_label = tk.Label(root, text="", font=("Arial", 12))  # Buat label kosong untuk hasil
result_label.grid(row=12, column=0, columnspan=2, pady=10)  # Tempatkan di bawah input

# Fungsi yang dipanggil saat button diklik
def predict_prodi():  # Definisi fungsi prediksi
    all_filled = True  # Asumsikan semua input terisi
    for entry in entries:  # Loop untuk cek setiap entry
        if not entry.get().strip():  # Jika entry kosong (setelah strip spasi)
            all_filled = False  # Set flag ke False
            break  # Keluar dari loop
    if all_filled:  # Jika semua terisi
        result_label.config(text="Teknologi Informasi")  # Set teks hasil ke "Teknologi Informasi"
    else:  # Jika ada yang kosong
        result_label.config(text="Harap isi semua nilai!")  # Set pesan error

# Buat button "Hasil Prediksi"
predict_button = tk.Button(root, text="Hasil Prediksi", command=predict_prodi)  # Buat button dengan teks dan fungsi
predict_button.grid(row=11, column=0, columnspan=2, pady=10)  # Tempatkan di bawah input, kolom 0-1

# Jalankan loop utama GUI
root.mainloop()  # Jalankan aplikasi agar window tetap terbuka dan responsif
