# 1. Contoh Tipe Data Array (menggunakan list di Python)

# a. Array Satu Dimensi
# Kumpulan item dalam satu baris.
print("--- Array Satu Dimensi ---")
array_1d = [10, 20, 30, 40, 50]
print(f"Array 1D: {array_1d}")
# Mengakses elemen dengan indeks (dimulai dari 0)
print(f"Elemen ke-3 (indeks 2): {array_1d[2]}")
print("-" * 25)

# b. Array Dua Dimensi (Matriks)
# List yang berisi list lain, membentuk struktur baris dan kolom.
print("--- Array Dua Dimensi ---")
array_2d = [
    [1, 2, 3],  # Baris 0
    [4, 5, 6],  # Baris 1
    [7, 8, 9]   # Baris 2
]
print("Array 2D:")
for baris in array_2d:
    print(baris)
# Mengakses elemen dengan indeks [baris][kolom]
print(f"Elemen pada baris 1, kolom 2: {array_2d[1][2]}") # Output: 6
print("-" * 25)

# c. Array Tiga Dimensi
# List yang berisi list dua dimensi.
print("--- Array Tiga Dimensi ---")
array_3d = [
    [ # Layer 0
        [1, 2],
        [3, 4]
    ],
    [ # Layer 1
        [5, 6],
        [7, 8]
    ]
]
print("Array 3D:")
print(array_3d)
# Mengakses elemen dengan indeks [layer][baris][kolom]
print(f"Elemen pada layer 1, baris 0, kolom 1: {array_3d[1][0][1]}") # Output: 6
print("-" * 25)
