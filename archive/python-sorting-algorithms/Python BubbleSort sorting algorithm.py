'''Man schaut sich immer zwei nebeneinander liegende Punkte an und startet
links. Wenn der rechte Punkt größer ist tauschen sie Plätze und man schaut
sich die nächsten beiden an. Man geht auf diese Weise so lange erneut durch das
Array bis alle im richtigen Punkt sind. (0)n**2
yt: https://www.youtube.com/watch?v=YHm_4bVOe1s&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=3'''
'langsam'
def bubbleSort(myList):
    for i in range(0, len(myList) - 1):
        for j in range(0, len(myList) - 1 - i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

print(bubbleSort([1,4,6,2,6,9,2]))
