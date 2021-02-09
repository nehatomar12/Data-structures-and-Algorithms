import collections
graph = {}
inDegree = {}

k = 4
alien_dict = ["baa", "abcd", "abca", "cab", "cad"]

for word in alien_dict:
    for letter in word:
        graph[letter] = []
        inDegree[letter] = 0

for i in range(len(alien_dict)-1):
    w1 = alien_dict[i]
    w2 = alien_dict[i+1]

    for j in range(0, min(len(w1), len(w2))):
        if w1[j] != w2[j]:
            graph[w1[j]].append(w2[j])
            inDegree[w2[j]] += 1
            break
    else:
        if len(w2) < len(w1):
            print('')

q = collections.deque()
res = []

print(inDegree)
for key, value in list(inDegree.items()):
    if value == 0:
        q.append(key)
print(q)
while q:
    node = q.popleft()
    res.append(node)

    for child in graph[node]:
        inDegree[child] -= 1

        if inDegree[child] == 0:
            q.append(child)

print((''.join(res) if len(res) == k else ''))
