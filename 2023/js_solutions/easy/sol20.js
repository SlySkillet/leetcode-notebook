// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/description/

var isValid = function(s) {
    let stack = []
    for (let i=0; i<s.length; i++){
        if (s[i] == '('){
            stack.push(')')
        } else if (s[i] == '['){
            stack.push(']')
        } else if (s[i] == '{'){
            stack.push('}')
        } else if (stack.pop() !== s[i]){
            return false
        }
    }
    return !stack.length
};
