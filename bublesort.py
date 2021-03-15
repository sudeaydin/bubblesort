a=[6,2,11,7,5]
n=len(a)
k=0
swapped=True
while (swapped):
     swapped=False
     for i in range(n-k-1):
         if a[i]>a[i+1]:
           a[i],a[i+1]=a[i+1],a[i]
           swapped=True
     k=k+1

print(a)
