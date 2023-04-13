function quickSort(array){
    if (array.length<1){
        return array;
    }
    var middle=array[0];
    var left=[];
    var right=[];
    for (let i=1;i<array.length;i++){
        if(array[i]<middle){
            left.push(array[i]);
        }else{
            right.push(array[i]);
        }
    }
    return quickSort(left).concat(middle,quickSort(right));
}
var unsorted=[5,4,3,2,1];
var sorted =quickSort(unsorted);
console.log(sorted);
