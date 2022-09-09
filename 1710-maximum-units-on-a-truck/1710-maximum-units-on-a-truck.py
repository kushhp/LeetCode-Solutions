class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        ans = 0
        box_used = 0
        for i in range(len(boxTypes)):
            num_box, num_units = boxTypes[i][0], boxTypes[i][1]
            for _ in range(num_box):
                if box_used >= truckSize:
                    break
                ans += num_units
                box_used += 1
        return ans 