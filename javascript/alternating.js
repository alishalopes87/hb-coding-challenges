function alternatingSort(a) {
    const b = [],
    j = a.length- 1
    
    for(i = 0; i < a.length; i++){
        if( i % 2 === 0){
            b.push(a[i])
        }else{
            b.push(a[j])
            j -= j
        }
    }
    return b
}

console.log(alternatingSort([1, 3, 5, 6, 4, 2]))