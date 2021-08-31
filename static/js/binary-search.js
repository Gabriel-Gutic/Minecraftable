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

function BinarySearchElement(element_type, element_id)
{
    if (element_type == "item") {
        var list = $(".item-element")
        let item_id = BinarySearchUnorderedList(list, element_id, 0, list.length)

        return $("#radio-item-" + item_id)

    } else if (element_type == "tag") {
        var list = $(".tag-element")
        let tag_id = BinarySearchUnorderedList(list, element_id, 0, list.length)

        return $("#radio-tag-" + tag_id)
    } else {
        console.error("Invalid element type: " + element_type)
    }
}