function BinarySearchUnorderedList(list, value, left, right) {
    let middle = Math.trunc((left + right) / 2);
    if (left <= right) {
        id = parseInt(list[middle].id.split('-')[3], 10);

        if (id == value) {
            return id;
        } else if (value < id) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }

        return BinarySearchUnorderedList(list, value, left, right);
    }
    return null
}