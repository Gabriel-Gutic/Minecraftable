function IsLetter(char) {
    return char.length === 1 && char.match(/[a-z]/i);
}

function IsNumeric(char) {
    return char.length === 1 && char >= '0' && char <= '9';
}

function IsLetterOrNumber(char) {
    return isLetter(char) || isNumeric(char)
}