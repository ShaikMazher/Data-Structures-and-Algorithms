def product_cat(s):
    note={}
    for char in s:
        if char in note:
            note[char]+=1
        else:
            note[char]=1
    for first in range(len(s)):
        char=s[first]
        if    note[char]==1:
            return first
    return False
print(product_cat("aabbcdd"))
