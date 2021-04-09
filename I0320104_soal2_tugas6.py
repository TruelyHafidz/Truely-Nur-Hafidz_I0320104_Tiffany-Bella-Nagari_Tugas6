n = int(input("banyaknya data"))
data = []
total = 0
for i in range(0, n):
    a = int(input("Masukkan data ke-%d:" %(i +1)))
    data.append(a)
    total = total + data[i]
    rata_rata = total/n

print("rata rata = %0.2f" %rata_rata)
