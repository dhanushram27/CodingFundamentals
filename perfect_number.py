def is_perfect_number(n):
    divisors = [i for i in range(1,n) if n % i == 0]
    return sum(divisors) == n

n = int(input("Enter the Number : "))

if is_perfect_number(n):
    print("Its a perfect Number")
else:
    print("Its not a perfect Number")
