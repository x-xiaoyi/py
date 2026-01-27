try:
    n = int(input())
    if n <= 0:
        raise ValueError()
except Exception:
    print("请输入一个正整数。")
    raise SystemExit

path = []
used = [False] * (n + 1)
def dfs(depth):
    if depth == n + 1:
        for i in path:
            print(f"{i:5d}", end="")
        print()
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            path.append(i)
            dfs(depth + 1)
            path.pop()
            used[i] = False

if __name__ == "__main__":
    dfs(1)