'''
## -------------------lambda functions--------------

wish = lambda name: f'hello {name}, welcome to python'
print(wish("a"))
print(wish("b"))

add = lambda a,b,c: (a+b+c)/3
print(add(1,2,3))
print(add(6,7,8))

iseven = lambda n: "Even" if n%2==0 else "Odd"
print(iseven(19))
print(iseven(18))


greater = lambda a,b: "Greater" if a>b else "Smaller"
print(greater(4,6))
print(greater(6,2))

isvowel = lambda a: "Vol" if a in vol else "Con"
vol="aeiouAEIOU"
print(isvowel('a'))
print(isvowel('d'))


l=['ab','bc','cd','ef']
res = list(map(lambda i:i.title(),l))
print(res)


l=[20,30,40,50,60,80]
res = list(filter(lambda i:i%3==0,l))
print(res)


l=[20,30,40,50,60,80]
res = list(filter(lambda i:i>60,l))
print(res)

l=[20,30,40,50,60,80]
res = list(filter(lambda i:i<=60,l))


l={'laptop':True,
   'iphone':False,
   'mouse':True,
   'tablet':False,
   'charger':True
}
res = list(filter(lambda i:l[i],l))
print(res)

l=[1,0,2,3,0,1,3,4,5,5,6,2,3,5,6,7,8,2]
res = list(filter(lambda i:i%2==0,l))
print(res)

l=[1,0,2,3,0,1,3,4,5,5,6,2,3,5,6,7,8,2]
res = list(filter(lambda i:i!=0,l))
print(res)


from functools import reduce
l=[1,0,2,3,0,1,3,4,5,5,6,2,3,5,6,7,8,2]
res = reduce(lambda a,b:a*b,l)
print(res)

from functools import reduce
l=[1,0,2,3,0,1,3,4,5,5,6,2,3,5,6,7,8,2]
res = reduce(lambda a,b:a+b,l)
print(res)
'''

from functools import reduce
l=['python','java','c++','c','html','reactjs']
res = reduce(lambda a,b:a+' '+b,l)
print(res)


'''
l=[10,20,30,40]
res = [20,30,40,50]=> map
res1=[20,40]=> filter
res2=100=> reduce
'''
d={'apple':30,
   'arange':25,
   'pineapple':60,
   'grapes':50,
   'banana':40
}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(), key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(), key=lambda i:i[1],reverse=True)))




















