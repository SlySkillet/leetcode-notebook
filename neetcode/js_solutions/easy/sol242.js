// 242. Valid Anagram
// https://leetcode.com/problems/valid-anagram/description/

var isAnagram = function(s, t) {
    let sOrd = []
    let tOrd = []
    if (s.length !== t.length){
        return false
    }
    for (let i=0; i < s.length; i++){
        sOrd.push(s.charCodeAt(i))
        tOrd.push(t.charCodeAt(i))
    }
    sOrd.sort((a,b)=>a-b)
    tOrd.sort((a,b)=>a-b)
    console.log("s", sOrd, "t", tOrd)
    for (let i=0; i < s.length; i++){
        if (sOrd[i] != tOrd[i]) {
            console.log("i", i)
            return false
        }
    }
    return true
};

// refactored solution with count objects
var isAnagram = function(s, t) {
    if (s.length !== t.length){
        return false
    }
    sCount = {}
    tCount = {}
    for (let i=0; i < s.length; i++){
        sCount[s[i]] ? sCount[s[i]] += 1 : sCount[s[i]] = 1
        tCount[t[i]] ? tCount[t[i]] += 1 : tCount[t[i]] = 1
    }
    for (let char in sCount){
        if (sCount[char] !== tCount[char]){
            return false
        }
    }
    return true
};
