
def f(s):
    for i in range(len(s)):
        if s[0]==s[i-1] and s[1]==s[i-2]:
            return True
        else: return False

print(f('hello'))
            