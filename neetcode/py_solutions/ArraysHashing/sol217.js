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

// improve runtime with a set
var containsDuplicate = function(nums) {
    let hashmap = new Set()
    for (let num of nums){
        if (hashmap.has(num)){
            return true
        }
        hashmap.add(num)
    }
    return false
};

// solution comparing set to input array
var containsDuplicate = function(nums) {
    const s = new Set(nums);
    return s.size !== nums.length;
};
