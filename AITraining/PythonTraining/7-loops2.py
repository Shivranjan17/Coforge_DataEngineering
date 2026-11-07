for i in range(1,50,2):
    print(i)
for i in range(0,51,2):
    print(i)
evenoddsum=0
evenoddcount=0
evensum=0
evencount=0
oddsum=0
oddcount=0


for i in range(1,51):
    evenoddsum +=i
    evenoddcount +=1
    if i%2 ==0:
        evencount +=1
        evensum +=i
        print(evencount)
        print(evensum)
    else:
        oddcount += 1
        oddsum+=i
        print(oddcount)
        print(oddsum)
print(i)
print(evenoddcount)
print(evenoddsum)
    

