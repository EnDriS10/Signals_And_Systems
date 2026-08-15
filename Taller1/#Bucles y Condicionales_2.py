#Combinacion de a en b

a = input("introduce un numero ")
a_= int(a)

b = input("introduce otro numero ")
b_= int(b)

c_=a_-b_

for i in range(1 , a_):
    a_=a_*i

for i in range(1 , b_):
    b_=b_*i

for i in range(1 , c_):
    c_=c_*i

Comb = (a_)/(b_*c_)

print(Comb)