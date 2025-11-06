import math
n=int(input("enter number of terms:"))
total_sum=0
for i in range(1,n+1):
    term=1/math.factorial(i)
    if i%2==0:
        total_sum-=term
    else:
        total_sum+=term
print(f"\nsum of the series upto {n} terms={total_sum}")
            
