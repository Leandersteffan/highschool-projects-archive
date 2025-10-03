given = "cbbd"

def longestPalindrome(s):
    d = ''
    half_s = int(len(s) / 2)
    for i in range(len(s)):
        a, b, c = i - 1, i + 1, s[i]
        for j in range(half_s):
            if a > -1 and b < len(s):
                if s[a] == s[b]:
                    c = s[a] + c + s[b]
                    a, b = a - 1, b + 1
                else:
                    break
        if len(c) > len(d):
            d = c
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            a, b, c = i - 1, i + 2, s[i] + s[i + 1]
            for j in range(half_s):
                if a > -1 and b < len(s):
                    if s[a] == s[b]:
                        c = s[a] + c + s[b]
                        a, b = a - 1, b + 1
                    else:
                        break
            if len(c) > len(d):
                d = c
    s = d
    return s



print(longestPalindrome(given))