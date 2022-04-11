# we have 2 sorted array
# [17, 21, 29, 38] and [4, 9, 25, 32]
# []
def merge_two_sorted_array(list1, list2):
    i = 0
    j = 0
    final_ans = []
    while i < len(list1) and j < len(list2):
        if list2[j] <= list1[i]:
            final_ans.append(list2[j])
            j += 1
        elif list1[i] < list2[j]:
            final_ans.append(list1[i])
            i += 1
    if j == len(list2):
        final_ans += (list1[i:])
    else:
        final_ans += (list2[j:])
    return final_ans


# break the list down to single variable and then use recursive to merge it
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    # print(merge_two_sorted_array(left, right))
    return merge_two_sorted_array(left, right)


if __name__ == '__main__':
    # print(merge_two_sorted_array([17, 21, 29, 38], [4, 9, 25,  32]))
    # print(merge_two_sorted_array([17, 21, 29, 30, 38, 39, 41, 42], [1, 2, 4, 9, 10, 15, 25, 26, 32, 40, 43]))
    print(merge_sort([21, 38, 29, 17, 4, 25, 32, 9]))
