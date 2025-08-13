import heapq

class MedianFinder:

    def __init__(self):
        self.top_half = [] # min heap
        self.bottom_half = [] # max heap

    def addNum(self, num: int) -> None:
        # 1) see if the number belongs to the top half or bottom half
        # 2) push it to the half it belongs to
        # 3) if the half that got pushed to is more than 1 greater than the other half, then pop one from it and add it to the other half
        if(len(self.bottom_half) != 0 and num > -self.bottom_half[0]):
            heapq.heappush(self.top_half, num)
        else:
            heapq.heappush(self.bottom_half, -num)
        
        if(len(self.bottom_half) > len(self.top_half) + 1):
            # pop one from bottom half, give it to top half
            popped = -heapq.heappop(self.bottom_half)
            heapq.heappush(self.top_half, popped)
        elif (len(self.top_half) > len(self.bottom_half) + 1):
            popped = heapq.heappop(self.top_half)
            heapq.heappush(self.bottom_half, -popped)

    def findMedian(self) -> float:
        if((len(self.bottom_half) - len(self.top_half)) == 0):
            return ((-self.bottom_half[0]) + self.top_half[0]) / 2
        elif((len(self.bottom_half) - len(self.top_half)) == 1):
            return -(self.bottom_half[0])
        elif((len(self.top_half) - len(self.bottom_half)) == 1):
            return (self.top_half[0])
        else:
            return -9


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()