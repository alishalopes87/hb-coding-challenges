function common_prefix(word1,word2){
	let substring = ""
	let i = 0
	let j = 0

	while(i < word1.length && j < word2.length){
		if(word1[i] === word2[j]){
			substring = substring + word1[i]
			i++
			j++

		}else{
			break
		}
	}
	return substring
}

function longest_prefix(array){
	
	if(array.length < 1){
		return substring
	}
	if(array.length == 1){
		return array[0]
	}

	let word1 = array[0]
	let word2 = array[1]
	let substring = common_prefix(word1, word2)

	for(i=2; i < array.length; i++){
		substring = common_prefix(substring, array[i])
	}
	return substring
}

console.log(longest_prefix(["flower","flow", "flight"]))
console.log(longest_prefix(["a"]))