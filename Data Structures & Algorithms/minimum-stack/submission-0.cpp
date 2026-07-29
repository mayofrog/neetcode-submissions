class MinStack {
private:
    long min;
    std::stack<long> stack1;
    std::stack<long> stack2;

public:
    MinStack() {}
    
    void push(int val) {
        if(stack1.empty()){
            stack1.push(val);
            stack2.push(val);
        }
        else{
            stack1.push(val);
            if(val > getMin())
                stack2.push(getMin());
            else{
                stack2.push(val);
            }
        }
    }
    
    void pop() {
        stack1.pop();
        stack2.pop();
    }
    
    int top() {
        return stack1.top();
    }
    
    int getMin() {
        return stack2.top();
    }
};
