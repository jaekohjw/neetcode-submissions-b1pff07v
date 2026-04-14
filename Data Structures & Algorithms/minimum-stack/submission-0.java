class MinStack {

    private Stack<Integer[]> stack;

    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if (stack.empty()) {
            stack.push(new Integer[] {val, val});
        } else if (val < stack.peek()[1]) {
            stack.push(new Integer[] {val, val});
        } else {
            stack.push(new Integer[] {val, stack.peek()[1]});
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek()[0];
    }
    
    public int getMin() {
        return stack.peek()[1];
    }
}
