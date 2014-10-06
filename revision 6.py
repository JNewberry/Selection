#30/09/14
#John Newberry
#selection revision 6
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))
if number1 > number2 and number3:
    greater_number1 = number1
if number2 > number1 and number3:
    greater_number1 = number2
if number3 > greater_number1:
    print("{0} is the largest.".format(number3))
if number3 < greater_number1:
    print("{0} is the largest.".fomat(greater_number1))

                
