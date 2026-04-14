class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stk = new Stack<>();

        for (String t : tokens) {
            int num1, num2;
            switch (t) {
                case "*":
                    num2 = stk.pop();
                    num1 = stk.pop();
                    stk.push(num1 * num2);
                    break;
                case "+":
                    num2 = stk.pop();
                    num1 = stk.pop();
                    stk.push(num1 + num2);
                    break;
                case "-":
                    num2 = stk.pop();
                    num1 = stk.pop();
                    stk.push(num1 - num2);
                    break;
                case "/":
                    num2 = stk.pop();
                    num1 = stk.pop();
                    stk.push(num1 / num2);
                    break;
                default:
                    stk.push(Integer.valueOf(t));
                    break;
            }
        }
        
        return stk.pop();
    }
}
