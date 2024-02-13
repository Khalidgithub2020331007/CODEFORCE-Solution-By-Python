s=input()
stack=[]
for i in range(len(s)):
    if(len(stack)==0):
        stack.append(s[i]);
    elif (stack[len(stack)-1]==s[i]):
        stack.pop()
    else:
        stack.append(s[i])
if(len(stack)==0):
    print("YES")
else:
    print("NO")
