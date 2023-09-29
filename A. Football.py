n = input()

for1=for0=0

for i in n:
    if i=="0":
        for0+=1
        for1=0
    else:
        for1+=1
        for0=0
    if for1 >= 7 or for0 >= 7:
        print("YES")
        break
else:
     print("NO")
