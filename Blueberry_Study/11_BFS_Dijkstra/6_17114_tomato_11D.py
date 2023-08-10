import sys
import heapq

input = sys.stdin.readline
direction = [(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
             (-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1)]

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
mmap = [[[[[[[[[[] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
queue = []

zero_count = 0
for _w in range(w):
    for _v in range(v):
        for _u in range(u):
            for _t in range(t):
                for _s in range(s):
                    for _r in range(r):
                        for _q in range(q):
                            for _p in range(p):
                                for _o in range(o):
                                    for _n in range(n):
                                        line = list(map(int, input().split()))
                                        mmap[_w][_v][_u][_t][_s][_r][_q][_p][_o].append(line)
                                        zero_count += line.count(0)
                                        for _m in range(m):
                                            if line[_m] == 1:
                                                queue.append((1, _m, _n, _o, _p, _q, _r, _s, _t, _u, _v, _w))

heapq.heapify(queue)

while queue:
    day, _m, _n, _o, _p, _q, _r, _s, _t, _u, _v, _w = heapq.heappop(queue)
    for dm, dn, do, dp, dq, dr, ds, dt, du, dv, dw in direction:
        nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw = _m + dm, _n + dn, _o + do, _p + dp, _q + dq, _r + dr, _s + ds, _t + dt, _u + du, _v + dv, _w + dw
        if not (0 <= nm < m and 0 <= nn < n and 0 <= no < o and 0 <= np < p and 0 <= nq < q and 0 <= nr < r and 0 <= ns < s and 0 <= nt < t and 0 <= nu < u and 0 <= nv < v and 0 <= nw < w):
            continue
        if mmap[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] != 0:
            continue
        zero_count -= 1
        mmap[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = day + 1
        heapq.heappush(queue, (day + 1, nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw))

if zero_count != 0:
    print(-1)
else:
    print(day - 1)
