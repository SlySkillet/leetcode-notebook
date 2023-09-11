// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/description/

var containsDuplicate = function(nums) {
    let hashmap = []
    for (let num of nums){
        if (hashmap.includes(num)){
            return true
        }
        hashmap.push(num)
    }
    return false
};
