# 7. Contoh Tipe Data Utama

print("--- Tipe Data Utama ---")

# a. String (str)
# Untuk menyimpan teks. Didefinisikan dengan tanda kutip tunggal atau ganda.
nama_kota = "Jakarta"
kalimat = 'Ini adalah sebuah kalimat.'
print(f"Tipe data String: {nama_kota} (Tipe: {type(nama_kota)})")

# b. Numerik (int, float)
# int untuk bilangan bulat, float untuk bilangan desimal.
umur = 25  # Integer
tinggi_badan = 175.5  # Float
print(f"Tipe data Integer: {umur} (Tipe: {type(umur)})")
print(f"Tipe data Float: {tinggi_badan} (Tipe: {type(tinggi_badan)})")

# c. List
# Kumpulan data yang terurut dan bisa diubah (mutable).
# Bisa berisi berbagai tipe data.
hobi = ["membaca", "bersepeda", "koding"]
data_campuran = [10, "apel", True, 3.14]
print(f"Tipe data List: {hobi} (Tipe: {type(hobi)})")
# Mengakses dan mengubah list
hobi.append("berenang") # Menambah item
print(f"List setelah ditambah: {hobi}")
print("-" * 25)
