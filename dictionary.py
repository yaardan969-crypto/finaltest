# 6. Contoh Dictionary

print("--- Dictionary ---")
# Membuat dictionary data mahasiswa
mahasiswa = {
    "nama": "Budi",
    "nim": "123456",
    "jurusan": "Informatika",
    "ipk": 3.8,
    "mata_kuliah": ["Struktur Data", "Algoritma", "Basis Data"]
}

# 1. Mengakses nilai (value) menggunakan kunci (key)
print(f"Nama: {mahasiswa['nama']}")
print(f"Mata kuliah pertama: {mahasiswa['mata_kuliah'][0]}")

# 2. Menambah atau mengubah item
mahasiswa['ipk'] = 3.9  # Mengubah nilai yang sudah ada
mahasiswa['angkatan'] = 2022 # Menambah item baru
print(f"\nData setelah diupdate: {mahasiswa}")

# 3. Menghapus item menggunakan pop()
jurusan_yang_dihapus = mahasiswa.pop('jurusan')
print(f"Jurusan '{jurusan_yang_dihapus}' telah dihapus.")
print(f"Data setelah pop: {mahasiswa}")

# 4. Iterasi melalui dictionary
print("\nIterasi melalui keys dan values:")
for key, value in mahasiswa.items():
    print(f"- {key}: {value}")

print("-" * 25)
