# Development Log – The Torchbearer

**Student Name:** ____Matthew Long_____
**Student ID:** ___129916732_____

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/5/26]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

I will first try to code the problem, then check if I understand more on the question or vice versa, and then repeat in a consecutive iterative fashion. Though if I notice I can code a question as a mockup first I will do that in order to have some sort of notes on what I should do.

I expect part 6 to be most difficult as it requires understanding of pruning and I do not understand that one well. I think part 4 will be the most challenging as it will require me to fully understand the greediness of the algorithm to find a counterexample. 

I plan to test using the given test cases, specifically using solve as a sandbox for all the different functions I want to test and calling functions in solve.

---

## Entry 2 – [5/6/26]: [Djikstra's, select_sources, and General Part 1 and 2 answers]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

I changed the plan to be a bit more flexible. Answered Part 1 initially.

Initial answer to select_sources code. Initial answer to select_sources question.

Initial commits to run_djikstra(). Had to fix the float(inf) issue
Worked on more of djikstra's and seems to be stable.

Changes to select_sources to better fit README answer

---

## Entry 3 – [5/7/26]: [Finished precompute_distances()]

Answering distance storage(2b) in README.

Slight changes to the strategy and select_sources().

Started and finished untested precompute_distances().
Small bug in which formatting was off as each key was appended.
Fixed it with appending .items().

---

## Entry 4 – [5/8/26]: [Part 3 answers]

Comments for djikstra's. Edited readMe formatting. Edited 2c answer
Found and fixed bug in precompute_distances() with nodes not being restricted to ones in sources and not all of graphs.

Added descriptions to each of my entries, and made small changes to initial plan. Added new entry for next day.
Added answers for 3a,3b,3c.

Fixed formatting bug for precompute_distances(), Returns a dictionary instead of a list

---

## Entry 5 – [5/9/26]: [Part 4 answers]

Edits to headers. Initial part 4 answers typed in ReadME.
Initial Part 4 Example inserted as a table

---

## Entry 6 – [5/9/26]: [Initial part 5 code answer]

Skipped part 5 readMe to see if I could code _explore() and print_optimal_path well. 
Initial algorithm continues for too long. Changed graph 3 to check a certain edge case

---

## Entry 5 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
