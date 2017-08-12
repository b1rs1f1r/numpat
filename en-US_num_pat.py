num1=int(input("Enter start number: "))
num2=int(input("Enter finish number: "))
num3=int(input("Enter increase: "))

list1=[x for x in range(num1,num2) if x % num3 == 0]

print(list1)