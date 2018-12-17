def computepay(h,r):
    sum =0
    if(h>40):
        sum=(((h-40)*1.5*r) + (40*r))
    else:
        sum = h*r

    return sum

hrs = float(input("Enter Hours:"))
r = float(input("Enter RAte:"))
p = computepay(hrs,r)
print("Pay",p)
