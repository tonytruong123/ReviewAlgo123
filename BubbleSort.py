# The reason why it is called bubble sort is the bubble in the water
# will go from the button to the surface of the warer

# [38, 9, 28, 7, 2, 15, 28]
# For bubble sort, we gonna start with the first 2 numbers: 38, 9
# since 38 > 9 so switch
# => [9, 38, 28, 7, 2, 15, 28]
# keep doing the same thing until the whole list is sorted

def bubble_sort(list1):
    list2 = list1[:]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list2) - 1):
            if list2[i] > list2[i + 1]:
                sorted = False
                list2[i], list2[i + 1] = list2[i + 1], list2[i]

    return list2


if __name__ == '__main__':
    list1 = [38, 9, 28, 7, 2, 15, 28]
    ans_list = bubble_sort(list1)

    print(f"Original list {list1} and sorted list {ans_list}")
