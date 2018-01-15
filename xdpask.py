#pask

file = open("xd.txt")
ju = {}

for rida in file:
    for taht in rida:
        if taht in ju:
            ju[taht] += 1
        else:
            ju[taht] = 1


print(ju)



