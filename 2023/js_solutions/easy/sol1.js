// 1. Two Sum
// https://leetcode.com/problems/two-sum/

var twoSum = function(nums, target) {
    const setNums = new Set(nums)
    console.log(setNums)
    let result = []
    for (let i=0; i < nums.length; i++){
        let searchNum = target - nums[i]
        console.log(searchNum)
        let j
        if (setNums.has(searchNum) && nums.indexOf(searchNum) !== i) {
            j = nums.indexOf(searchNum)
            result.push(i)
            result.push(j)
            return result
        }
    }
};
