import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Data usia yang akan diurutkan
usia = [25, 18, 30, 22, 40, 28, 19, 35, 50, 27, 32, 21, 45, 29, 33, 23, 26, 20, 31, 24]

print("Data sebelum diurutkan:", usia)
start_time = time.time()
selection_sort(usia)
end_time = time.time()
print("Data setelah diurutkan:", usia)
print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")
