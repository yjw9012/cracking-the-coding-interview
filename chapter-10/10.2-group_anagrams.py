def group_anagrams(arr):

    anagram_dict = {}
    for s in arr:
        sorted_s = "".join(sorted(s))

        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]

    result = []
    for sorted_form, lis_anagrams in anagram_dict.items():
        result += lis_anagrams

    return result


if __name__ == "__main__":

    lis = ["bac", "cb", "bca", "bc", "abc", "abcd", "dbca"]
    print(group_anagrams(lis))
