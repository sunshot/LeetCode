public class Solution1 {
    public int divide(int dividend, int divisor) {
        if(divisor == 0){
            return Integer.MAX_VALUE;
        }
        if(dividend == 0){
            return 0;
        }
        // handle overflow
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        if(divisor == Integer.MIN_VALUE){
            if(dividend == Integer.MIN_VALUE){
                return 1;
            }else{
                return 0;
            }
        }
        int sign = 1;
        if((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)){
            sign = -1;
        }
        int ans = 0;
        divisor = Math.abs(divisor);
        if(dividend == Integer.MIN_VALUE){
            dividend =  Integer.MAX_VALUE - divisor;
            dividend += 1;
            ans++;
        }else{
            dividend = Math.abs(dividend);
        }
        
        while(dividend >= divisor){
            dividend -= divisor;
            ans ++;
        }
        if(sign == -1){
            ans = 0 - ans;
        }
        return ans;
    }
    public static void main(String[] args) {
        Solution1 solution1 = new Solution1();
        int dividend = Integer.MIN_VALUE;
        int divisor = -1;
        int ans = solution1.divide(dividend, divisor);
        System.out.println(ans);

        int a = 1;
        System.out.println(a << 32);
        System.out.println(a << 31 << 1);
        System.out.println(a << 31);
    }
}
