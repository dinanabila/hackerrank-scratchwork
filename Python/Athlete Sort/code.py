if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    # my code start here 'v')/
    some_dict = {}
    
    for i in range(n):
        some_dict[i] = arr[i][k]
    
    sorted_attr = dict(sorted(some_dict.items(), key=lambda x: x[1]))

    for i in sorted_attr.keys():
        print(*arr[i])
    