secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
print("Enter a Number")
number= int(input())

while number != secret_number:
    print("Ha ha! You´re stock in my loop")
    print("Enter a New Number")
    number=int(input())
print("Well done, muggle! You are Free now")
