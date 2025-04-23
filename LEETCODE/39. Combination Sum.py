from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        1. 저장할 상태값 : 지금까지 담은 숫자 리스트 
        2. 다음 노드로 넘어갈 조건  : target보다 작은경우
        3. 정답인 조건 : 숫자 리스트의 총합 == target
        """

        ans = []
        
        def backtrack(start_idx: int, num_list: List[int]) -> None:
            nonlocal ans
            if sum(num_list) == target:
                ans.append(list(num_list))
                return

            # 유니크한 조합의 경우
            for i in range(start_idx, len(candidates)):
                candidate = candidates[i]
                if sum(num_list) + candidate <= target:
                    num_list.append(candidate)
                    backtrack(i, num_list)
                    num_list.pop()

            # 중복 순열 (정답 X)
            # for cd in candidates:
            #     if sum(num_list) + cd <= target:
            #         num_list.append(cd)
            #         backtrack(num_list)
            #         num_list.pop()

        backtrack(0, [])
        return ans
