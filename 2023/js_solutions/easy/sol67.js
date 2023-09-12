//  67. Add Binary
// https://leetcode.com/problems/add-binary/description/

// solution using add and carry
var addBinary = function(a, b) {
    // create result variable as an array
    let res = ""
    // determine if length of strings is the same
    if (a.length !== b.length){
    // pad the shorter string with leading 0s
        if (a.length < b.length){
            while(a.length !== b.length){
                a = '0' + a
            }
        }else if (b.length < a.length){
            while (b.length !== a.length){
                b = '0' + b
            }
        }
    }
    // iterate from the end of each string, adding the digits and carrying remainder
    let carry = 0
    for (let i=a.length-1; i >=0; i--){
        let num = parseInt(a[i]) + parseInt(b[i]) + carry
        res = (num%2) + res
        carry = num >= 2 ? 1 : 0
    }
    if (carry) {
        res = "1" + res
    }
    // return result
    return res
};
