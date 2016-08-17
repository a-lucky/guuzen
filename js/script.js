var guuzen = [];

function data_append(data, i){
    if(i >= data['texts'].length) return;
    var is_exist = false;
    for(var x in guuzen){
        if(data['texts'][i][0] == guuzen[x][0]) {
            is_exist = true;
            break;
        }
    }
    if(is_exist){
        data_append(data, i+1);
        return;
    }

    guuzen.push(data['texts'][i]);
    var app = "";
    for(var j in data['texts'][i]){
        app += '<span>'+data['texts'][i][j]+'</span>';
    }
    $('#vert').append('<div class="element"><p>'+app+'</p></div>');
    $('#main').animate( {scrollLeft: 0}, 900, function(){
        data_append(data, i+1);
    });
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
    setInterval( function(){
        getGuuzen();
    },10000);
});

