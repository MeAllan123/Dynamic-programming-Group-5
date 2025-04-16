def fibonacci_memo(n, store={}):
    if n <= 1:
        return n
    if n not in store:
        store[n] = fibonacci_memo(n-1, store) + fibonacci_memo(n-2, store)
    return store[n]

def fibonacci_table(n):
    track = [0, 1]
    for i in range(2, n+1):
        track.append(track[i-1] + track[i-2])
    return track[n]

num = 8
print(fibonacci_memo(num))

