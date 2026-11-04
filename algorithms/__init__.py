"""算法练习：BFS / DFS / 全排列 / 枚举 / 动态规划。"""

from .bfs import knight_distances
from .dfs import permutations
from .dynamic_programming import climb_stairs
from .enumeration import count_even_digit_sum, digit_sum
from .exhaustive_enumeration import is_palindrome_date, next_palindrome_date
from .permutation import format_permutation_table

__all__ = [
    "climb_stairs",
    "count_even_digit_sum",
    "digit_sum",
    "format_permutation_table",
    "is_palindrome_date",
    "knight_distances",
    "next_palindrome_date",
    "permutations",
]
