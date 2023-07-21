function getIp(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            callback(xhr.responseText); 
        }

    }
    xhr.send();
}

myip = getIp()
var url = 'https://kaihu51.com/ip.txt'
getIp(url, function(ip) {
    var node = document.getElementById('ip');
    node.innerHTML = ip;
})