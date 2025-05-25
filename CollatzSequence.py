print("name : T P Aswathi,usn :1AY24AI109,sec:O")
def collatz_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("Collatz sequence:")
    print(n, end=' ')
    while n != 1:
        if n % 2 == 0: 
            n = n // 2
        else:          
            n = 3 * n + 1
        print(n, end=' ')
    print() 
try:
    num = int(input("Enter a positive integer: "))
    collatz_sequence(num)
except ValueError:
    print("Invalid input. Please enter an integer.")
