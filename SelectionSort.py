# def find_min_element(arr):
#     min = float("inf")
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#     return min

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_val = min(arr[i+1:])
        if arr[i] >= min_val:
            arr[arr.index(min_val)] = arr[i]
            arr[i] = min_val
    print(arr)

if __name__ == '__main__':
    elements = [78, 1,  12, 15, 8, 61, 53, 23, 27,13]
    print(selection_sort(elements))

