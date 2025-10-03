def checkDistances(s, distance):
    for i in range(len(distance)):
        buchstabe = chr(i + 97)
        pos = s.find(buchstabe)
        if pos < 0:
            continue
        if pos + distance[i] + 1 >= len(s) or s[pos] != s[pos + distance[i] + 1]:
            return False
    return True






distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s = "abaccb"
print(checkDistances(s, distance))