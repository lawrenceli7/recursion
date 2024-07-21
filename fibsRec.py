def fibsRec(n):
    def helper(count, a=0, b=1):
        if count == 0:
            return []
        if count == 1:
            return [a]
        return [a] + helper(count - 1, b, a + b)

    return helper(n)


print(fibsRec(8))
