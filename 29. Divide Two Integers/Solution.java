class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == 0){
            return 0;
        }
        // handle overflow
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        
        int ans = 0;
        int a = Math.abs(dividend);
        int b = Math.abs(divisor);
       
        for(int x=31; x>=0; x--){
            if((a >>> x) - b >= 0){
                ans += 1 << x;
                a -= b << x;
            }
        }
        
        return (dividend > 0) == (divisor > 0)? ans : -ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int dividend = Integer.MIN_VALUE;
        int divisor = -1;
        int ans = solution.divide(dividend, divisor);
        System.out.println(ans);
    }
}
