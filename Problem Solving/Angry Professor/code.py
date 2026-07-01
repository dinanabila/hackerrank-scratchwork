import os

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a

def angryProfessor(k, a):
    # my code starts here 'v')/
    on_time_num = 0
    for i in range(n):
        if a[i] <= 0:
            on_time_num += 1
    if on_time_num >= k:
        return "NO"
    else:
        return "YES"
    # my code ends here '-')b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
