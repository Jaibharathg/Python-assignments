fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
dictio = dict()
for l1 in fh:
    if not l1.startswith('From:'):
        if l1.startswith('From'):
            count = count  + 1
            l2 = l1.split()
        #    print(l2[1])
            dictio[l2[1]] =dictio.get(l2[1],0)+1

#print("There were", count, "lines in the file with From as the first word")
#print(dictio)
b1 = None
b2 = None
for k,v in dictio.items():
    if b1 is None or v > b1:
        b1=v
        b2=k

print(b2,b1)
