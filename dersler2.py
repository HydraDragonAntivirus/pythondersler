sayi = 1
fibonacci_list = list()
fibonacci_list.append(1)
fibonacci_sayisi = 0
while len(fibonacci_list) != 100:
    sayi2 = sayi + sayi
    sayi3 = sayi2 + sayi
    sayi = sayi3
    fibonacci_list.append(sayi3)
print(fibonacci_list)