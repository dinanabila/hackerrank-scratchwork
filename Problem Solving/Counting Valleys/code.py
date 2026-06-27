def countingValleys(steps, path):
    something = []
    num_u = 0
    num_d = 0
    num_valleys = 0
    
    for i in range(steps):
        if path[i] == 'U':
            num_u += 1
        elif path[i] == 'D':
            num_d += 1
        
        something.append(path[i])
        
        if num_u == num_d and something[0] == 'D' and something[len(something)-1] == 'U':
            num_valleys += 1
            something.clear()
        elif num_u == num_d and something[0] == 'U' and something[len(something)-1] == 'D':
            something.clear()
            
    return num_valleys