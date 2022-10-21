def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []

    def helper(target, curr, p, skip):
        if p >= 0 and sum(candidates[: p + 1]) >= target:
            num = candidates[p]
            if sum(candidates[: p + 1]) == target:
                temp = curr.copy()
                for i in range(p + 1):
                    temp.append(candidates[p - i])
                result.append(temp)
                p = -1
            elif num == target:
                if num not in skip:
                    temp = curr.copy()
                    temp.append(num)
                    result.append(temp)
                    cskip = skip.copy()
                    cskip.add(num)
                    helper(target, curr, p - 1, cskip)
                else:
                    helper(target, curr, p - 1, skip)
            elif num > target:
                helper(target, curr, p - 1, skip)
            else:
                if num not in skip:
                    # use num and iterate
                    temp = curr.copy()
                    temp.append(num)
                    helper(target - num, temp, p - 1, skip)

                    # skip num and iterate
                    cskip = skip.copy()
                    cskip.add(num)
                    helper(target, curr, p - 1, cskip)
                else:
                    helper(target, curr, p - 1, skip)

    helper(target, [], len(candidates) - 1, set())

    # delete duplicates
    unique = set()

    for r in result:
        unique.add(tuple(r))

    return list(unique)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

candidates2 = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
target2 = 27

candidates3 = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
target3 = 30

print(combinationSum2(candidates, target))
print(combinationSum2(candidates2, target2))
print(combinationSum2(candidates3, target3))
