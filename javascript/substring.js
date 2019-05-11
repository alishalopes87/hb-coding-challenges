// For str = "aabeefegeeccrr" and k = 3, 
// the output should be upToKDifferences(str, k) = 3.

// There are a few ways to achieve this result; 
// one example would be to split str this way: ["aab", "eefegee", "ccrr"].
// input:
// str: "boooolpptttpptab"
// k: 2
// Expected Output:

function upToKDifferences(str,k){
	//create var count
	//create var substring
	//results = []
	//iterate over str
	//if str[i] in subtring
	//count += 1
	//if count >= 3
	//push substring to result
	//count = 0
	//return result

	let count = 1
	let substring = ''
	const result = []

	for(i=0; i < str.length; i++){
		if( substring.includes(str[i])){
			count = count + 1
			if(count >= k){
				result.push(substring)
				substring = ''
				count = 0
			}
			substring = substring + str[i]
		}else{
			substring = substring + str[i]
		}
	}
	result.push(substring)
	return result.length
}
console.log(upToKDifferences("aabeefegeeccrr",3))