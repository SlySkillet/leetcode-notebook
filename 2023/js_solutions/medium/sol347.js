// 347. Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

// broken:
var topKFrequent = function(nums, k) {
    // create a hashmap with num: numOccurrences
    let hashmp = {}
    for (let i=0; i<nums.length; i++){
        if (Object.keys(hashmp).includes(nums[i].toString())){
            hashmp[nums[i]] += 1
        } else {
            hashmp[nums[i]] = 1
        }
    }
    console.log(Object.keys(hashmp))
    console.log(hashmp)
    // sort hashmap by numOccurrences
    let sorted = []
    for (let entry in hashmp){
        sorted.push([entry, hashmp[entry]])
    }
    sorted.sort((a,b)=>{a[1]-b[1]}) // I believe the bug is here, not sorting by value correctly
    console.log(sorted)
    sorted = sorted.slice(0,k)
    let result = []
    sorted.forEach((item)=> {result.push(parseInt(item[0]))})
    return result
    // return an array of k highest
};
