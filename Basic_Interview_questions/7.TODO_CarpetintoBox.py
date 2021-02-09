"""
Given a carpet of size a*b [length*breadth] and a box of size c*d,
one has to fit the carpet in box in minimum number of moves.
A move is to fold the carpet in half, either by length or breadth.

One can even turn the carpet by 90 degrees any number of times, won’t be counted as a move.

Example:
Box = 6 * 10
Carpet = 8 * 12

Output: No of moves = 1

Fold the carpet by breadth, 12/2
so now carpet is 6*8 and can fit fine.


Answer: min(⌈log2𝑎/𝑐⌉+⌈log2𝑏/𝑑⌉, ⌈log2𝑏/𝑐⌉+⌈log2𝑎/𝑑⌉)
"""