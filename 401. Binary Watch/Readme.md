# [401. Binary Watch](https://leetcode.com/problems/binary-watch/)

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

```
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
```

Note:
- The order of output does not matter.
- The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
- The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

Similar Problems:

- [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)

Solution1: Backtracking. 其实时排列组合问题，即 num 个 LED 灯，如何选择 hours 和 minutes？回溯是类似问题的解法，关键在于如何选择 Candidate？

```python
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
```

即先选择 hours ，再选择 minutes，要注意 ``backtrack(curr_hours, curr_minutes, len(hours), m)`` 用于选择 0 个 hours。Runtime: 28 ms, faster than 92.12% of Python3 online submissions for Binary Watch.

https://leetcode.com/problems/binary-watch/discuss/88453/Python-DFS-and-complexity-analysis

