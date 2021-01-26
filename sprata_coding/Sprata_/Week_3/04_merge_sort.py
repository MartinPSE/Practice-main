# 병합 정렬 - merge
# 합치면서 정렬 합시다!

A = [1, 2, 3, 5]
B = [4, 6, 7, 8]


def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            array_c.append(array2[array1_index])
            array1_index += 1
    return array_c


print(merge(A, B))
