def is_perm_of_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True

    dict = {}
    for char in s:
        dict[char] = dict.get(char, 0) + 1

    odd_count_exist = False
    for char, count in dict.items():
        if count % 2 != 0:
            if odd_count_exist:
                return False
            else:
                odd_count_exist = True

    return True

# If we assume s consists of a-z characters:
def is_perm_of_palindrome_bit(s):
    if len(s) == 0 or len(s) == 1:
        return True

    result = 0
    for char in s:
        result ^= get_bit_representation(char)

    return result == 0 or result & result - 1 == 0

def get_bit_representation(char):
    return 1 << ord(char)-ord('a')



s = "aabbccdd"
print(is_perm_of_palindrome(s))

s = "aabbccdde"
print(is_perm_of_palindrome(s))

s = "abcde"
print(is_perm_of_palindrome(s))

s = "aabbccdd"
print(is_perm_of_palindrome_bit(s))

s = "aabbccdde"
print(is_perm_of_palindrome_bit(s))

s = "abcde"
print(is_perm_of_palindrome_bit(s))
