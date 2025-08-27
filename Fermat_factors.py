import math
n = int(input("Enter a odd number to find Fermat Factors: "))
if n<=1:
    print("Enter a number greater then 1")
elif n%2 ==0:
    print("Enter a Odd number")
else:
    t = int(math.sqrt(n))
    if t*t == n:
        print(t)
t +=1
while True:
    s_squared = t*t -n
    s = int(math.sqrt(s_squared))  
    if s*s == s_squared:
        break
    t += 1

a = t+s
b = t-s
print(a)
print(b)


    

