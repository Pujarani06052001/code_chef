n=int(input())
for x in range(n):
    u=int(input())
    l=list(map(int,input().split()))
    for i in l:
        if l.count(i)>2:
            print('no')
            break
    else:
        print('yes')
