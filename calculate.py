#calculator program

print("two number calculator")
print("You can input formula")
print()
print()

formula = str(input("input formula : "))
divided = formula.split()

if(str(divided[1]) == "+"):
	print("Result = " + str(int(divided[0]) + int(divided[2])))
elif(str(divided[1]) == "-"):
	print("Result = " + str(int(divided[0]) - int(divided[2])))
elif(str(divided[1]) == "*"):
	print("Result = " + str(float(divided[0]) * float(divided[2])))
elif(str(divided[1]) == "/"):
	print("Result = " + str(float(divided[0] / float(divided[2])))
