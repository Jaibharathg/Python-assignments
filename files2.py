# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count =0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count +1
    p1 = line[len("X-DSPAM-Confidence:"):]
    sum = sum + float(p1.strip())
    #print(sum)
    #print(line)
avg = sum/count
print("Average spam confidence:",avg)
