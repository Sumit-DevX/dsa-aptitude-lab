def bubble_sort(nums : list[int]) -> list[int]:
    swapping : bool = True 

    end : int = len(nums)

    while swapping:
        swapping = False 
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1],nums[i] = nums[i] , nums[i-1]
                swapping = True

        end -= 1 


    return nums

print(bubble_sort([3,5,2,4]))
