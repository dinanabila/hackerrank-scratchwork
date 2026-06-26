def migratoryBirds(arr):
    # Write your code here
    num_birds_type = 5*[0]
    
    for i in range(len(arr)):
        if arr[i] == 1:
            num_birds_type[0]+=1
        elif arr[i] == 2:
            num_birds_type[1]+=1
        elif arr[i] == 3:
            num_birds_type[2]+=1
        elif arr[i] == 4:
            num_birds_type[3]+=1
        elif arr[i] == 5:
            num_birds_type[4]+=1

    return num_birds_type.index(max(num_birds_type)) + 1
