"""
Problem: Get a list of prime number till given number
steps:
1. create a bool array of size n+1
2. Run a loop from p=2 till p*p <= N
    mark all multiple of 2 from true to false (from p*p to n+1)
    until condition fail

    Note: why loop start from p*p
    let say for 4, 4*4 bcoz 4*2 4*3 is already covered as part of 2*4, 3*2

"""

def sieve_of_eratosthenes(num):
    prime_numbers = [True] * (num+1)
    p = 2
    while p*p <= num:
        for i in range(p*p, num+1, p):
            prime_numbers[i] = False
            if not prime_numbers[num]:
                print("Not prime number")
                return
        p += 1
    print("Prime number")
    all_prime_number = []
    for i in range(2, num):
        if prime_numbers[i]:
            all_prime_number.append(i)
    print(all_prime_number)

sieve_of_eratosthenes(11)