def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()

    result = []

    def helper(target, curr, p):
        if p >=0:
            num = candidates[p]

            if num == target:
                temp = curr.copy()
                temp.append(num)
                result.append(temp)

                helper(target, curr, p-1)
            
            elif num > target:
                helper(target, curr, p-1)
            else:
                new_target = target - num
                temp1 = curr.copy()
                temp1.append(num)
                temp2 = curr.copy()
                temp2.append(num)
                # iterate with new target with same p
                helper(new_target,temp1,p)

                # iterate with new target with p -1
                helper(new_target,temp2,p-1)

                # iterate with the same target with p-1
                helper(target, curr, p-1)
    
    helper(target, [], len(candidates)-1)

    unique = set()
    for r in result:
        unique.add(tuple(r))
    final = []
    for u in unique:
        final.append(list(u))
    
    return final
    

candidates = [2,3,5,6,7,8]
target = 8

print(combinationSum(candidates,target))