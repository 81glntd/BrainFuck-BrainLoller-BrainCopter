import time

print(time.localtime())




y = 3 + 4 + 5
print (y)

x = pow(3,2) + pow(4,2) + pow(5,2)
print(x)

if (pow(3,2) + pow(4,2)) == pow(5,2):
	print('plati')

z = 51 / 7
print(z)

z = 51 % 7
print(z)

myName = "Tomas Sykora";
print(len(myName.replace(" ","")))

print myName[0] 
print myName[1] 
print myName[-1]
print myName[-2:-1]
print('sdsds')
#x = input('zadej x;')
#y = input('zadej y:')

if x <y:
 	print('Y (%d) je vetsi'  %y)
else:
	print('X (%d) je vetsi'  %x)
if x > y:
 	print('Y (%d) je mensi'  %y)
else:
	print('X (%d) je mensi'  %x)

x = myName.split()
print (x)

print(abs(len(x[0]) - len(x[1])))

if 0 and '' or "Ahoj!":
	print('vubec nevim co to dela')

i = 0
while i < 11:
	print('ahoj')
	i = i + 1
j=1
while j < 10:
	print(j)
	j = j + 1

print("\n")
m = 0
while m < len(myName):
	print(myName[m])
	m= m + 1

print("\n")
for letter in myName:
	print(letter)

jj = 0
print("\n")

for m in range(0,10):
	jj = jj + m
print(jj)

#for m in range(0,10):
#	jj = jj + m
print(jj/10.0)


#rok = str(time.localtime()[0])
#mesic = str(time.localtime()[1])
#den = str(time.localtime()[2])
#hodina = str(time.localtime()[3])
#minuta = str(time.localtime()[4])

print(str(time.localtime()[0]) + " "+str(time.localtime()[1]))

print("Prave je :    " + str(time.localtime()[2]) +"."+ str(time.localtime()[1])+"."+ str(time.localtime()[0]) + "  " + str(time.localtime()[3])+":" + str(time.localtime()[4]))