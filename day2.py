#list
l=[2,4,5,6,7]
print(l[1])
l[2]=50
print(l)
print(len(l))
print(sum(l))
i=2
m=l.pop(i)
print(l)
l=[2,4,6,8,2]
m=l.count(2)
print(m)
l=[4,2,8,6]
l.sort()
print(l)
l=[3,4,5,6,7]
a=2
m=10
l.insert(a,m)
print(l)
m=[100,20]
l.extend(m)
print(l)
l.append(200)
print(l)
#dictionries
D = {'I':1,'V':5,'X':10,'L':50,'C':100}
print(D.keys())
print(D.values())
del D['X']
print(D)
D['f']=20
print(D)
print(len(D))
print(str(D))
#tuple
tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
print(len(tup))
print(tup[1])
#set
s={22,34,15,32,19}
print(s)
#string
s1="swati"
s2="kumari"
print(s1 + s2)
s3="swati","23","33","23"
print(s3)
print(s3.count("23"))
