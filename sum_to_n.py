'''
Sum of 1 to n integers : n(n+1)/2
'''

def sum_of_numbers(n):
    return sum(range(1, n + 1))

def main():
    n = int(input("Enter the number n: "))
    total = sum_of_numbers(n)
    print(f"The sum of numbers from 1 to {n} is: {total}")

if __name__ == "__main__":
    main()
