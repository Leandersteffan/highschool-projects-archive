class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0
        for number, units in boxTypes:
            if truckSize <= number:
                total_units += truckSize * units
                break
            total_units += units * number
            truckSize -= number
        return total_units

# selber (success)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        for i in range(1, len(boxTypes)):
            while boxTypes[i][1] > boxTypes[i-1][1] and i > 0:
                x = boxTypes.pop(i)
                boxTypes.insert(i - 1, x)
                i -= 1
        while truckSize > 0:
            if len(boxTypes) != 0:
                if boxTypes[0][0] == 0:
                    boxTypes.pop(0)
                else:
                    boxTypes[0][0] -= 1
                    units += boxTypes[0][1]
                    truckSize -= 1
            else:
                break
        return units
