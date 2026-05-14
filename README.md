# The Torchbearer

**Student Name:** ____Matthew Long__
**Student ID:** ___129916732______
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  - A single shortest path run from S is not sufficient as it cannot decide which path to T uses the least fuel.
  - It cannot even decide where T is to stop, if it is just a path to the shortest nodes

- **What decision remains after all inter-location costs are known:**
  - The structural decision of the most efficient path to T still remains as we must compare which path has the least fuel.

- **Why this requires a search over orders (one sentence):**
  - Since there are multiple paths that could end in T, we must find the most optimal path by searching through every path in orders, not just a single computation.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Starting or S | We must always record the distance from the start node, since we always use it  |
| Must Visit or Relic | Since each Relic room must be visited, we must always record the distance |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | dictionary |
| What the keys represent | valid nodes |
| What the values represent | distances from source |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Python dictionaries use Hash Maps|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** |M|+1 where M is the set of Relic Rooms, and the + 1 is for the source S.
- **Cost per run:** Djikstra’s has O(E log V) since all of the Graph(V,E) must be traversed to minimize distance(even intermediate rooms)
- **Total complexity:** Thus, combined we can say O(|M| * E log V)
- **Justification (one line):** Since Djikstra’s is nested in a loop that runs about |M| times, we multiply the |M| times E log V for each Djikstra’s applied to the set M to get O(|M| * E log V)

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  - Only the most minimal, shortest distance from the current source has been recorded in dist[v]
  - Up-to-date with the smallest distances for vertexes up to v


- **For nodes not yet finalized (not in S):**
 - The distance recorded for nodes from the current source may not yet be the shortest distance
 - May be infinity, or unreachable, and thus undiscovered
 - May be just larger than vertex v
 - The distance, if recorded, comes from a source that is already in S


### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  - All distances but x to itself are undiscovered and marked with infinity as distance
  - The start node is most minimal at 0, so the first invariant for vertices in S holds
  - For all other vertices not in S, they are undiscovered and not yet in dist[u]
  - There are no discovered distances not in S, so the second invariant holds by nullity


- **Maintenance : why finalizing the min-dist node is always correct:**
  - For node u not in S, on an iteration, Graph(V,E) has nonnegative edge weights
  - Thus, distance to u can be minimized by comparing the current nonnegative distance from x to a lesser nonnegative distance of a neighboring path
  - For the next iteration, the old node u is now in the set S, and treated like v, and is minimal
  - All other nodes have not yet been discovered so both invariants hold

- **Termination : what the invariant guarantees when the algorithm ends:**
  - Since pq is now empty, assume invariants hold for all past nodes. 
  - Every v in S has been minimized
  - Every vertex has been discovered
  - If there is a vertex u not in S, then it is not minimal compared to v, or is unreachable and marked as infinity.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

- To decide the best route through all relic rooms in set M and node T, we need the most minimal distances to each of the rooms and T.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 1   | 4   | inf | --  |
| B         | 0   | 2   | inf | 1   |
| C         | inf | --  | 6   | 2   |
| D         | 1   | inf | inf | 4   |

- **The failure mode:** 
  - Greedy fails when it chooses S->B instead of S->C since it focuses on immediate local minimums
- **Counter-example setup:** 
  - Assume we use the graph above, and we choose the immediate local minimum of cost_so_far.
  - We choose the immediate minimum relic room from our current source that we have not already visited in our set.
- **What greedy picks:** 
  - S -> B -> C -> D -> T, total fuel = 1 + 2 + 6 + 4 = 13
- **What optimal picks:**
  - S -> C -> D -> B -> T, total fuel = 4 + 6 + 1 + 1 = 12
- **Why greedy loses:**
  - Greedy looks at the most immediate local minimum which is S-> B = 1
  - Greedy misses out on the path starting with S->C = 4 
  - The S->C path has a lesser global minimum in the end

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The optimal algorithm must explore each relic room order of set M to find the most minimal combination.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | cur_location | int | each relic room source(has its own path) that should be recursively explored with _explore |
| Relics already collected | relics_visited_order | list | an ordered list of the relic rooms of an optimal path(pop on relics queue) |
| Fuel cost so far | cost_so_far | int | Has the cost of the current relic room path and checks if it is minimal to become optimal cost|

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1) set check|
| Operation: mark a relic as collected | Time complexity: O(1) set removal |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) set addition |
| Why this structure fits | The set uses hashing to have short removal and addition which I use for indicating whether or not I want to backtrack over certain pathing attempts|

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:**
  - Worst-case is O(ck) with c being a constant for the amount of branches and k = |M| 
- **Why:** 
  - There could be more than one state branch of a viable path which requires more than one exploration of the |M| nodes in the relic room set of M.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- https://www.youtube.com/watch?v=1FEP_sNb62k
- https://www.geeksforgeeks.org/python/time-complexities-of-python-dictionary/
- https://www.w3schools.com/PYTHON/ref_list_extend.asp
