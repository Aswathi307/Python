print("name : T P Aswathi,usn :1AY24AI109,sec:O")
def collatz_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("Collatz sequence:")
    print(n, end=' ')
    while n != 1:
        if n % 2 == 0:  # Even number
            n = n // 2
        else:           # Odd number
            n = 3 * n + 1
        print(n, end=' ')
    print()  # New line after the sequence

# Example usage:
try:
    num = int(input("Enter a positive integer: "))
    collatz_sequence(num)
except ValueError:
    print("Invalid input. Please enter an integer.")
