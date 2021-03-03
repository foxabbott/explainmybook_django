// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");

// if user press any key and release
inputBox.onkeyup = (e) => {
    let userData = e.target.value; // characters entered by user
    let includedKeys = [];
    if (userData) {
        includedKeys = Object.keys(books).filter((key) => {
            // filtering books to those that start with user entry
            let userDataSplit = userData.split(" ");
            let searchable = books[key].searchable;
            let titleAuthorSplit = searchable.split(" ");
            let wordMatchCount = 0;

            // loops through each word entered, checks against each book for match (words can be in wrong order)
            for (var u = 0; u < userDataSplit.length; u++) {
                var userWord = userDataSplit[u];
                for (var b = 0; b < titleAuthorSplit.length; b++) {
                    var bookWord = titleAuthorSplit[b];
                    if (bookWord.toLocaleLowerCase().startsWith(userWord.toLocaleLowerCase())) {
                        wordMatchCount ++;
                        break
                    }
                }
            }

            return wordMatchCount === userDataSplit.length
        });

        includedBooks = includedKeys.map((data) => {
            linkWrap = `<a href="/books/` + data + `">`;
            linkInterior = `<li>` + books[data].list_display + `</li>`;
            totalOut = linkWrap + linkInterior + `</a>`;
            return totalOut
        });
        searchWrapper.classList.add("active");
    }
    showSuggestions(includedBooks, userData);
}

function showSuggestions(includedBooks, userData) {
    let listData;
    if (userData.length === 0) {
        listData = '';
    }
    else if (!includedBooks.length) {
        userValue = inputBox.value;
        listData = '<li>Add a new book: ' + userValue + '</li>';
    }
    else {
        listData = includedBooks.join('');
        console.log(listData);
    }
    suggBox.innerHTML = listData;
}