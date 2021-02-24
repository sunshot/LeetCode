## Solution

找到 LinkedList 的中间节点，然后比较前后两部分

https://leetcode.com/problems/palindrome-linked-list/

与：

https://leetcode.com/problems/reverse-linked-list/
https://leetcode.com/problems/linked-list-cycle
https://leetcode.com/problems/linked-list-cycle-ii
https://leetcode.com/problems/reorder-list/

都是相同的思路和套路

用两个 pointer 找到中间节点

## Solution1
所谓的 straightforward，找到中间节点，然后把结尾的一般先 reverse，然后再比较

## Solution1 and Solution2

讨论中的思路：https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space

寻找中间节点的时候就可以把前半段 reverse，然后比较，很聪明

比较的过程中可以把前半段再恢复，更聪明
