def isSubsequence(s,t):

    l = ""
    s_ptr = 0
    t_ptr = 0

    while t_ptr < len(t):
        if s_ptr == len(s):
            break
        if s[s_ptr] == t[t_ptr]:
            l += t[t_ptr]
            s_ptr += 1
            t_ptr += 1
        else:
            t_ptr += 1

    return s == l



s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))