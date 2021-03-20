from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num < 0:
            return []
        if num == 0:
            return ['0:00']
        if num > 10:
            num = 10
        ans = []
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        select_hours = []
        select_minutes = []
        
        def add(curr_hours: int, curr_minutes: int) -> None:
            curr = str(curr_hours) + ':'
            if curr_minutes < 10:
                curr += '0' + str(curr_minutes)
            else:
                curr += str(curr_minutes)
            ans.append(curr)
        
        def backtrack(curr_hours: int, curr_minutes: int, h: int, m: int) -> None:
            if h < len(hours):
                for i in range(h, len(hours)):
                    if curr_hours + hours[i] <= 11:
                        # valid one
                        select_hours.append(hours[i])
                        if len(select_hours) + len(select_minutes) == num:
                            # find one solution
                            add(curr_hours + hours[i], curr_minutes)
                        else:
                            backtrack(curr_hours + hours[i], curr_minutes, i+1, m)
                        select_hours.remove(hours[i])
                
                backtrack(curr_hours, curr_minutes, len(hours), m)
                        
            elif m < len(minutes):
                for j in range(m, len(minutes)):
                    if curr_minutes + minutes[j] <= 59:
                        select_minutes.append(minutes[j])
                        if len(select_hours) + len(select_minutes) == num:
                            # find one solution
                            add(curr_hours, curr_minutes + minutes[j])
                        else:
                            backtrack(curr_hours, curr_minutes + minutes[j], h, j+1)
                        select_minutes.remove(minutes[j])
        
        backtrack(0, 0, 0, 0)
        return ans
            
            
if __name__== '__main__':
    solution = Solution()

    num = 1
    ans = solution.readBinaryWatch(num)
    print(ans)

