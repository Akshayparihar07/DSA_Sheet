/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    function elem_search(mat_row, target, m) {
        var low = 0;
        var high = m - 1;

        while (low <= high) {
            var mid = Math.floor((low + high) / 2);

            if (mat_row[mid] == target) {
                return true;
            }

            if (mat_row[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
    }


    var n = matrix.length;
    for(var r=0; r<n; r++){
        var m = matrix[r].length
        if(matrix[r][0]<=target && target<=matrix[r][m-1]){
            if(elem_search(matrix[r], target, m)){
                return true;
            }
        }
    }
    return false;
};
