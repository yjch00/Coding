import sys
import heapq
from collections import defaultdict


l, q = map(int, sys.stdin.readline().split())
waiting = dict()
queue = []
customer = defaultdict(int)
customer_dict = dict()
for _ in range(q):
    tmp = list(sys.stdin.readline().rstrip().split())
    if tmp[0] == '100':
        t, x = int(tmp[1]), int(tmp[2])
        name = tmp[3]
        if customer[name] < 0:
            c_t, c_x, c_n = customer_dict[tmp[3]]
            if c_x >= x:
                heapq.heappush(queue, (t + c_x - x, tmp[3]))
            else:
                heapq.heappush(queue, (t + l - x + c_x, tmp[3]))
        else:   # 그냥 초밥 쌓는 경우
            if not name in waiting:
                waiting[name] = []    
            waiting[name].append((t, x)) # t, x
        
    elif tmp[0] == '200':
        c_t, c_x, c_n = int(tmp[1]), int(tmp[2]), int(tmp[4])
        name = tmp[3]
        customer_dict[name] = (c_t, c_x, c_n)
        customer[name] -= c_n
        if name in waiting:
            for k in waiting[name]:
                t = k[0]
                x = k[1]
                if c_x >= (x+c_t-t)%l:
                    heapq.heappush(queue, (c_t + c_x - (x+c_t-t)%l, name))
                else:
                    heapq.heappush(queue, (c_t + l - (x+c_t-t)%l + c_x, name))
            waiting.pop(name)
            
    else:
        human_cnt = 0
        bab_cnt = 0
        p_t = int(tmp[1])

        while queue:
            t, name = heapq.heappop(queue)
            if t > p_t:
                heapq.heappush(queue, (t, name))
                break
            customer[name] += 1
        for i in waiting.values():      # !!! 처음 틀렸던 부분.
            bab_cnt += len(i)
        bab_cnt += len(queue)
        for i in list(customer.values()):
            if i < 0 :
                human_cnt += 1
        
        print(human_cnt, bab_cnt)