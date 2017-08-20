# Given a string with unique characters
def get_permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for idx in range(len(s)):
        c = s[idx]
        permutations = get_permutations(s[0:idx] + s[idx+1:len(s)])
        for permutation in permutations:
            result.append(c + permutation)

    return result

# Given a string with duplicate characters
def get_permutations_given_dups(s):
    if len(s) == 1:
        return {s}

    result = set()
    for idx in range(len(s)):
        c = s[idx]
        permutations = get_permutations(s[0:idx] + s[idx+1:len(s)])
        for permutation in permutations:
            result.add(c + permutation)

    return result


if __name__ == '__main__':

    s = "abcd"
    print(get_permutations(s))

    s = "aab"
    print(get_permutations(s))
    print(get_permutations_given_dups(s))
