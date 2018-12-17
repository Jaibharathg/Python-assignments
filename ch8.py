fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    l1 = line.split()
    for f in l1:
        if not f in lst:
            lst.append(f)

lst.sort()
print(lst)
