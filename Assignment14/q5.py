def Prefix(strs):
    if not strs:
        return ""
    prefix = ""
    for chars in zip(*strs):
        if len(set(chars)) > 1:
            break
        prefix += chars[0]
    return prefix

print(Prefix(["flower", "flow", "flight"]))  
print(Prefix(["dog", "racecar", "car"]))     
