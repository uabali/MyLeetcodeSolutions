def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Minimum elemanın dizideki indeksini bul
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Minimum elemanı bulunan elemanla yer değiştir
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
print("Dizi sıralanmadan önce:")
print(arr)

selection_sort(arr)

print("Dizi sıralandıktan sonra:")
print(arr)
