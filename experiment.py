import random
import greedy
import branch_and_bound
from decorator import *
from functools import reduce

def generate(universe):
    costs = [ 
        random.randint(1,1000) 
        for i in range(universe)
    ]
    subsets = [
        set([ 
            random.randint(1,universe) 
            for i in range(random.randint(1,universe)) 
        ])
        for i in range(random.randint(10,20))
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
        for i in range(1,universe+1)
        if i not in set_val
    ])
    subsets.append(res)
    
    return universe, subsets, costs

@benchmark
def solve_greedy(universe, subsets, costs):
    return greedy.main(universe, subsets, costs)

@benchmark
def solve_bb(universe, subsets, costs):
    return branch_and_bound.main(universe, subsets, costs)

for size in [20, 200, 2000]:
    print(f'Size = {size}')
    universe, subsets, costs = generate(size)
    greedy_cost = solve_greedy(universe, subsets, costs)
    bb_cost = solve_bb(universe, subsets, costs)
    print(f'> Greedy           : {greedy_cost}')
    print(f'> Branch and Bound : {bb_cost}')
    print()
