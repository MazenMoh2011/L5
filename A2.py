print("half pyramid with numbers: ")
n = int(input("how many rows do you want: "))
m = 0
for i in range(n):
    for j in range(i+1):
     m=m+1
     print(m, end=" ")
    print( )