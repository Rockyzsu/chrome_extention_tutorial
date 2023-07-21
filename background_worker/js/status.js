function httpRequest(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true)
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            callback(true)
        }

    }
    xhr.onerror = function () {
        callback(true)
    };

    xhr.send();
}
var url = "https://kaihu51.com/"
setInterval(httpRequest(url, function (status) {
    alert("World")
    if (status) {
        chrome.browserAction.setIcon({ path: 'image/online.png' })
    } else {
        chrome.browserAction.setIcon({ path: 'image/offline.png' })

    }
}), 5000)