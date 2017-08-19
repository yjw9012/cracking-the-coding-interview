def generate_prime_numbers(n):
    flags = [True for i in range(n+1)]
    flags[0] = flags[1] = False     # 0 and 1 are not prime numbers

    num = 2
    while num <= n // 2:
        for i in range(num*2, n+1, num):
            flags[i] = False
        num = find_next_prime(flags, num, n)

    return [i for i in range(len(flags)) if flags[i]]

def find_next_prime(flags, num, n):
    next_num = num+1
    while next_num <= n and not flags[next_num]:
        next_num += 1
    return next_num


if __name__ == '__main__':

<<<<<<< HEAD
    prime_numbers = generate_prime_numbers(100)
    prime_numbers_up_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(len(prime_numbers_up_to_100)):
        assert prime_numbers[i] == prime_numbers_up_to_100[i]
=======
    print(generate_prime_numbers(100))
>>>>>>> 777c27796fb79d817cd7ba812933cf9767a91363
