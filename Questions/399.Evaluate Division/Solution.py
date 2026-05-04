# I'll use a hash map to store the relationship for those pairs
from collections import defaultdict
def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    pairs = defaultdict(tuple)
    
    for a, b, c in zip(equations, values):
        pairs[a] = (b, c)
        pairs[b] = (a, 1 / c)

    ret = []

    def dfs(cur: str, next: str, num: int) -> bool:
        if cur == next:
            return 



        


    

    
