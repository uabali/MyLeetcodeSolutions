def bubble_sort(arr):
    n = len(arr)
    swapped = False  # Bir takas işlemi gerçekleşti mi?

    for i in range(n - 1):
        swapped = False  # Başlangıçta hiç takas işlemi olmadı
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Elemanları yer değiştir
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Takas işlemi gerçekleşti

        # Eğer herhangi bir takas işlemi olmadıysa, dizi zaten sıralıdır
        if not swapped:
            break

arr = [11, 12, 22, 25, 34, 64, 90]  # Zaten sıralı dizi

print("Dizi sıralanmadan önce:")
print(arr)

bubble_sort(arr)

print("Dizi sıralandıktan sonra:")
print(arr)
