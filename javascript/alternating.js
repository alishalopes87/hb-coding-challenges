function isSorted(b){
    let current = b[0]
    for(i=1; i < b.length; i++){
        if(b[i] > current){
            current = b[i]
        }else{
            return False
        }
    }
    return true
}
function generateArray(a){
    const b = []
    let i = 0
    let j = a.length - 1

    if(j == i){
        b.push(i)
    }
    while(i < j){
        b.push(a[i])
        b.push(a[j])
        i += 1
        j-= 1
    }
    return b
}


function alternatingSort(a){
    const b = generateArray(a)
    return isSorted(b)
}

console.log(alternatingSort([1, 3, 5, 6, 4, 2]))
//[1,2,3,4,4,6]