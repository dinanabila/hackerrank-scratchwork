def getMinimumCost(k, c):
    cost_multiplier = 0
    num_purchase = math.ceil(len(c)/k)
    cost_list = []
    flower_cost_purcased = 0
    
    for _ in range(num_purchase):
        if k <= len(c):
            for _ in range(k):
                flower_cost_purcased = max(c)
                cost_list.append((cost_multiplier+1)*flower_cost_purcased)
                c.remove(max(c))
        else:
            for _ in range(len(c)):
                flower_cost_purcased = max(c)
                cost_list.append((cost_multiplier+1)*flower_cost_purcased)
                c.remove(max(c))
        cost_multiplier+=1
    return sum(cost_list)
