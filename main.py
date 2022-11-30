import numpy as np
n=int(input('\nВведите число - количество участников:  '))+1
a = np.array([["№"]])
for i in range(1, n):
    a=np.append(a, "Участник №"+str(i))
m=int(input('\nВведите число приоритетов:  '))+1
for i in range(1, m):
    s = np.array([str(i)])
    for j in range(1, n):
        s = np.append(s, "-")
    a = np.vstack([a, s])
print()
def pr(a):
    for i in range(m):
        for j in range(n):
            if j == 0:
                print('%-5s' % (a[i, j]), end="")
            else:
                print('%12s' % (a[i, j]), end="  ")
        print()
pr(a)
for i in range(m-1):
    r = input('\nВведите результаты голосования по ' + str(i+1) + ' приоритету (через пробел) :  ')
    s = np.array([str(i+1)])
    s=np.append(s, np.fromstring(r, dtype = int, sep = ' '))
    a[i+1]=s
print()
pr(a)
k = int(input('\nВыберите метод принятия решения (1-Модель Борда; 2-Метод относительного большинства) :  '))
if k==1:
    sum=np.zeros((m,n-1))
    x=m
    for i in range(1, m):
        for j in range(1, n):
           sum[i-1, j-1]=int(a[i, j])*x
        x=x-1
    print('\nДомножение голосов на баллы:')
    for i in range(m-1):
        for j in range(n-1):
                print('%12s' % (sum[i, j]), end="  ")
        print()
    for i in range(m-1):
        for j in range(n-1):
            sum[m - 1, j]=sum[m-1, j]+sum[i,j]
    print('\nСумма баллов каждого участника:')
    for i in range(n-1):
            print('%12s' % (sum[m-1, i]), end="  ")
    max=0
    k=0
    for i in range(len(sum)):
        if max<sum[m-1, i]:
            max=sum[m-1, i]
            k=i+1
    print()
    print("\nНаибольшее количество баллов набал участник №",k)
else:
    max=0
    for i in range(1, m+1):
        if max<int(a[1,i]):
            max=int(a[1,i])
    for i in range(1, m+1):
        if int(a[1,i])==max:
            print('\nВыиграл участник с максимальным количеством баллов - Участник №',i)