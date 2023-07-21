function getIp(callback) {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.ipify.org/?format=json', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            callback(xhr.responseText);
        }
    }
    xhr.send();
}

getIp(function (content) {
    var node = document.getElementById('ipAddress')
    var js_data = JSON.parse(content)
    console.log(js_data.ip)
    node.innerHTML = js_data.ip
})
