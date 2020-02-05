# 1 задача

for i in range(1,6):
   print(i, i*0)
#2 задача
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())
summm = 0
if a==5:
    summm += 1
if b==5:
    summm += 1
if c==5:
    summm += 1
if d==5:
    summm += 1
if e==5:
    summm += 1
if f==5:
    summm += 1
if g==5:
    summm += 1
if h==5:
    summm += 1
if i==5:
    summm += 1
if j==5:
    summm += 1
print("сумма пятерок", summm)
#задача 3
# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)
# задача 4
umnoj = 1
for i in range(1,11):
    umnoj *= i
print("произведение равно", umnoj)
#задача 5
# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10
#задача 6, 7
n = int(input())
mult = 1
summ = 0
while n > 0:
    if n%10!= 0:
        mult = mult*(n%10)
    summ = summ + n%10
    n = n//10
print ("сумма цифр числа равна", summ)
print ("произведение цифр числа равна", mult)
#задача 8
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
# задача 9
a = int(input())
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print("максимальная цифра числа", m)
#10 задача
n=int(input())
k=0
while n!=0:
    d=n%10
    if d==5:
        k +=1
    n=n//10
print("количество единиц в числе", k)
