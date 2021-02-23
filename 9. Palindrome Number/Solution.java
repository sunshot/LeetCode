class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        if(x<10){
            return true;
        }
        int num = x;
        int result = 0;
        while(num>0){
            if(result > Integer.MAX_VALUE / 10 || 
               (result == Integer.MAX_VALUE / 10 && num % 10 > Integer.MAX_VALUE % 10)){
                return false;
            }
            result = result * 10 + num % 10;
            num = num / 10;
        }
        return result == x;
    }
}