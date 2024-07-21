def mergeSort(array):
    if len(array) <= 1:
        return array

    def merge(left, right):
        result = []
        leftIndex, rightIndex = 0, 0

        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                result.append(left[leftIndex])
                leftIndex += 1
            else:
                result.append(right[rightIndex])
                rightIndex += 1

        result.extend(left[leftIndex:])
        result.extend(right[rightIndex:])
        return result

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)


print(mergeSort([3, 2, 1, 13, 8, 5, 0, 1]))
print(mergeSort([105, 79, 100, 110]))
