import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

def recbinsearch(L, l, u, target):
    # L: 탐색 대상이 되는 리스트
    # l: 탐색 범위의 왼쪽 (아래쪽) 끝 (lower)
    # u: 탐색 범위의 오른쪽 (위쪽) 끝 (upper)
    # target: 탐색하고자 하는 값 (key)
    return -1

    middlenum = (l+u)//2
    if target == L[middlenum]:
        return L(middlenum)
    elif target < L[middlenum]:
        return recbinsearch(L, l, middlenum-1, target)
    else :
        return recbinsearch(L, middlenum + 1, l, target)



numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))