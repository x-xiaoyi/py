![Python](https://img.shields.io/badge/python-3.10%2B-1f6feb)
![Deps](https://img.shields.io/badge/runtime%20deps-none-8957e5)
![Tests](https://img.shields.io/badge/pytest-122%20passed-success)
![License](https://img.shields.io/badge/license-MIT-blue)

# py —— Python 学习 / 算法练习合集

Python 学习 / 算法练习合集。仓库里是学习过程中写下的算法题、枚举题和面向对象练习，
现在统一整理成「按主题分目录 + 统一英文 snake_case 文件名 + pytest 覆盖」的形态。

- 纯标准库实现，**运行时不依赖任何第三方包**；
- 每个脚本都能单独 `python <file>` 跑，交互式脚本支持 stdin 输入，也支持不带输入时打印示例；
- 所有可测函数都在 `tests/` 下有单测，含 0 / 1 / 负数 / 空输入等边界。

## 环境要求

| 项目 | 要求 |
| --- | --- |
| Python | 3.10+（用到了 `list[int]`、`X \| None` 等写法；本机验证版本 3.14.2） |
| 运行时依赖 | 无（纯标准库） |
| 测试依赖 | pytest（仅测试用）：`python -m pip install pytest` |

## 目录结构

```
py/
├── algorithms/                 # 算法题
│   ├── __init__.py
│   ├── bfs.py                  # 马走日最短路（BFS，返回每格到起点的最少步数）
│   ├── dfs.py                  # 全排列（DFS 回溯，返回 list[list[int]]）
│   ├── permutation.py          # 全排列的定宽表格输出（算法复用 dfs.py）
│   ├── enumeration.py          # 枚举：1..2026 中各位数字之和为偶数的个数
│   ├── exhaustive_enumeration.py  # 穷举：下一个回文日期（yyyymmdd）
│   └── dynamic_programming.py  # 爬楼梯（每步 1/2/3 阶，滚动数组 DP）
├── basics/
│   ├── __init__.py
│   └── narcissistic.py         # 自恋数（水仙花数）判定与枚举
├── oop/
│   ├── __init__.py
│   ├── student.py              # 学生数据模型（原 le.py）
│   ├── student_management.py   # 学生名册：增/查/删/列（原 studentManagement.py + leiceshi.py）
│   └── inheritance_demo.py     # 继承与多态：Device / Smartphone / Smartwatch / Tablet
├── tests/                      # pytest 用例，10 个文件 122 个用例
├── pytest.ini                  # testpaths=tests, pythonpath=.
└── README.md
```

### 每个模块一句话

| 模块 | 说明 |
| --- | --- |
| `algorithms/bfs.py` | 骑士（马走日）在 n×m 棋盘上的最短路 BFS，输出距离矩阵，走不到为 -1 |
| `algorithms/dfs.py` | 用「选数—标记—回溯」的 DFS 生成 `1..n` 全排列 |
| `algorithms/permutation.py` | 同一套全排列算法的定宽（5 列）表格输出，对应原来 `permutation.py` 的打印样式 |
| `algorithms/enumeration.py` | 穷举统计 `1..limit` 中各位数字之和为偶数的整数个数（默认 2026，答案 1013） |
| `algorithms/exhaustive_enumeration.py` | 逐日穷举，找指定日期之后的第一个回文日期（`20200202` → `20211202`） |
| `algorithms/dynamic_programming.py` | 爬楼梯：`f(n)=f(n-1)+f(n-2)+f(n-3)`，`f(0)=1`，O(1) 空间 |
| `basics/narcissistic.py` | 自恋数判定（按位数取幂）与区间枚举 |
| `oop/student.py` | `Student` 数据类：姓名/年龄/成绩，带年龄校验 |
| `oop/student_management.py` | 内存版学生名册，含增删查列与可运行的演示流程 |
| `oop/inheritance_demo.py` | 继承、私有属性、方法重写与多态的演示 |

## 旧文件名 → 新文件名对照表

按拼音/中文记文件名的同学看这张表：

| 旧文件（仓库根目录） | 新位置 | 处理方式 |
| --- | --- | --- |
| `判断水仙花数.py` | `basics/narcissistic.py` | **合并**：初版实现（有 2 个致命 bug），逻辑并入并修正 |
| `shuixianhua.py` | `basics/narcissistic.py` | **合并**：正确版本（用 temp 暂存原值），作为合并后的基准实现 |
| `ceshi.py` | `basics/narcissistic.py` 的 `main()` | **合并**：只有 3 行的 `print(shuixianhua(153))` 验证脚本 |
| `测试.py` | — | **删除**：0 字节空文件 |
| `bfs.py` | `algorithms/bfs.py` | git mv，修 4 处 bug |
| `dfs.py` | `algorithms/dfs.py` | git mv，抽出函数 + 加 `__main__` 守卫 |
| `permutation.py` | `algorithms/permutation.py` | git mv，算法复用 `algorithms/dfs.py`，只保留排版 |
| `enumeration.py` | `algorithms/enumeration.py` | git mv，修计数逻辑 |
| `Exhaustiveenumeration.py` | `algorithms/exhaustive_enumeration.py` | git mv，文件名蛇形化 |
| `dynamic programming.py` | `algorithms/dynamic_programming.py` | git mv，去掉文件名空格 |
| `le.py` | `oop/student.py` | git mv，`student` → `Student` |
| `studentManagement.py` | `oop/student_management.py` | git mv，修 3 处属性/删除逻辑 bug |
| `leiceshi.py` | `oop/student_management.py` 的 `demo()` | **合并**：消除与 `studentManagement` 的循环导入 |
| `jicheng.py` | `oop/inheritance_demo.py` | git mv，`jicheng`（继承）→ `inheritance_demo` |

> 重命名全部用 `git mv` 完成，`git log --follow oop/student.py` 之类仍能追到旧文件。
> 被「合并」的 3 个脚本内容都已经在新文件的 docstring / `# 修复:` 注释 / `README` 表格里留档。

## 已修复的 bug 清单

| 文件（旧名） | 问题 | 修法 |
| --- | --- | --- |
| `判断水仙花数.py` | `s = s + a**3` 而 `s` 从未初始化 → `UnboundLocalError` | 改用 `sum(int(d) ** len(digits))`，不再用累加变量 |
| `判断水仙花数.py` | `while number != 0: number //= 10` 把入参除到 0，最后 `s == number` 恒为 False | 用 `str(number)` 拆位，不修改入参（对照 `shuixianhua.py` 的 temp 写法） |
| `bfs.py` | `ans = [[-1 for _ in range(m)]-1 in range(n)]`：list 减 1 → TypeError；整个表达式得到的是 bool 不是矩阵 | 改成 `[[-1] * cols for _ in range(rows)]` |
| `bfs.py` | 先 `x -= 1` 再 `start_x = x - 1`，坐标减两次，起点越界 | 只做一次 1-based → 0-based 转换 |
| `bfs.py` | 函数 `solve()` 末尾调用 `solve()`，无限递归 | 删掉递归，改成 `if __name__ == "__main__": main()` |
| `bfs.py` | `input()` 只 catch `ValueError`，EOF 抛 `EOFError` 直接崩 | 一次性 `sys.stdin.read()`，空输入走示例分支 |
| `leiceshi.py` | `from leiceshi import student` 自引用 + 与 `studentManagement` 互相 import（循环导入） | 删掉 `leiceshi.py`，`Student` 只由 `oop/student.py` 提供，依赖单向 |
| `studentManagement.py` | `self.studentts` 拼写多一个 `t` → `AttributeError` | 统一为 `self.students` |
| `studentManagement.py` | 删除时用不存在的 `self.student`，删完不 `break`，未命中也逐项打印"没找到" | 用 `enumerate` + `del`，命中立即 `return True`，否则 `return False` |
| `enumeration.py` | 在逐位累加的循环体内就判断奇偶并 `n += 1`，一个数被重复计数 | 所有位加完再判断（`digit_sum(number) % 2 == 0`） |
| `dynamic programming.py` | `n <= 0` 时没有分支，掉到 `return c` 返回 4 | 显式处理 `n == 0`（返回 1）、`n < 0` 抛 `ValueError` |
| `dfs.py` / `permutation.py` | 模块顶层直接 `input()`，import 即阻塞，无法测试；负数静默无输出 | 算法进函数、交互进 `main()`，加 `__main__` 守卫与入参校验 |
| `Exhaustiveenumeration.py` | `strftime('%Y%m%d')` 的 `%Y` 不保证补零，公元 1000 年以前判断失效 | 手写 `f"{year:04d}{month:02d}{day:02d}"` |
| `jicheng.py` | 类名小写、`temprature`/`pingmu` 拼写、所有代码在模块顶层 | 规范命名 + 收进 `main()` |
| `le.py` | `display_inf0`（数字 0）、`upgrade_age`（实为覆盖）命名误导；年龄存成字符串 | 改名 `display_info` / `set_age`，年龄统一转 int 并校验 |

## 运行方式

```bash
# 1) 交互式脚本：不带参数会打印用法 + 示例
python algorithms/bfs.py
python algorithms/dfs.py
python algorithms/permutation.py
python algorithms/dynamic_programming.py
python algorithms/enumeration.py
python algorithms/exhaustive_enumeration.py

# 2) 从 stdin 喂输入
echo "3 3 1 1" | python algorithms/bfs.py          # 马走日 3x3 起点(1,1)
echo 3        | python algorithms/dfs.py           # 1..3 的全排列
echo 10       | python algorithms/dynamic_programming.py
echo 20200202 | python algorithms/exhaustive_enumeration.py

# 3) 不需要输入的脚本
python basics/narcissistic.py
python oop/inheritance_demo.py
python oop/student_management.py
```

> Windows PowerShell 下 `echo` 等价于 `Write-Output`，上面写法可直接用；
> 若终端中文乱码，先 `$env:PYTHONIOENCODING='utf-8'`。

## 测试

```bash
python -m pip install pytest     # 仅首次
python -m pytest -q              # 全量
python -m pytest tests/test_bfs.py -v   # 单个文件
```

当前状态：**122 passed**（`pytest 9.2.0`，Python 3.14.2）。用例覆盖每个可测函数，
包含 0 / 1 / 负数 / 空输入 / 不可达棋盘等边界；BFS 用「3x3 起点 (1,1)」这类可手算的
小例子断言完整距离矩阵。

## 已完成

- [x] 目录重构：`algorithms/` / `basics/` / `oop/` / `tests/`，全部 `git mv` 保留历史
- [x] 14 个散落脚本（外加 1 行 README）合并去重为 10 个模块（3 个合并进新文件、1 个空文件删除）
- [x] 上述 15 处 bug 修复，每处都有 `# 修复:` 单行注释说明「原来错在哪」
- [x] 所有脚本加 `if __name__ == "__main__":` 守卫，支持 stdin + 无输入示例
- [x] pytest 122 个用例全绿
- [x] README 重写（本文件）

## 待扩展

- [ ] `algorithms/` 补上复杂度注释（时间/空间）与对应题目链接
- [ ] 再加排序、二分、并查集、最短路径（Dijkstra）等专题
- [ ] `oop/` 增加 `dataclass` 版本对比，演示 `@dataclass` 与手写 `__init__` 的差异
- [ ] 给学生名册加持久化（`json` 文件读写），顺便练习文件 I/O 与异常处理
- [ ] 接入 `ruff` / `mypy`（属于开发依赖，不影响运行时的「无第三方依赖」约束）
