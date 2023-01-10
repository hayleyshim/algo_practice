


sample = ["propose"]
answer = []
tmp = {}
for w in sample:
    w1 = w.lower()
    if w1 in tmp:
        tmp[w1] += 1
    else:
        tmp[w1] = 1


tmplist = [[c, tmp[c]] for c in tmp]
print(tmplist)
tmplist.sort(key=lambda x : (x[1], x[0]), reverse = True)
print(tmplist)


sortres = sorted(sorted(tmplist, key=lambda x: x[0]), key=lambda x: -x[1])
print(sortres)

for w in sortres:
    answer.append(w[0])

print(answer)