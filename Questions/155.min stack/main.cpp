#include<iostream>

class MinStack {
public:
    std::stack<std::pair<int, int>> s;

    MinStack() {

    }

    void push(int val) {
        if (s.empty()) {
            s.push({val, val});
        } else {
            int curMin = s.top().second;
            s.push({val, std::min(curMin, val)});
        }
    }

    void pop() {
        s.pop();
    }

    int top() {
        return s.top().first;
    }

    int getMin() {
        return s.top().second;
    }
    
};