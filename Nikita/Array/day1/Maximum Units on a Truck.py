def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1],reverse=True)
        total=0
        for box,unit in boxTypes:
            if truckSize<=box:
                total+=truckSize*unit
                break
            total+=box*unit
            truckSize-=box
        return total
            
            
        
