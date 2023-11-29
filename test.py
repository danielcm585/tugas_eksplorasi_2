import random
import greedy
import branch_and_bound
from decorator import *
from functools import reduce

def generate(size):
    costs = [ 
        random.randint(1,1000000000) 
        for i in range(size)
    ]
    subsets = [
        set([ 
            random.randint(1,size) 
            for i in range(random.randint(1,size)) 
        ])
        for i in range(size-1)
    ]
    
    mx_val = max([ 
        max(subset) 
        for subset in subsets 
    ])
    set_val = reduce(
        lambda a, b: a.union(b), 
        subsets
    )

    res = set([ 
        i 
        for i in range(1,size+1)
        if i not in set_val
    ])
    subsets.append(res)

    universe = len(subsets)
    
    return universe, subsets, costs

@benchmark
def solve_greedy(universe, subsets, costs):
    return greedy.set_cover(universe, subsets, costs)

@benchmark
def solve_bb(universe, subsets, costs):
    return branch_and_bound.BB(universe, subsets, costs)

for size in [20, 200, 2000]:
    print(f'Size = {size}')
    universe, subsets, costs = generate(size)
    cover, cost = solve_greedy(universe, subsets, costs)
    bestCost, bestSubset = solve_bb(universe, subsets, costs)
    print(f'> Greedy           : {cost}')
    print(f'> Branch and Bound : {bestCost}')
    print()
