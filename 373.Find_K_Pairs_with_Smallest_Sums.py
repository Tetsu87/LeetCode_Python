import heapq
nums1 = [7,15,1]
nums2 = [2,9,11]

def ksmall(nums1,nums2,k):
    if not nums1 or not nums2:
        return []
    
    visited = set()
    heap = []
    output = []

    heapq.heappush(heap, (nums1[0]+nums2[0],0,0))
    visited.add((0,0))

    while len(output) < k and heap:
        val = heapq.heappop(heap)
        curr_sum,p1,p2 = val
        output.append((nums1[p1],nums2[p2]))

        if p1 + 1 < len(nums1) and (p1+1,p2) not in visited:
            heapq.heappush(heap,(nums1[p1+1] + nums2[p2]),p1+1,p2)
            visited.add(p1+1,p2)
        
        if p2 + 1 < len(nums1) and (p1,p2+1) not in visited:
            heapq.heappush(heap,(nums1[p1] + nums2[p2+1]),p1,p2+1)
            visited.add(p1,p2+1)
    return output


        
