function processList(bookList) {
    var suggSplit = suggestions.split('&quot;');
    var itemsToExclude = [", ", "[", "]"];
    var suggReduced = suggSplit.filter(function(item) {
        var itemToExclude;
        for (i = 0; i < itemsToExclude.length; i++) {
            itemToExclude = itemsToExclude[i];
            if (item === itemToExclude) {
                return false
            }
        }
        return true
    });
    return suggReduced
}

function processZippedList(bookAuthorList) {
    console.log(bookAuthorList);
}