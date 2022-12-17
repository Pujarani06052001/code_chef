# l,r=map(int,input().split())
# for i in range(l,r+1):
#     if(i%2!=0):
#         print(i,end=" ")

# r=int(input("enter a number"))
# l=int(input("enter a number"))
# for i in range(l,r+1):
#     if(i%2!=0):
#         print(i,end=" ") 


# l,r=map(int,input().split())
l=int(input("enter a number"))
r=int(input("enter a number"))
sum=0
for i in range(l,r):
    sum=l+r
    # print(sum)
    # sum(l+r)
    if(sum%2!=0):
        print("Alice")
    else:
        print("bob")