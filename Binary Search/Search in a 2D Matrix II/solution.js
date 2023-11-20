var searchMatrix = function(matrix, target) {
    var row = 0;
    var col = matrix[0].length-1;

    while(row<matrix.length && col>=0){
        if (matrix[row][col]==target){
            return true;
        }
        if (matrix[row][col]<target){
            row ++;
        } 
        else{
            col--;
        }
    }
    return false;
};
