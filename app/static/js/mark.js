document.write("<script language=javascript src='/static/js/config.js'></script>");
function drawPointInPic(mark_div_list, point_list){
    var length = point_list.length;
    for(var i =0;i<length;i++){
        point= new Object();
        point.x = 20 + parseInt(point_list[i]['x']);
        point.y = 100 + parseInt(point_list[i]['y']);
        ret = SolidCircle(point.x,point.y,5,2,'red', i);
        point.circle = ret;
        idx = mark_div_list.length;
        mark_div_list.push(point);
        $("#mark_list").append("<li idx=" + idx + ">(" + point_list[i]['x'] + ',' + point_list[i]['y'] + ")<pre>" + coordinate_list[i]['x']+ coordinate_list[i]['y'] + coordinate_list[i]['z'] + "</li>");
    }
}
function preGeneratePoints(){
    video_name=getUrlParam('video_name')
    image_id=getUrlParam('image_id')
    $.ajax({
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            url: $SCRIPT_ROOT + '/simple/mark/getPrePoint',
            async: false,
            data: JSON.stringify({'video_name':video_name,'image_id':image_id}),
            dataType:'json',
            success: function(data){
                for(var i=0;i<mark_div_list.length;i++){
                     if(typeof(mark_div_list[i]) == 'undefined'){
                        console.log(i);
                        continue;
                    }
                    for(var j=0;j<mark_div_list[i].circle.length;j++){
                        document.body.removeChild(mark_div_list[i].circle[j]);
                    }
                }
                mark_list = data.mark_list;
                coordinate_list = data.coordinate_list;
                mark_div_list = [];
                $("#mark_list").empty();
                var offset =  $(".div1").offset();
                for(var j=0;j<mark_list.length;j++){
                    point= new Object();
                    point.x = mark_list[j].x + offset.left;
                    point.y = mark_list[j].y + offset.top;
                    ret = SolidCircle(point.x ,point.y, 5,2,COLOR_MARK,j);

                    point.circle = ret;
                    idx = mark_div_list.length;
                    mark_div_list.push(point);
                    $("#mark_list").append("<li style=''  idx=" + idx + ">(" + mark_list[j].x + ',' + mark_list[j].y + ")<pre>" + coordinate_list[j] + "</pre></li>");
                }
                green_point = -1;
            },
            error: function(data){
                console.log(data);
            }
        });
}

function getPointCoordinate(video_name, image_id, point_list){
    var ok = true;
    for(var i = 0;i<point_list.length;i++){

        $.ajax({
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            url: $SCRIPT_ROOT + '/simple/mark/check',
            async: false,
            data: JSON.stringify({'video_name':video_name,'image_id':image_id,'mark':point_list[i].y+','+point_list[i].x}),
            dataType:'json',
            success: function(data){
//                console.log(data);
//                console.log(data.ok == 'false');
                if (data.ok == 'false'){
//                    ok = false;
                    console.log('该点坐标有问题，请选择其他坐标');
                    return;
                }else{

                    ret = SolidCircle(WIDTH_OFFSET + point_list[i].x, HEIGHT_OFFSET + point_list[i].y, 5, 2, COLOR_LIGHT_MARK, coordinate_list.length);
                    point= new Object();
                    point.x = WIDTH_OFFSET + point_list[i].x;
                    point.y = HEIGHT_OFFSET + point_list[i].y;
                    point.circle = ret;
                    idx = mark_div_list.length;
                    mark_div_list.push(point);
                    mark_list.push({'x':point_list[i].x,'y':point_list[i].y});
                    coordinate_list.push({'x':data.coordinate[0],'y':data.coordinate[1],'z':data.coordinate[2]});
                    if (green_point != -1){
                        $("#mark_list li[idx="+green_point+"]").attr('style','');
                        for(var j =0;j<mark_div_list[green_point].circle.length;j++)
                            mark_div_list[green_point].circle[j].style.backgroundColor=COLOR_MARK;
                        //ret = SolidCircle(mark_div_list[green_point].x,mark_div_list[green_point].y,5,2,'red');
                    }
                    green_point = idx;
                    $("#mark_list").append("<li style='background-color:green;color:white'  idx=" + idx + ">(" + point_list[i].x + ',' + point_list[i].y + ")<pre>" + data.coordinate + "</li>");
                }
            },
            error: function(data){
                console.log(data);
            }
        });
    }

}