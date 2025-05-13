class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """_summary_

        Args:
            nums (list[int]): lista di interi
            target (int): è il target di riferimento

        Returns:
            list[int]: ritorna una lista di interi, ovvero gli indici degli elementi della lista che se sommati equivalgono al param target
        """        
        result_list:list[int]= [num[0]+nums[1:] for num in nums if sum(num)==target]
        

            # if sum(num)==target:
            #     nums[0]