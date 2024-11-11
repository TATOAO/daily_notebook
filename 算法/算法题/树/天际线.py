# https://leetcode.cn/problems/the-skyline-problem/?envType=problem-list-v2&envId=segment-tree
from typing import List, Self, Optional

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:


        class Point():
            all_points: List[Self] = []
            def __init__(self, x: int, h: int, left_point: Optional[Self], right_point: Optional[Self]):
                self.x = x
                self.h = h
                self.left_point = None
                self.right_point = None

            def add_point(self, point: Self,  current_index: int):

                point_list = Point.all_points
                if len(point_list) == 0:
                    point_list.append(point)
                    return 

                if current_index is None:
                    current_index = 0

                middle_index = current_index + (len(point_list) - current_index) // 2

                if self <= point:
                    all_points[middle_index]


            
            
            def __le__(self, other: Self):
                return self.x <= other.x and self.h <= other.h
            
            

        return [[]]


def main():
    solu = Solution()
    s1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    s2 = [[0,2,3],[2,5,3]]
    
    result = solu.getSkyline(s1)
    print(result)

if __name__ == "__main__":
    main()

