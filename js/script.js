var guuzen = [];

function data_append(data, i){
    if(i >= data['lists'].length) return;
    var is_exist = false;
    for(var x in guuzen){
        if(data['lists'][i]['text'][0] == guuzen[x][0]) {
            is_exist = true;
            break;
        }
    }
    if(is_exist){
        data_append(data, i+1);
        return;
    }

    guuzen.push(data['lists'][i]['text']);
    var app = '<a href=https://twitter.com/intent/tweet?text='
            + data['lists'][i]['text'].join("%0a")
            + '%0a&hashtags=偶然詩歌'
            + '&via=' + data['lists'][i]['name']
            + '&url=' + data['lists'][i]['url']
            + ' onClick="window.open(encodeURI(decodeURI(this.href)), \'tweetwindow\', \'width=650, height=470, personalbar=0, toolbar=0, scrollbars=1, sizable=1\'); return false;" rel="nofollow" >';
    for(var j in data['lists'][i]['text']){
        app += '<span>'+data['lists'][i]['text'][j]+'</span>';
    }
    app += '</a>'
    
    name = data['lists'][i]['name'].replace(/[A-Za-z0-9]/g, function(s) {
        return String.fromCharCode(s.charCodeAt(0) + 0xFEE0);
    })
    app += '<div class="sign">'
        + '<a href=' + data['lists'][i]['url'] 
        +' target="_blank" rel="nofollow">'
            + '＠' + name
            + '<img src="' + data['lists'][i]['img'] +'"/>'
        + '</a>'
        + '</div>';
        
    console.log(app);
    
    $('#vert').append('<div class="element"><div class="text">'+app+'</div></div>');
    if($("#checkbox").prop("checked")) {
        $('#main').animate( {scrollLeft: 0}, 900, function(){
            data_append(data, i+1);
        });
    } else {
        setTimeout(function(){
            data_append(data, i+1);
        },900);
    }
    
};

function getGuuzen() {
    $.getJSON('./guuzen.json', null,
        function(data, status){

            console.log(data);
            data_append(data, 0);
//            for(var i in data['texts']){
//                var is_exist = false;
//                for(var x in guuzen){
//                    if(data['texts'][i][0] == guuzen[x][0]) {
//                        is_exist = true;
//                        break;
//                    }
//                }
//                if(is_exist) continue;
//                
//                guuzen.push(data['texts'][i]);
//                var app = "";
//                for(var j in data['texts'][i]){
//                    app += '<span>'+data['texts'][i][j]+'</span>';
//                }
//                $('#vert').append('<div class="element"><p>'+app+'</p></div>');
//                $('#main').animate( {scrollLeft: 0}, 500);
//            }
        });
};

$(function (){
//    getGuuzen();
    $("#checkbox").prop("checked", true);
    $('#main').animate( {scrollLeft: 0}, 900);
    setInterval( function(){
        getGuuzen();
    },10000);
});

