print("inverted right-angled triangle: ")
i = int(input("how many rows: "))
while(i>0):
    j = i
    while(j>0):
      print('*', end=' ')
      j= j-1
    i=i-1
    print( )