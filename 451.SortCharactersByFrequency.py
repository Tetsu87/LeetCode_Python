from collections import Counter

def frequencySort(s):
    mapping = Counter(s)

    sorted_mapping = sorted(mapping.items(), key=lambda x:x[1])

    print(sorted_mapping)

    result = ""

    # for key,value in sorted_mapping.items():
    #     result += key*value
    
    return result

print(frequencySort("tree"))
