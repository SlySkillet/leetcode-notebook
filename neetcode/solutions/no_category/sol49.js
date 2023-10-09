// 49. Group Anagrams
// https://leetcode.com/problems/group-anagrams/description/

var groupAnagrams = function(strs) {
    let hashmp = new Map()
    strs.forEach(str =>{
        let sorted = str.split("").sort().join("")
        if (hashmp.has(sorted)){
            hashmp.set(sorted, [...hashmp.get(sorted),str])
        } else { hashmp.set(sorted, [str])}
    })
    return Array.from(hashmp.values())
};
