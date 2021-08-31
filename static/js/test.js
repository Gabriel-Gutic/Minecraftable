function compressedString(message) {
    if (message.length == 0) {
        return;
    }
    var result = "";
    var count = 0;
    for (var n = 0; n < message.length; n++) {
        count++;
        if (message[n] != message[n + 1]) {
            result += message[n] + count;
            count = 0;
        }
    }
    return result;
}

console.log(compressedString("aabcc"))