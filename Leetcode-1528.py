s = input()
indices = list(map(int,input().split()))
l = list(s)
for i in range(len(indices)):
    for j in range(i+1,len(indices)):
        if indices[i]>indices[j]:
            indices[i],indices[j] = indices[j],indices[i]
            l[i],l[j] = l[j],l[i]
print("".join(i for i in l))