# 3. Contoh Algoritma Pencarian

# Data harus terurut untuk kedua algoritma ini
data_urut = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

# a. Binary Search
print("--- Binary Search ---")
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Mencari di antara indeks {low} dan {high}, tengah: {mid}")
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid  # Elemen ditemukan
    return -1 # Elemen tidak ditemukan

hasil_binary = binary_search(data_urut, target)
if hasil_binary != -1:
    print(f"Binary Search: Elemen {target} ditemukan di indeks {hasil_binary}.")
else:
    print(f"Binary Search: Elemen {target} tidak ditemukan.")
print("-" * 25)


# b. Interpolation Search
print("--- Interpolation Search ---")
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        
        # Rumus interpolasi untuk menebak posisi
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        print(f"Mencari di antara indeks {low} dan {high}, tebakan posisi: {pos}")

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

hasil_inter = interpolation_search(data_urut, target)
if hasil_inter != -1:
    print(f"Interpolation Search: Elemen {target} ditemukan di indeks {hasil_inter}.")
else:
    print(f"Interpolation Search: Elemen {target} tidak ditemukan.")
print("-" * 25)

