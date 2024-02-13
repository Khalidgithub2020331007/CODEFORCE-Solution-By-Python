for _ in range(int(input())):
    a=int(input())
    lists=['a','a','a']
    if(a>27):
        lists[2]='z'
        a-=26
        if a>27:
            lists[1]='z'
            a-=26
            a+=96
            c=chr(a)
            lists[0]=c
        else:
            lists[0]='a'
            a-=1
            a+=96
            c=chr(a)
            lists[1]=c
    else:
        lists[0]='a'
        lists[1]='a'

        lists[2]=chr(a-2+96)
    for i in lists:
        print(i,end="")
    print()
