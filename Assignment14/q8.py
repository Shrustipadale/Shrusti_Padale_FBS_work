def group_anagrams(strs):
    result = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in result:
            result[key].append(s)
        else:
            result[key] = [s]
    return list(result.values())
strs = input("Enter strings separated by space: ").split()
grouped = group_anagrams(strs)
print(grouped)

