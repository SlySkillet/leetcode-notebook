//  238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/description/

var productExceptSelf = function(nums) {
    let res = []
    for (let i=0; i < nums.length; i++){
        res.push(1)
    }
    let prefix = 1
    for (let i=0; i < nums.length; i++){
        res[i] = prefix
        prefix *= nums[i]
    }
    let postfix = 1
    for (let i=nums.length - 1; i >= 0; i--){
        res[i] *= postfix
        postfix *= nums[i]
    }
    return res
};
