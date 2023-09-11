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
