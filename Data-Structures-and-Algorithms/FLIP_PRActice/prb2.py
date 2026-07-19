def is_anagram(s,t):
    if len(s) !=len(t):
        return False
    note_s={}
    note_t={}
    for i in range(len(s)):
        char_s=s[i]
        char_t=t[i]
        if char_s==note_s:
            note_s+=1
        else:
            note_s=1
        if char_t==note_t:
            note_t+=1
        else:
            note_t=1
    return note_s==note_t
print(is_anagram('cat','act'))
        
