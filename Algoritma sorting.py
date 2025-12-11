# 4 & 5. Contoh Algoritma Sorting

data_acak = [64, 25, 12, 22, 11]
print(f"Data sebelum diurutkan: {data_acak}\n")

# a. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Salin array agar tidak mengubah array asli
    arr_copy = arr[:]
    # Lakukan iterasi sebanyak n kali
    for i in range(n):
        swapped = False
        # Iterasi dari elemen pertama hingga elemen yang belum terurut
        for j in range(0, n-i-1):
            # Tukar jika elemen yang ditemukan lebih besar dari elemen berikutnya
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                swapped = True
        # Jika tidak ada pertukaran dalam satu iterasi, array sudah terurut
        if not swapped:
            break
    return arr_copy

print(f"Bubble Sort: {bubble_sort(data_acak)}")


# b. Selection Sort
def selection_sort(arr):
    arr_copy = arr[:]
    n = len(arr_copy)
    # Iterasi melalui semua elemen array
    for i in range(n):
        # Temukan elemen minimum di sisa array yang belum terurut
        min_idx = i
        for j in range(i+1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        # Tukar elemen minimum yang ditemukan dengan elemen pertama yang belum terurut
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    return arr_copy

print(f"Selection Sort: {selection_sort(data_acak)}")


# c. Insertion Sort
def insertion_sort(arr):
    arr_copy = arr[:]
    # Iterasi dari elemen kedua hingga akhir
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        # Pindahkan elemen dari arr[0..i-1] yang lebih besar dari key
        # ke satu posisi di depan posisi mereka saat ini
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

print(f"Insertion Sort: {insertion_sort(data_acak)}")
print("-" * 25)
