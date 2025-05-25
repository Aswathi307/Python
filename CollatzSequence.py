print("name : T P Aswathi,usn :1AY24AI109,sec:O")
def collatz_sequence(n):
    if n < 1:
        print("Please enter a positive integer.")
        return

    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # Final value

# Example usage
num = int(input("Enter a positive integer: "))
collatz_sequence(num)
