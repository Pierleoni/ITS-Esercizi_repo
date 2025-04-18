from typing import Callable

nums_list:list[int] = [5, 12, 17, 18, 24, 32]

even_list:Callable[[list[int]], list[int]] = list(filter(lambda x:x%2==0, nums_list))
print(even_list)