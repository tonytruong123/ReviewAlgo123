# The idea is that we have an unsorted list [7,9,2,27,18]
# We want to insert 11 into the middle such that
# the list become [7,9,2,11,27,18]
# the right numbers of 11 will be numbers less than 11
# the left numbers of 11 will be numbers greater than 11
# => repeat the same process for the left and right by choosing a number and putting it in the middle

# => this method is called Partition
# we have: Hoare Partition and Lomuto Partition
def swap(a,b,arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]


def partition(elements, start, end):
    pivot = start
    # we need to add start < len(elements) because if the right numbers of the pivot all smaller than it
    # => it will keep incrementing and at one point it will be out of range
    while end > start and start < len(elements):
        if elements[start] <= elements[pivot]:
            start += 1
        if elements[end] > elements[pivot]:
            end -= 1
        elif elements[start] > elements[pivot] >= elements[end]:
            elements[start], elements[end] = elements[end], elements[start]
    elements[end], elements[pivot] = elements[pivot], elements[end]
    return end


def quick_sort(elements, start, end):
    # how long should we do this process.
    # say when we only have 1 element that we need to sort => that's when we need to stop
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [11, 9, 12, 3, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
