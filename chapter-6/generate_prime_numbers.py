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

    print(generate_prime_numbers(100))
