#print("hello python!")

#-variables-
#name = "manoj"     #str
#age = 21           #int
#cgpa = 8.1         #float
#arrears = False    #boolean

#-type casting-
#print(type(age))       #to check the datatype
#age = float(age)       #to change the datatype

#-arithmetic operations-
#number = 5
#number += 3        #addition
#number -= 3        #subtraction
#number *= 3        #multiplication
#number /= 3        #division
#number %= 3        #modulus
#number **=2        #exponent(power)

#-math funtions - part 1 
#result = round(num)            #round off
#result = abs(num)              #absolute value
#result = pow(num, 2)           #power
#result = min(num1,num2,num3)   #minimum
#result = max(num1,num2,num3)   #maximum

#-math funtions - part 2
#import math                    #module import
#print(math.pi)                 #pi value
#print(math.e)                  #exponential constant value
#print(math.sqrt(144))          #square root
#print(math.ceil(7.5))          #round up
#print(math.floor(7.5))         #round down
#print(round(circumstance, 3))  #round & cut off certain digits after point [1.23456789 -> 1.234]

#-if, else if, else conditions-
#if condition :
    #print()
#elif:
    #print()
#else:
    #print()

#-logical operators-
#and        #all conditions must be true 
#or         #atleast one condition must be true
#not        #inverts the condition (true -> false & false -> true)

#-conditional expression-
# "X" if condition else "Y"     #one line shortcut for if else statemnet 
#print("positive" if num > 0 else "negative")

#-string methods-
#name = "manoj"                 
#len(name)                      #returns the lenght of the string
#name.find("a")                 #finds the first occurance of the character
#name.rfind("a")                #finds the last occurance of the character
#name.capitalize()              #returns the first letter in caps
#name.upper()                   #converts entire string to upper case
#name.lower()                   #converts entire strinb to lower case
#name.isdigit()                 #returns true if string contains only numbers (false if mixed with numbers and letters)
#name.isalpha()                 #returns true if string contains only letters (false if contains number or spaces)
#name.count("h")                #counts the no. of occurances of the character
#name.replace("o", "g")         #replaces one with another

#-string indexing-          #accessing elements of a string  [start : end : step]
#numbers = "123-456-789-012"
#print(numbers[0])          #to print one charcter based on ondex value
#print(numbers[:5])         #to print a range of characters (start to X)
#print(numbers[3:])         #to print a range of characters (X to end)
#print(numbers[4:8])        #to print a range of characters (X to Y)
#print(numbers[-1])         #to print from reverse
#print(numbers[2:8:3])      #to print a range with a specific step count
#print(numbers[::-1])       #to print the strings in reverse

#-format specifiers-                #values formatted based of flags -> {value:flag}
#value = 1244.3862
#print(f"value is {value:.2f}")      #prcision decimal point
#print(f"value is {value:10}")       #space before value
#print(f"value is {value:010}")      #zero padding before value
#print(f"value is {value:<10}")      #left align
#print(f"value is {value:>10}")      #right align
#print(f"value is {value:^10}")      #center align
#print(f"value is {value:,}")        #1000s value seperator