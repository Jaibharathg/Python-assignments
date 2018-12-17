name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
l3 = dict()
for l1 in handle:
    if l1.startswith("From") and not l1.startswith("From:"):
        l2=l1.split()
    #    print("l2",l2[5])
        #if l3 is None:
        l4 = l2[5].split(':')
        l3[l4[0]] = l3.get(l4[0],0) + 1
        #else:
        #    l3 = l3.append(l2[5].split(':'))
#print("l3",sorted(l3))

lst = list()
for k,v in l3.items():
    nt = (k,v)
    lst.append(nt)

lst = sorted(lst)
for k,v in lst:
    print(k,v)
#print("l3",l3)
