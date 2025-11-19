is_ = ''
s = ""
s = ''' '''
s = "' '"

name = 'Ajay'
name1 = "Krishna"

print(name + name1)
print(name + ' ' + name1)
print(name + ' ' + name1)
print(name)
print(name * 10)
print('*' * 100)
print('-' * 10)
print('----------')

name = 'Ajay Kumar'
print(name[3])
print(name[-2])
print(name[-5])
print(name[1])

names = 'AjayKrishnaSatishNishithaPreethiRuchitha'

print(names[0:4])
print(names[:4])
print(names[4:11])
print(names[11:17])
print(names[17:25])
print(names[25:32])
print(names[32:40])
print(names[32:])
print(names[0:4:2])
print(names[::3])
print(names[-8:])
print(names)

print(names[-15:-8])
print(names[-23:-15])
print(names[-29:-23])
print(names[-36:-29])
print(names[-40:-36])
print(names[::-1])
print(names)

print(names[4::-1])
print(names[3::-1])
print(names[10:4])
print(names[10:4:-1])
print(names[10:3:-1])
print(names[16:10:-1])
print(names[24:16:-1])
print(names[31:24:-1])
print(names[39:31:-1])

print('Ajay' in names)
print('nithin' in names)
print('priya' in names)
print('sahithi' not in names)

print(names.upper())
print(names.lower())
print(names.swapcase())

l = "python programming language"
print(l.capitalize())
print(l.title())
print("ß".casefold())

print('priya' in names)

print(l.center(100, '*'))
print(l.center(50, '*'))
print(l.center(50, '-'))
print(l.center(50, '_'))
print(l.ljust(50, '-'))
print(l.ljust(50, ' ') + ':')
print(l.rjust(50, '-'))

print('2'.zfill(6))
print('202'.zfill(6))
print('202123'.zfill(6))

print(names.find('j'))
print(names.find('a'))
print(names.find('Ajay'))
print(names.find('z'))
print(names.rfind('a'))
print(names.index('K'))
print(names.index('a'))
print(names.rindex('a'))

print(names.count('a'))
print(names.count('e'))
print(names.count('i'))

print(names.replace('a','*'))
print(names.replace('sh',''))
print(names.replace('sh','00'))
print(names.replace('sh','-00-'))
print(names.replace('Ajay','Anirudh'))

print(names.translate(names.maketrans('aeiou','*****')))
print(names.translate(names.maketrans('AEIOUaeiou','1234500000')))