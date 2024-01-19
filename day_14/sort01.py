import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    s = input().count('0')
    print(
        *(
            ['0']*s + ['1']*(n-s)
        )
    )

for _ in range(int(input())): solve()
