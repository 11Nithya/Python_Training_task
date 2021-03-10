a = []

b = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, b + 1):
    value = int(input("Please enter the Value of  Element : "))
    a.append(value)

for i in range (b):
    for j in range(i + 1, b):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)

