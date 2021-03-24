class Solution {
    public int myAtoi(String s) {
        int i = 0;
        while(i<s.length() && s.charAt(i) == ' '){
            i++;
        }
        int sign = 1;
        if(i<s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')){
            if(s.charAt(i) == '-'){
                sign = -1;
            }
            i++;
        }
        
        int result = 0;
        while(i<s.length() && (s.charAt(i) >= '0' && s.charAt(i) <= '9')){
            // int curr = s.charAt(i) - '0';
            if(result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && s.charAt(i) - '0' > Integer.MAX_VALUE % 10)){
                if(sign == 1){
                    return Integer.MAX_VALUE;
                }else{
                    return Integer.MIN_VALUE;
                }
            }else{
                result = result * 10 + (s.charAt(i) - '0');
            }
            i++;
        }
        return sign * result;
    }
}