# ass3.py
# finding prime numbers within other numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Only check up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Input: Range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and display prime numbers in the range
print(f"Prime numbers between {start} and {end}:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number, end=" ")
