import math


def binarysearch(arr, item):
    midpoint = math.floor(len(arr)/2)
    if item == arr[midpoint]:
        print("{} exists ".format(item))
    elif item<arr[midpoint]:
        newarr=arr[:midpoint]
        print(newarr)
        binarysearch(newarr, item)

    elif item >arr[midpoint] and item<=arr[-1]:
        newarr=arr[midpoint:]
        print(newarr)
        binarysearch(newarr, item)

    else:
        print("{} does not exists".format(item))




if __name__ == '__main__':
    arr=[item for item in range(0,300)]

    binarysearch(arr, 275)
