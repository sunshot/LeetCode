public class Solution {
    public String multiply(String num1, String num2) {
        if(num1 == null || num1.trim().isEmpty() || num2 == null || num2.trim().isEmpty()){
            return "0";
        }
        num1 = num1.trim();
        num2 = num2.trim();
        if(num1.equals("0") || num2.equals("0")){
            return "0";
        }
        int len1 = num1.length();
        int len2 = num2.length();
        int i_n1 = 0;
        int i_n2 = 0;
        int []result = new int[len1 + len2];
        
        // Go from right to left in num1 
        for (int i = len1 - 1; i >= 0; i--){
            int carry = 0;
            int n1 = num1.charAt(i) - '0';
            
            i_n2 = 0;
            
            for (int j = len2 - 1; j>=0; j--){
                int n2 = num2.charAt(j) - '0';
                int sum = n1 * n2 + result[i_n1 + i_n2] + carry; 
                carry = sum / 10;
                result[i_n1 + i_n2] = sum % 10;
                
                i_n2++;
            }
            
            if(carry>0)
                result[i_n1+i_n2] += carry;
            
            i_n1++;
        }
        
        // ignore '0's from the right 
        int i = result.length - 1;
        while(i >= 0 && result[i] == 0)
            i--;
        if(i==-1)
            return "0";
        
        String s = "";
        while(i>=0){
            s += result[i--];
        }
        
        return s;
    }
}
