# #===6061
# a,b= map(int, input().split())
# print(a|b)

# #===6062
# a,b= map(int, input().split())
# print(a^b)

# #===6063
# a,b= map(int, input().split())
# if a>b: print(a)
# else: print(b)

# #===6064
# a,b,c= map(int, input().split())
# print((a if a<b else b) if ((a if a<b else b)<c) else c)

# #===6065
# a,b,c= map(int, input().split())
# if a%2==0: print(a)
# if b%2==0: print(b)
# if c%2==0: print(c)

#===6066
# lst= map(int, input().split())
# for i in lst:
#     if i%2==0: print('even')
#     else: print('odd')

# #===6067
# a= int(input())
# if a%2==0 and a<0: print("A")
# elif a%2!=0 and a<0: print("B")
# elif a%2==0 and a>0: print("C")
# else: print("D")

# #===6068
# n=int(input())
# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#     print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D')

# #===6069
# a= input()
# if a=='A': print('best!!!')
# elif a=='B': print('good!!')
# elif a=='C': print('run!')
# elif a=='D': print('slowly~')
# else: print('what?')

# #===6070
# a= int(input())
# if a//3==1: print('spring')
# elif a//6==1 and a%6<3: print('summer')
# elif a//9==1 and a%9<3: print('fall')
# else: print('winter')

# #===6071
# n=1
# while n!=0:
#     n=int(input())
#     if n!=0: print(n)
#     else: break

# #===6072
# a= int(input())
# for i in range(5):
#     print(5-i)

# #===6073
# a= int(input())
# while a!=0:
#     a=a-1
#     print(a)

# #===6074
# n= ord(input())
# a= ord('a')
# while a<=n:
#     print(chr(a))
#     a= a+1

# #===6075
# a= int(input())
# n=0
# while n<=a:
#     print(n)
#     n=n+1

# #===6076
# a= int(input())
# for i in range(a+1):
#     print(i)

# #===6077
# a= int(input())
# sum=0
# for i in range(a+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# #===6078
# a='a'
# while a!='q':
#     n=input()
#     if n!='q': print(n)
#     else: break

# #===6079
# a= int(input())
# num=0
# n=0
# while num<a:
#     n=n+1
#     num+=n
# print(n)

# #===6080
# a,b= map(int, input().split())
# for i in range(a):
#     for j in range(b):
#         print(i+1,j+1, sep=' ')

# #===6081
# a= int(input(),16)
# for i in range(1,16):
#     print('%X'%a,'*%X='%i,'%X'%(a*i), sep='')

# #===6082
# a= int(input())
# for i in range(1,a+1):
#     if i%3==0: print('X', end=' ')
#     else: print(i, end=' ')

# #===6083
# r,g,b= map(int, input().split())
# n= r*g*b
# for i in range(r):
#     for j in range(g):
#         for p in range(b):
#             print(i,j,p)

# #===6084
# h, b, c, s = map(int, input().split())
# mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
# print('{} MB'.format(mb))

# #===6085
# w, h, b = map(int, input().split())
# mb = round(((w*h*b) / 8 / 1024 / 1024), 2)
# print('{:.2f} MB'.format(mb))

# #===6086
# a= int(input())
# num=0
# n=0
# while num<a:
#     n=n+1
#     num+=n
# print(num)

# #===6087
# a= int(input())
# for i in range(1,a+1):
#     if i%3==0:continue
#     else: print(i, end=' ')

# #===6088
# a,d,n= map(int, input().split())
# for i in range(n-1):
#     a+=d
# print(a)

# #===6089
# a,r,n= map(int, input().split())
# for i in range(n-1):
#     a=a*r
# print(a)

# #===6090
# a,m,d,n= map(int, input().split())
# for i in range(n-1):
#     a=a*m+d
# print(a)

# #===6091
# a, b, c = map(int, input().split())
# d = 1
# while d % a != 0 or d % b != 0 or d % c != 0:
#     d += 1
# print(d)

# #===6092
# a= int(input())
# lst= list(map(int, input().split()))
# for i in range(1,24):
#     if i in lst:
#         print(lst.count(i), end=' ')
#     else: print(0, end=' ')

# #===6093
# a= int(input())
# lst= input().split()
# lst.reverse()
# for i in lst:
#     print(i, end=' ')

# #===6094
# a= int(input())
# lst= input().split()
# print(min(lst))

# #===6095
# li = [[0 for i in range(19)]
# for j in range(19)]
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     if(li[x-1][y-1] != 1):
#         li[x-1][y-1] = 1
#         for i in li:
#             print(' '.join(map(str, i)))

# #===6096
# li = []
# for i in range(19):
#     li.append([])
#     k = input().split()
#     for e in k:
#         li[i].append(int(e))
#         n = int(input())
#         x = []
#         y = []
#         for i in range(n):
#             a, b = map(int, input().split())
#             for j in range(19):
#                 li[a-1][j] = 1
#                 if li[a-1][j] != 1
#                 else 0 li[j][b-1] = 1
#                 if li[j][b-1] != 1
#                 else 0
#                 for i in li:
#                     print(' '.join(map(str, i)))

# #===6097
# li = []
# h, w = map(int, input().split())
# for i in range(h):
#     li.append([])
#     for j in range(w):
#         li[i].append(0)
#         n = int(input())
#         for i in range(n):
#             l, d, x, y = map(int, input().split())
#             for j in range(l):
#                 if d == 0:
#                     li[x-1][y-1] = 1
#                     y += 1
#                     else:
#                         li[x-1][y-1] = 1
#                         x += 1
#                         for i in li:
#                             print(' '.join(map(str, i)))

# #===6098
# li = []
# for i in range(10):
#     li.append([])
#     k = input().split()
#     for e in k:
#         li[i].append(int(e))
#         x, y = 1, 1
#         flag = True
#         while flag:
#             if li[x][y] == 2:
#                 li[x][y] = 9
#                 flag = False
#                 elif (li[x][y+1]) == 1:
#                     if li[x+1][y] == 1:
#                         li[x][y] = 9
#                         flag = False
#                         else: li[x][y] = 9
#                         x += 1 else:
#                         li[x][y] = 9
#                         y += 1
#                         for i in li:
#                             print(' '.join(map(str, i)))
