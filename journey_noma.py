extras = ["soka" , "suka" , "shekpe"]
extras.append(200)

lumos = [40 , 30 , 20 , 50 , 30 , 10 , 30 , 'noma' , 'ngori']
lumos[3] = 420
count_30 = lumos.count(30)

extras.extend(lumos)
extras[1] = "puta"

only_the = ['konnichiwa' , 'kudasai' , 'jaane' , 'boushi' , 'kooto' , 'kutsu' , 'koko' , 'shiroi' , 'akaii']
del only_the[3]
only_the.remove('shiroi')
only_the.insert(3 ,'niku')
only_the.pop(5) #confer further
only_the.index('kooto')

new = ['chicken' , 'cow' , 'goat', 'sheep']
index_goat = new.index('goat')
for chicken in new : #confer further
    print(chicken)

print("Part 1 :" ,extras)
print("Part 2 :" ,lumos)
print('Part 3 :' ,only_the)
print("Part 4 :" ,new)
print(index_goat)
print(count_30)

salamu = {'calling out' : 'oya' , 'regular' : 'niaje' , 'casual' : 'mambo' , 'young' : 'rada' , 'coastal' :    'vipi' , 'disliked' : 'niambie'}
salamu ["cool"] = 'yo'
salamu['casual'] = 'sawa'
sorted_salamu = sorted(salamu)

print(salamu)
print(len(salamu))
print(all(salamu))
print(any('casual'))
print(sorted_salamu)
print('mambo' in salamu)

numbers = {13 , 27 , 44 , 23 , 79}
numbers.add(84)
numbers.discard(13)

words = ['hello', 'world', 'python', 'code']
numbers.update(words)

print(numbers)
print(type(numbers))
print(sum(numbers))
print(len(numbers))