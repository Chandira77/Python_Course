#calculate the simple interest
"""p = 100
t = 35
r = float(4.5)
SI = (p * t * r) / 100
print("the simple interest =", SI)
"""


def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     
# Driver code
simple_interest(8, 6, 8)
