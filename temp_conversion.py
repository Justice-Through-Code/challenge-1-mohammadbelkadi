

def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    celsius_100 = (100 - 32) * 5 / 9
    print(celsius_100)
    print('float')
    # it is a float because 37.7 cannot be an interger due to it being a decimal.
convert_100_to_celsius()

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    celsius_0 = (0 - 32) * 5 / 9
    print(celsius_0)
convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    celsius_34_2 = (34.2 - 32) * 5 / 9
    print(celsius_34_2)
convert_34_2_to_celsius()    

'''
Now, can you convert back?
'''

def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    convert_5_to_fahrenheit = (5 * 9 / 5) + 32
    print(convert_5_to_fahrenheit)
convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
   print('30.2 degrees celsius')
hotter_temp() 

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))


temp = float(input("Enter temperature in Fahrenheit: "))
celsius = (temp - 32) * 5/9
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")