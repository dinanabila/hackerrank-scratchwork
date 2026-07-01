import os

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # my code starts here 'v')/
    if abs(y-z) < abs(x-z):
        return "Cat B"
    elif abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(x-z) == abs(y-z):
        return "Mouse C"
    # my code ends here '-')b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
