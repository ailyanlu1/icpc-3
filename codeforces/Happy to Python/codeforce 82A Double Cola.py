a=['Sheldon','Leonard','Penny','Rajesh','Howard']
n= input()-1;
i= 5;
while n>=i:
    n-=i
    i*= 2
print a[n/(i/5)];
