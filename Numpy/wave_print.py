# str=input().strip().split(" ")
# n=int(str[0])
# m=int(str[1])
# l=[int(i) for i in input().strip().split(" ")]
# out=[]
# for i in range(n):
#     out.append([])
#     for  j in range(m):
#         out[i].append(l[i*m+j])
# out
# out2=[[l[i*m+j] for j in range(m)] for i in range(n)]
# out2
n=len[out2]
m=len[out2[0]]
for j in range(m):
    if j%2==0:
        for i in range(n):
            print(out2[i][j],end =" ")
    else:
        i=n-1
        while(i>=0):
            print(out2[i][j],end =" ")
            i=i-1
for j in range(10,0,-1):
    print()