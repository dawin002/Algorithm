n, m = map(int, input().split())
arr = []
res = []
for _ in range(n):
    name, tmp = input().split()
    songs = []
    for i in range(m):
        if tmp[i] == 'Y':
            songs.append(i)
    arr.append(songs)

mini = 99999999
maxi = 0
def recur(idx, count):
    if idx == n:
        global maxi
        global mini
        if maxi <= len(set(res)):
            maxi = len(set(res))
            if mini > count:
                mini = count

        return

    for song in arr[idx]:
        res.append(song)
    recur(idx+1, count+1)
    for song in arr[idx]:
        res.remove(song)

    recur(idx+1, count)

recur(0, 0)
if mini == 0 or mini == 99999999:
    print(-1)
else:
    print(mini)