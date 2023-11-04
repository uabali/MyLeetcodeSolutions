def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Elemanları değiştir
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Max heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Max heap'tan elemanları sıralı bir şekilde çıkar
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Kök elemanı ile son elemanı değiştir
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
print("Dizi sıralanmadan önce:")
print(arr)

heap_sort(arr)

print("Dizi sıralandıktan sonra:")
print(arr)
