

# 最大连续地皮 = 最大连续子集的和 

from typing import List

class Solution:
    def maxSubArrayLen(self, gain: List[int], target: int) -> int:
        prefix_sum = 0  # 当前的前缀和
        max_length = 0  # 最大长度
        prefix_map = {0: -1}  # 用哈希表记录前缀和及其对应的索引，初始化为0对应索引-1

        for i, num in enumerate(gain):
            prefix_sum += num  # 更新前缀和

            # 检查是否存在前缀和满足条件
            if prefix_sum - target in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - target])

            # 记录当前前缀和首次出现的位置
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length

def main():
    # 示例1
    gain = [1, -1, 5, 7, -1, 2, 1]
    target = 4
    solution = Solution()
    print(solution.maxSubArrayLen(gain, target))  # 输出：7

    # 示例2
    gain = [2, -2, -2, 2]
    target = 3
    print(solution.maxSubArrayLen(gain, target))  # 输出：0
    

if __name__ == "__main__":
    main()

