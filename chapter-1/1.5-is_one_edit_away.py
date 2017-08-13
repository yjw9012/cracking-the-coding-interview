def is_one_edit_away(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        s1_walk = 0
        s2_walk = 0
        difference_found = False
        while s1_walk < len(s1):
            if s1[s1_walk] != s2[s2_walk]:
                if difference_found:
                    return False
                else:
                    difference_found = True
            s1_walk += 1
            s2_walk += 1
    else:
        s1_walk = 0
        s2_walk = 0
        difference_found = False
        while s1_walk < len(s1) and s2_walk < len(s2):
            if s1[s1_walk] != s2[s2_walk]:
                if difference_found:
                    return False
                else:
                    difference_found = True
                    if len(s1) > len(s2):
                        s1_walk += 1
                    else:
                        s2_walk += 1
                    continue
            s1_walk += 1
            s2_walk += 1

    return True

s1 = "pale"
s2 = "ple"
assert is_one_edit_away(s1, s2)

s1 = "pales"
s2 = "pale"
assert is_one_edit_away(s1, s2)

s1 = "pale"
s2 = "bale"
assert is_one_edit_away(s1, s2)

s1 = "pale"
s2 = "bake"
assert not is_one_edit_away(s1, s2)
