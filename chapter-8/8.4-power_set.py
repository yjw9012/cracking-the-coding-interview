def power_set(s):
    if len(s) == 0:
        return [[]]

    num = s.pop()
    subresult = power_set(s)
    other_result = [lis + [num] for lis in subresult]

    return subresult + other_result


if __name__ == '__main__':

    s = [1,2,3]
    print(power_set(s))
