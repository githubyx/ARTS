public class Solution {

    public static void main(String[] args){
        Solution sol=new Solution();
        int xx=sol.myAtoi("9223372036854775808");
        System.out.println("Integer.MAX_VALUE");
    }

   public int myAtoi(String str) {
        long res=0;
        String strt=str.trim();
        if (strt.length() == 0){
           return 0;
        }  
        int sign=1;
        int start=0;
        if(strt.charAt(0)=='-'){
            sign=-1;
            start++;
        }
       if(strt.charAt(0)=='+'){
            start++;
        }
        for(int i=start;i<strt.length();i++){
            if(strt.charAt(i)>'9'||strt.charAt(i)<'0'){
                return (int) res*sign;
            }
            if(strt.charAt(i)<='9'&&strt.charAt(i)>='0'){
                res=res*10+strt.charAt(i)-'0';
            }
        }
        if(sign==1&&res>Integer.MAX_VALUE){
            System.out.print(Integer.MAX_VALUE);
            return Integer.MAX_VALUE;
        }
        if(sign==-1&&-res<Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }
        return (int) res*sign;
     }
}