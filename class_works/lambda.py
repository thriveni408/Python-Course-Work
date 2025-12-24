#welcome example
def wish(name):
    return f'Welcome to python {name}!'

print(wish("Thriveni"))
print(wish("Pramodh"))
print(wish("Shirisha"))

#same example using lambda 
lwish=lambda name : f'Welcome to python {name}!'
print(lwish("Thriveni"))
print(lwish("Pramodh"))
print(lwish("Shirisha"))



#squares example
def squares(n):
    return f'Squares of {n}: {n*n}!'

print(squares(2))

#same example using lambda
lsquares=lambda n : f'Squares of {n}: {n*n}!'

print(lsquares(4))

#add example
def add(a,b):
    return a+b
print(add(2,3))


ladd=lambda a,b : a+b
print(ladd(2,3))


#even or odd example
def evenorodd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(evenorodd(13))

eoro=lambda n : "Even" if n%2==0 else "Odd"
print(eoro(12))



#vowels and consonants example

vol='aeiouAEIOU'
eoro=lambda ch: "Vol" if ch in vol else "con"


print(eoro('a'))
print(eoro('t'))



# using map()
#list updating example 
l=[1,2,3,4,5]

res=list(map(lambda i: f'{i}%',l))

print(res)


#captilize or title the names
l=[1,2,3,4,5]
names=['ajay kumar','sai krishna','sathish babu']
res1=list(map(lambda i: i.title(),names))

print(res1)


#GST example
l=[1,2,3,4,5]
price=[20000,38000,44000]

res2=list(map(lambda i: f'${i+i*0.18}' ,price))

print(res2)


#using filter()
#list updating example 
l=[1,2,3,4,5]
res=list(filter(lambda i: i%2==0,l))

print(res)

#captilize or title the names
l=[1,2,3,4,5]
names=['ajay kumar','sai krishna','sathish babu']
res1=list(filter(lambda i: i[0]=='s',names))

print(res1)

#GST example
l=[1,2,3,4,5]
price=[20000,38000,44000]
res2=list(filter(lambda i: i>35000 ,price))

print(res2)

#grocery using distionary
products={
    'milk':20,
    'bread':0,
    'soap':10,
    'butter':15,
    'headset':0,
    'sugar':0,
    'salt':1,
    'chilli powder':0
    }
res3=list(filter(lambda i: products[i]==0, products))

print(res3)




from functools import reduce

l=[1,2,3,4,5]
res=reduce(lambda a,b:a+b,l)
print(res)


l=[1,2,3,4,5]
res=reduce(lambda a,b:a*b,l)
print(res)


l=[1,2,3,4,5]
lang=['java','python','c','javascript','csharp','ruby']
res=reduce(lambda a,b:a+' '+b, lang)
res1=reduce(lambda a,b:a+','+b, lang)
res2=reduce(lambda a,b:a+b, lang)

print(res)
print(res1)
print(res2)



d={
    'praveen':80,
    'mohan':67,
    'manoj':54,
    'teja':96,
    'gopi krishne':84
}
print(d.items())
print(sorted(d.items()))


d={
    'praveen':80,
    'mohan':67,
    'manoj':54,
    'teja':96,
    'gopi krishne':84
}
print(d.items())
print(dict(sorted(d.items(),key= lambda i:i[0])))
print(dict(sorted(d.items(),key= lambda i:i[0],reverse=True)))

print(dict(sorted(d.items(),key= lambda i:i[1])))
print(dict(sorted(d.items(),key= lambda i:i[1],reverse=True)))



































