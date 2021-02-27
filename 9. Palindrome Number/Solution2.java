class Solution2 {
    public boolean isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)){
            return false;
        }
        if(x < 10){
            return true;
        }
        int result = 0;
        while(x > result){
            result = result * 10 + x % 10;
            x = x / 10;
        }
        return x == result || x == result/10;
    }

    public static void main(String[] args) {
        Solution2 solution = new Solution2();
        boolean result = solution.isPalindrome(121);
        System.out.println(result == true);
    }
}