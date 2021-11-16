#calculator program

print("two number calculator")
print("You can input two number and one calculator sign")
print()
print()

first_num = int(input("input first number : "))
second_num = int(input("input second number : "))
sign = str(input("input sign : "))  

if(sign == "+"):
	print("Result = " + str(first_num + second_num))
elif(sign == "-"):
	print("Result = " + str(first_num - second_num))
elif(sign == "*"):
	print("Result = " + str(float(first_num) * float(second_num)))
elif(sign == "/"):
	print("Result = " + str(float(first_num) / float(second_num)))
