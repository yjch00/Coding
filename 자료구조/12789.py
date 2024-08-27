import sys
from collections import deque


n = sys.stdin.readline().strip()
nums = map(int, sys.stdin.readline().split())
queue = deque(nums)
stack = []
target = 1
while queue:
    if queue and queue[0] == target:
        queue.popleft()
        target += 1
    else:
        stack.append(queue.popleft())
    while stack and stack[-1]==target:
        stack.pop()
        target += 1


if not stack:
    print('Nice')
else: print('Sad')