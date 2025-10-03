start = input('Was soll gecheckt werden: ')
gedreht = ''
for i in range (0,len(start)):
    gedreht = start[i] + gedreht
if gedreht.lower() == start.lower():
    print('ist ein Palindrom')
else:
    print('ist kein Palindrom')




def f():
    start = input()
    gedreht = ''
    for i in range (0,len(start)):
        gedreht = start[i] + gedreht
    if gedreht == start:
        print(start,'reads as', gedreht, 'from left to right and from right to left.')
        True
    else:
        print('From left to right, it reads', start, '. From right to left, it becomes', gedreht,'. Therefore it is not a palindrome.')
        
f()
