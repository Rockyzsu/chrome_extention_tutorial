function httpRequest(url,callback){

    var xhr = new XMLHttpRequest();
    xhr.open('GET',url,true)
    xhr.onreadystatechange=function(){
        if(xhr.readyState==4){
            callback(xhr.responseText);
        }
    }
    xhr.send();
    console.log('send');
}

function renderHTML(content){
    console.log('render')
    var result = JSON.parse(content);
    var ip = result['prompt'];
    console.info(ip);
    txt = document.getElementById('ip')
    txt.innerHTML = ip;
}

function bondTable(content){
    var result = JSON.parse(content);
    data = result['rows']
    var table = '<table><tr><th>转债代码</th><th>转债名称</th><th>涨跌幅</th></tr>'
    for (var i in data){
        table+='<tr>'
        table+='<td>'+data[i]['cell']['bond_id']+'</td>'
        table+='<td>'+data[i]['cell']['bond_nm']+'</td>'
        table+='<td>'+data[i]['cell']['increase_rt']+'</td>'
        table+='</tr>'
    }

    table+='</table>'
    document.getElementById('table').innerHTML = table
}
var url = 'https://www.jisilu.cn/data/cbnew/cb_list_new/?___jsl=LST___t=1689663194990';
httpRequest(url,bondTable);