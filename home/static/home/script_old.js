// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");



// if user press any key and release
inputBox.onkeyup = (e) => {
    let userData = e.target.value; // characters entered by user
    let emptyArray = [];
    if (userData) {
        emptyArray = suggestions.filter((data) => {
            // filtering books to those that start with user entry
            let userDataSplit = userData.split(" ");
            let bookSplit = data.split(" ");
            let wordMatchCount = 0;

            // loops through each word entered, checks against each book for match (words can be in wrong order)
            for (var u = 0; u < userDataSplit.length; u++) {
                var userWord = userDataSplit[u];
                for (var b = 0; b < bookSplit.length; b++) {
                    var bookWord = bookSplit[b];
                    if (bookWord.toLocaleLowerCase().startsWith(userWord.toLocaleLowerCase())) {
                        wordMatchCount ++;
                        break
                    }
                }
            }

            return wordMatchCount === userDataSplit.length
        });
        emptyArray = emptyArray.map((data) => {
            return data = '<li>'+ data +'</li>';
        });
        console.log(emptyArray);
        searchWrapper.classList.add("active");
    }
    showSuggestions(emptyArray, userData);
}

function showSuggestions(list, userData) {
    let listData;
    if (userData.length === 0) {
        listData = '';
    }
    else if (!list.length) {
        userValue = inputBox.value;
        listData = '<li>Add a new book: ' + userValue + '</li>';
    }
    else {
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}