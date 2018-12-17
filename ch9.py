fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for l1 in fh:
    if not l1.startswith('From:'):
        if l1.startswith('From'):
            count = count  + 1
            l2 = l1.split()
            print(l2[1])


print("There were", count, "lines in the file with From as the first word")
