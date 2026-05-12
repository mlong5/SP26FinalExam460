"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___Matthew Long_____
Student ID:   _____129916732_________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    ans = 'A single shortest path run from S is not sufficient as it cannot decide which path to T uses the least fuel. ' \
    'It cannot even decide where T is to stop, if it is just a path to the shortest nodes. ' \
    'The structural decision of the most efficient path to T still remains as we must compare which path has the least fuel.' \
    'Since there are multiple paths that could end in T, we must find the most optimal path by searching through every path in orders, not just a single computation.'

    return ans


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = list()
    sources.append(spawn)
    sources.extend(relics) #exit_node is ommitted but may still need to be included?
    return sources 


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
    """
    value = {node1: float('inf') for node1 in graph}
    value[source] = 0

    pq = []
    heapq.heappush(pq, (0, source))
    
    while pq:
        (dist, node) = heapq.heappop(pq)

        if(dist > value[node]): #if dist from source greater than curr, unhelpful don't use
            continue

        for (nextNode,cost) in graph[node]: #if neighbor is more minimal, push onto min heap
            if value[node] + cost < value[nextNode]:
                value[nextNode] = value[node] + cost
                heapq.heappush(pq, (value[nextNode], nextNode))
    return value


#access pq and change the pq priority if needed




def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    
    all_paths = {}
    all_paths.update({spawn : {}})
    for node2 in graph:
        if(node2 in relics):
            all_paths.update({node2 : {}})
        '''lis2 = graph[node2]
        for item in lis2:
            if item[0] == spawn:
                graph[node2].remove(item)'''
    #all_paths = {node2: [] for node2 in graph and node2 in relics}
    valid_sources = select_sources(spawn,relics,exit_node) #list with each of the sources, no exit_node
    for source in valid_sources:
        curr_path = run_dijkstra(graph,source)
        if(curr_path[source] == 0):
            del curr_path[source]
        all_paths[source].update(curr_path.items()) #all_paths may return the intermediate nodes, maybe need to change, maybe not
    return all_paths




# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "TODO"


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """

    #print(dist_table['S'].keys())

    rel_order = []
    #maybe instead make it an array that uses a subset every time
    rel_rem = set(relics)
    best = [spawn]
    cost = 0

   
    
    rowSum = 0
    mini = float('inf')
    for src in dist_table:
        #print(dist_table[src])
        reduceR = min(dist_table[src].values())
        #print(reduceR)
        rowSum += reduceR
        for dist in dist_table[src]:
            dist_table[src][dist] -= reduceR
    
    
    colSum = 0
    mini2 = float('inf')
    for j, node in enumerate(list(dist_table.values())):
        print(node)
        #print(node)
        #mini2 = float('inf')
        for i,src2 in enumerate(list(dist_table.keys())):
            print(src2)
            
    #print(colSum)
        
            




    #print(rowSum)
    #print('here2')
        
            
    

    _explore(dist_table, spawn, rel_rem, rel_order, cost, exit_node, best)
   
    if(rel_order and rel_order[-1] == '@'):
        rel_order.pop(-1)
        rel_order.clear()
    
    #rel_rem = set(relics)
    #if(best and best[-1] != exit_node):
        #_explore(dist_table, best[-1], rel_rem, rel_order, cost, exit_node, best)
    #print(best)
    
    for i in range(0, len(best)-2):
       if(best[i] == best[i+1]):
           best.pop(i)

    #have to find cost outside i guess
    best.extend(exit_node)

    print(best)
    

    cost2 = 0
    v1 = spawn
    for v2 in best:
        if(v2 != spawn):
            cost2 += dist_table[v1][v2]
            v1 = v2
            if(v1 == exit_node):
                break
    #print(cost2)
        
def bound(cost, current_list):
    if(cost == 0):
        cost = float('inf')
        return cost
    for key in current_list:
        if current_list[key] < cost:
            cost = current_list[key]
            return cost



def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    #visited = []
    #visited.append(current_loc)

    

    
    if( not relics_remaining): #check if current path is too long
        #print(relics_visited_order)
        best.extend(relics_visited_order)
        #relics_visited_order.append('@')
        cost_so_far = cost_so_far + dist_table[current_loc][exit_node]
        #print(cost_so_far)
        return 
    if( dist_table[current_loc][exit_node] != float('inf') and cost_so_far >= 3):
        print(bound(cost_so_far, dist_table[current_loc]))
        return 
    
    for v in dist_table[current_loc]:
        print()
        if (v in relics_remaining and v not in relics_visited_order and dist_table[current_loc][v] != float('inf')):
            #heapq.heappush(relics_visited_order,(dist_table[current_loc][v],v))

            relics_remaining.remove(v) 
            relics_visited_order.append(v)
            cost_so_far += dist_table[current_loc][v]

            print(relics_visited_order)

            _explore(dist_table, v, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)

            if relics_visited_order[-1] == '@':
                return
            #heapq.heappop(relics_visited_order)
            relics_remaining.add(v)
            relics_visited_order.remove(v)
            cost_so_far -= dist_table[current_loc][v]



#maybe relics visisted order is a min heap


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_tab = precompute_distances(graph,spawn,relics,exit_node)
    print(dist_tab)
    print(find_optimal_route(dist_tab,spawn,relics,exit_node)) 


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")


    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R',1)],
        'R': [ ('T', 1), ('R2',1)],
        'R2': [('R',1)],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R','R2'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
    'S': [('X', 1)],
    'X': [('R1', 2), ('R2', 5)],
    'R1': [('Y', 1)],
    'Y': [('R2', 1)],
    'R2': [('T', 1)],
    'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
        f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
