def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    print(f'The union is : {get_union(list1, list2)}')
    print(f'The intersection is : {get_intersection(list1, list2)}')


def get_union(list1, list2):
    union = []
    for i in list1:
        if i not in union:
            union.append(i)
    for i in list2:
        if i not in union:
            union.append(i)
    return union


def get_intersection(list1, list2):
    intersection = []
    for i in list1:
        if i in list2:
            intersection.append(i)
    return intersection


main()
