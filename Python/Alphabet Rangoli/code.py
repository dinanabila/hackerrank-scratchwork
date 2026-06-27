def print_rangoli(size):
    all_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    alphabet = 27 * 2 * ['-']
    
    pattern = ""
    
    for i in range(size):
        alphabet[i] = all_alphabet[i]
    
    for i in range(size-1, -size, -1):
        if i < 0:
            i = abs(i)
        something = 0
        for j in range(1,2*size):
            if j < size:
                pattern += f"{alphabet[i+size-j]}-"
            elif j > size:
                something += 1
                j -= (something*2)
                pattern += f"-{alphabet[i+size-j]}"
            else:
                pattern += f"{alphabet[i+size-j]}"
        pattern += "\n"
        
    print(pattern)
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)