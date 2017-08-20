def count_triple_step(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_triple_step(n-1) + count_triple_step(n-2) + count_triple_step(n-3)

def count_triple_step_better(n, memory):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        if memory[n] < 1:
            memory[n] = count_triple_step(n-1) + count_triple_step(n-2) + count_triple_step(n-3)
        return memory[n]

if __name__ == '__main__':

    assert count_triple_step(1) == 1
    assert count_triple_step(2) == 2
    assert count_triple_step(3) == 4
    assert count_triple_step(5) == 13

    assert count_triple_step_better(1, [0] * (1 + 1)) == 1
    assert count_triple_step_better(2, [0] * (2 + 1)) == 2
    assert count_triple_step_better(3, [0] * (3 + 1)) == 4
    assert count_triple_step_better(5, [0] * (5 + 1)) == 13
