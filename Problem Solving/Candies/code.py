def candies(n, arr):
    # Write your code here
    
    # potongan kode yang dikomen ini, walau bisa dipakai untuk skala kecil, 
    # tapi bikin test 11 gagal: Time limit exceeded (kalau input n nya sangat-sangat besar)
    # num_lower_after = []
    # counter = 0
    # for i in range(n):
    #     for j in range(i, n - 1):
    #         if arr[j + 1] < arr[j]:
    #             counter += 1
    #         else:
    #             break     
    #     num_lower_after.append(counter)
    #     counter = 0

    # harusnya gini biar ga 'berat'
    # start code yang lolos test time limit
    num_lower_after = [0] * n

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            num_lower_after[i] = num_lower_after[i + 1] + 1
    # end code yang lolos test time limit teehee

    num_candies = []
    for i in range(n):
        if i == 0:
            if arr[i] <= arr[i+1]:
                num_candies.append(1)
            elif arr[i] > arr[i+1]:
                num_candies.append(1+num_lower_after[i])
        elif i == (n-1):
            if arr[i] <= arr[i-1]:
                num_candies.append(1)
            elif arr[i] > arr[i-1]:
                num_candies.append(num_candies[i-1]+1)
        else:
            if arr[i] > arr[i+1]:
                if arr[i-1] < arr[i] and num_lower_after[i] < num_candies[i-1]:
                    num_candies.append(1 + num_candies[i-1])
                else:
                    num_candies.append(1 + num_lower_after[i])
            elif arr[i] <= arr[i+1]:
                if arr[i-1] < arr[i]:
                    num_candies.append(num_candies[i-1]+1)
                else:
                    num_candies.append(1)
        
    return sum(num_candies)
