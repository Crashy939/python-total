#Conversiones implícitas
num1 = 30
num2 = 4.6

print(type(num1))
print(type(num2))

num1 = num1 + num2
print(type(num1))

#Conversiones explícitas
num3 = 4.6
num3 = num3
print("\n", num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))

edad = int(input("\nIngresa tu edad: "))
nueva_edad = edad + 1

print("Tu nueva edad en un año será:", nueva_edad)
