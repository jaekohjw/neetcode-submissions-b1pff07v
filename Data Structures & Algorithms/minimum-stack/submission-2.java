class MinStack {

    private Stack<Long> stack;
    private long min;

    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if (stack.empty()) {
            stack.push(0L);
            min = val;
        } else {
            stack.push(val - min);
            if (val < min) {
                min = val;
            }
        }
    }
    
    public void pop() {
        long diff = stack.pop();
        if (diff < 0) {
            min = min - diff;
        }
    }
    
    public int top() {
        long diff = stack.peek();
        if (diff < 0) {
            return (int) min;
        } else {
            return (int) (min + diff);
        }
    }
    
    public int getMin() {
        return (int) min;
    }
}
