class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate area between current pointers
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            # Move the pointer at the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
