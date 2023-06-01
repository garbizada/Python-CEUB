#logical operatos (and, or, not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside: "))

if temp >= 0 and temp <= 30:            #both conditions must be true to work!!
  print("The temperature is good today!!")
  print("Go outside!")


elif temp < 0 or temp > 30:              #as long as one condition is true it works
  print("The temperature is bad today!")
  print("Stay inside!!")

#THE [NOT] OPERATOR TURNS THE CONDITION TRUE IF IT IS FALSE, AND IF ITS FALSE BECOMES TRUE 
# FOR EXAMPLE HERE ITS HOW YOU USE IT

#if not(temp >= 0 and temp <=30):
# if the conditions written inside is true then the NOT will turn it to false
