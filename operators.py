"""Operators"""

# Arithmetic operator = +, -, *, /, %, // (floor divison), **(Exponentiation)

a = 5 
b = 25

print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a // b)        # floor divison
print (5 ** 2)        # Exponentiation 
print (32 % 5)        # modulus 

# Assignment operator
 
c = 20
c = c + 20
c = c + 40          # Compound assignment operator
c = c + 60

print (c)

# Comparison operator  

a = 12.1
b = 12

print (a == b)
print (a != b)
print (a > b)
print (a < b)

print (22 > 22)
print (22 >= 22)
print (22 <= 22)

# Logical operators = and, or, not

print (123 > 100 and 34 == 34 and 45 < 90 and 12 > 20)
print (12 != 12 or 23 == 45 or 67 == 56 or 10 > 5)
print (not 12 == 12)
