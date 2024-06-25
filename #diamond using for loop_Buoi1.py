#diamond using for loop
def diamond(n):
    # Upper part of the diamond
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Input from user
rows = int(input("How high the diamond: "))
diamond(rows)