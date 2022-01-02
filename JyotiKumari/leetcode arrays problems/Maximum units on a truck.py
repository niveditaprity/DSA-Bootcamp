class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda row: (row[1], row[0]), reverse = True)
        count = 0
        max_units = 0
        for i in range(len(boxTypes)):
            if(count<truckSize):
                if(boxTypes[i][0]<truckSize-count):
                    max_units+=boxTypes[i][0]*boxTypes[i][1]
                    count+=boxTypes[i][0]
                else:
                    max_units+= (truckSize-count)*boxTypes[i][1]
                    count+=(truckSize-count)
            else:
                break
        return max_units