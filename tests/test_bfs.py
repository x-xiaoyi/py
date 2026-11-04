"""马走日 BFS 的单元测试 —— 全部用可手算的小棋盘。"""

import pytest

from algorithms.bfs import format_board, knight_distances, parse_case


def test_knight_distances_3x3_from_corner():
    """3x3 起点 (1,1)：中心格马永远走不到，距离矩阵可手工推出。"""
    # 手动推导（1-based 行列）：
    # 0 步: (1,1)
    # 1 步: (2,3),(3,2)
    # 2 步: (1,3),(3,1)
    # 3 步: (1,2),(2,1)
    # 4 步: (3,3)
    # 中心 (2,2) 不可达 -> -1
    expected = [
        [0, 3, 2],
        [3, -1, 1],
        [2, 1, 4],
    ]
    assert knight_distances(3, 3, 1, 1) == expected


def test_knight_distances_1x1_is_zero():
    """1x1 棋盘上起点就是终点。"""
    assert knight_distances(1, 1, 1, 1) == [[0]]


def test_knight_distances_single_row_all_unreachable():
    """1x3 一行：马一步都走不了，除起点外全是 -1。"""
    assert knight_distances(1, 3, 1, 2) == [[-1, 0, -1]]


def test_knight_distances_is_symmetric_in_time():
    """距离矩阵关于起点对称：从 (1,1) 到 (3,3) 的距离等于从 (3,3) 到 (1,1)。"""
    a = knight_distances(3, 3, 1, 1)[2][2]
    b = knight_distances(3, 3, 3, 3)[0][0]
    assert a == b == 4


@pytest.mark.parametrize("rows,cols", [(0, 3), (3, 0), (-1, 3)])
def test_knight_distances_rejects_non_positive_size(rows, cols):
    """行列数必须为正。"""
    with pytest.raises(ValueError, match="正整数"):
        knight_distances(rows, cols, 1, 1)


@pytest.mark.parametrize("x,y", [(0, 1), (1, 0), (4, 1), (1, 4)])
def test_knight_distances_rejects_start_out_of_board(x, y):
    """起点必须在棋盘内（1-based）。"""
    with pytest.raises(ValueError, match="超出"):
        knight_distances(3, 3, x, y)


def test_format_board_uses_fixed_width():
    """文本输出用于人工核对，列宽可调。"""
    text = format_board([[0, 1], [-1, 2]], width=3)
    assert text == "0  1  \n-1 2  "


@pytest.mark.parametrize(
    "text",
    ["", "3 3", "3 3 1", "a b c d", "3 3 1 1 9"],
)
def test_parse_case_rejects_bad_input(text):
    """字段不足 / 非整数 / 空输入都走 ValueError 而不是崩溃。"""
    with pytest.raises(ValueError):
        parse_case(text)


def test_parse_case_reads_four_ints():
    assert parse_case("4 5 2 3") == (4, 5, 2, 3)
