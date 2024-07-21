def fibs(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibSequence = [0, 1]
    for i in range(2, n):
        fibSequence.append(fibSequence[-1] + fibSequence[-2])

    return fibSequence


print(fibs(8))
