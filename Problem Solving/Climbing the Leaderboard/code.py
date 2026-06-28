import os
from bisect import bisect_left


# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player


def climbingLeaderboard(ranked, player):
    leaderboard_rank = len(ranked) * [1]
    
    for i in range(len(ranked)-1):
        if ranked[i+1] == ranked[i]:
            leaderboard_rank[i+1] = leaderboard_rank[i]
        elif ranked[i+1] < ranked[i]:
            leaderboard_rank[i+1] = leaderboard_rank[i] + 1
    
    player_rank = []
    
    ranked = ranked[::-1]
    leaderboard_rank = leaderboard_rank[::-1]
    
    for i in range(len(player)):
        pos = bisect_left(ranked, player[i])
        if pos >= len(ranked):
            player_rank.append(1)
        elif pos == 0:
            if player[i] == ranked[pos]:
                player_rank.append(leaderboard_rank[pos])
            elif player[i] < ranked[pos]:
                player_rank.append(leaderboard_rank[pos]+1)
        else:
            if player[i] >= ranked[pos - 1] and player[i] < ranked[pos]:
                player_rank.append(leaderboard_rank[pos-1])
            else:
                player_rank.append(leaderboard_rank[pos])
        
    return player_rank
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
