# Max conceticutive ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        maximum_length = 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                consecutive = 0
            maximum_length = max(maximum_length, consecutive)
        return maximum_length

# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        
        for n in nums:
            if len(str(n)) % 2 == 0:
                answer += 1 
                
        return answer

# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
      answer = []
      
      for n in nums:
          answer.append(n**2)
          
      return sorted(answer)
