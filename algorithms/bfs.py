"""马走日（国际象棋骑士走法）最短路 BFS。

题意：n 行 m 列的棋盘，骑士从 (x, y) 出发，每步走"日"字，求每个格子到起点的
最少步数；走不到的格子记为 -1。行列下标在输入中从 1 开始，内部按 0 开始处理。

用法::

    python algorithms/bfs.py          # 不带输入时打印用法 + 3x3 起点(1,1) 的示例
    echo "4 4 1 1" | python algorithms/bfs.py

原始脚本（仓库根目录的 bfs.py）有 4 个致命 bug，修复点见各处 ``# 修复:`` 注释。
"""

from __future__ import annotations

import sys
from collections import deque

# 骑士的 8 种走法：(行偏移, 列偏移)
KNIGHT_MOVES: tuple[tuple[int, int], ...] = (
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
)

USAGE = "用法: echo \"n m x y\" | python algorithms/bfs.py   # 例: echo \"3 3 1 1\""


def knight_distances(rows: int, cols: int, start_row: int, start_col: int) -> list[list[int]]:
    """返回 rows x cols 棋盘上每个格子到起点 (start_row, start_col) 的最少步数。

    Args:
        rows: 棋盘行数，正整数（1-based 行号范围 1..rows）。
        cols: 棋盘列数，正整数。
        start_row: 起点行号，1-based。
        start_col: 起点列号，1-based。

    Returns:
        二维矩阵 dist，``dist[r][c]`` 为最少步数，-1 表示不可达。

    Raises:
        ValueError: rows/cols 非正，或起点落在棋盘外。

    Example:
        >>> knight_distances(3, 3, 1, 1)
        [[0, 3, 2], [3, -1, 1], [2, 1, 4]]
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("rows 与 cols 必须是正整数")
    if not (1 <= start_row <= rows and 1 <= start_col <= cols):
        raise ValueError(f"起点 ({start_row}, {start_col}) 超出 {rows}x{cols} 棋盘")

    # 修复: 原代码 `ans = [[-1 for _ in range(m)]-1 in range(n)]`
    #       先把 list 减 1（TypeError）、再拿结果和 range 做 in 判断，得到的是一个
    #       bool 而不是矩阵。正确做法是先建 n 行 m 列的 -1 矩阵。
    ans: list[list[int]] = [[-1] * cols for _ in range(rows)]

    # 修复: 原代码先 `x -= 1`，随后又写 `start_x = x - 1`，坐标被减了两次，
    #       3x3 起点 (1,1) 会算出 (-1,-1) 直接越界。这里只做一次 1-based -> 0-based。
    sr, sc = start_row - 1, start_col - 1
    ans[sr][sc] = 0
    queue: deque[tuple[int, int]] = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()
        for dr, dc in KNIGHT_MOVES:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and ans[nr][nc] == -1:
                ans[nr][nc] = ans[r][c] + 1
                queue.append((nr, nc))

    return ans


def format_board(distances: list[list[int]], width: int = 5) -> str:
    """把距离矩阵渲染成定宽文本，便于终端查看和测试断言。"""
    return "\n".join("".join(f"{value:<{width}}" for value in row) for row in distances)


def parse_case(text: str) -> tuple[int, int, int, int]:
    """解析 ``n m x y`` 四个整数。

    Raises:
        ValueError: 字段不足、无法转成整数或数量不对。
    """
    parts = text.split()
    # 修复: 原代码 `n,m,x,y = map(int,line)` 一旦字段多于/少于 4 个就抛裸 ValueError，
    #       且没有提示；这里要求恰好 4 个整数并给出统一的用法说明。
    if len(parts) != 4:
        raise ValueError(USAGE)
    try:
        rows, cols, start_row, start_col = (int(part) for part in parts)
    except ValueError as exc:
        raise ValueError(USAGE) from exc
    return rows, cols, start_row, start_col


def main() -> int:
    """从 stdin 读 ``n m x y``；没有输入时打印用法与示例，返回进程退出码。"""
    # 修复: 原代码用 input() 且只 catch ValueError，读到 EOF 会抛 EOFError 直接崩溃，
    #       现在整段一次性读入 stdin，空输入走示例分支。
    data = sys.stdin.read()
    if not data.strip():
        print(USAGE)
        print("\n3x3 棋盘、起点 (1,1) 的结果（-1 表示马走不到）:")
        print(format_board(knight_distances(3, 3, 1, 1)))
        return 0

    try:
        rows, cols, start_row, start_col = parse_case(data)
        board = knight_distances(rows, cols, start_row, start_col)
    except ValueError as exc:
        print(f"输入有误: {exc}", file=sys.stderr)
        return 2

    print(format_board(board))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
