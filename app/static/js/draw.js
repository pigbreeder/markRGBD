document.write("<script language=javascript src='/static/js/mark.js'></script>");
document.write("<script language=javascript src='/static/js/config.js'></script>");

function line(startX, startY, endX, endY, container) {
    if (startX == endX) {
        if (startY > endY) {
            var tempY = startY;
            startY = endY;
            endY = tempY;
        }
        for (var k = startY; k < endY; k++) {
            createPoint(container, startX, k);
        }
    }
    // y = ax + b
    var a = (startY - endY) / (startX - endX);
    var b = startY - ((startY - endY) / (startX - endX)) * startX;
    if (Math.abs(startX - endX) > Math.abs(startY - endY)) {
        if (startX > endX) {
            var tempX = endX;
            endX = startX;
            startX = tempX;
        }
        var left = container.style.left;
        var top = container.style.top;
        for (var i = startX; i <= endX; i++) {
            createPoint(container, i, a * i + b);
        }
    } else {
        if (startY > endY) {
            var tempY = startY;
            startY = endY;
            endY = tempY;
        }
        for (var j = startY; j <= endY; j++) {
            createPoint(container, (j - b) / a, j);
        }
    }

}

function createPoint(container, x, y) {
    var node = document.createElement('div');
    node.className = 'line';
    node.style.marginTop = y;
    node.style.marginLeft = x;
    container.appendChild(node);
}

// input: 4 points, height slice , width slice
// output: cross_lst
// test case:point_lst=[{'x':0,'y':0},{'x':0,'y':100},{'x':100,'y':0},{'x':100,'y':100}];height_slice=3;width_slice=3;
// test case:point_lst=[{'x':0,'y':0},{'x':80,'y':100},{'x':100,'y':0},{'x':180,'y':100}];height_slice=3;width_slice=3;
function generatePoints(){
    height_slice= $("input[name='height_slice']").val();
    width_slice= $("input[name='width_slice']").val();
    console.log(height_slice,width_slice);
    console.log(typeof(height_slice),width_slice);
    if(mark_list.length != 4){
        alert('请先选择四个标定点');
        return;
    }
    point_list = mark_list.slice();
    $("#reset_mark").click();
    point_list = calcCrossPoint(point_list,parseInt(height_slice),parseInt(width_slice));
//    console.log(point_list);
//    getPointCoordinate(video_name, image_id, point_list);
    for(var i = 0;i<point_list.length;i++){
        ret = SolidCircle(WIDTH_OFFSET + point_list[i].x, HEIGHT_OFFSET + point_list[i].y, 5, 2, COLOR_LIGHT_MARK, i);
        point= new Object();
        point.x = WIDTH_OFFSET + point_list[i].x;
        point.y = HEIGHT_OFFSET + point_list[i].y;
        point.circle = ret;
        idx = mark_div_list.length;
        mark_div_list.push(point);
        mark_list.push({'x':point_list[i].x,'y':point_list[i].y});
//        coordinate_list.push({'x':data.coordinate[0],'y':data.coordinate[1],'z':data.coordinate[2]});
        if (green_point != -1){
            $("#mark_list li[idx="+green_point+"]").attr('style','');
            for(var j =0;j<mark_div_list[green_point].circle.length;j++)
                mark_div_list[green_point].circle[j].style.backgroundColor=COLOR_MARK;
            //ret = SolidCircle(mark_div_list[green_point].x,mark_div_list[green_point].y,5,2,'red');
        }
        green_point = idx;
        $("#mark_list").append("<li style='background-color:green;color:white'  idx=" + idx + ">(" + point_list[i].x + ',' + point_list[i].y + ")<pre>" + "</li>");
    }

}
function calcCrossPoint(point_lst, height_slice, width_slice) {
    // LU, LB, RU RB
    cross_lst =[];
    height_count = height_slice;
    width_count = width_slice;
    height_slice -= 1;
    width_slice -= 1;
    // 间隔要少一份，才能刚好对应上
    // 4点2线交点

    for(var i = 0;i<height_count;i++){
        cur_l_y = point_lst[0].y - (point_lst[0].y - point_lst[1].y)/height_slice * i;
        cur_l_x = point_lst[0].x - (point_lst[0].x - point_lst[1].x)/height_slice * i;

        cur_r_y = point_lst[2].y - (point_lst[2].y - point_lst[3].y)/height_slice * i;
        cur_r_x = point_lst[2].x - (point_lst[2].x - point_lst[3].x)/height_slice * i;
        // 计算直线
        cur_lr_a = cur_l_y - cur_r_y;
        cur_lr_b = cur_r_x - cur_l_x;
        cur_lr_c = cur_l_x * cur_r_y - cur_l_y * cur_r_x;

//        console.log(cur_l_y,cur_l_x,cur_r_y,cur_r_x);
//        console.log(cur_lr_a,cur_lr_b,cur_lr_c);
//        console.log('======')
        for(var j =0;j<width_count;j++){
            cur_u_y = point_lst[0].y - (point_lst[0].y - point_lst[2].y)/width_slice * j;
            cur_u_x = point_lst[0].x - (point_lst[0].x - point_lst[2].x)/width_slice * j;

            cur_b_y = point_lst[1].y - (point_lst[1].y - point_lst[3].y)/width_slice * j;
            cur_b_x = point_lst[1].x - (point_lst[1].x - point_lst[3].x)/width_slice * j;
            // 计算直线
            cur_ub_a = cur_u_y - cur_b_y;
            cur_ub_b = cur_b_x - cur_u_x;
            cur_ub_c = cur_u_x * cur_b_y - cur_u_y * cur_b_x;

            D = cur_lr_a * cur_ub_b - cur_ub_a * cur_lr_b;
            cross_x = (cur_lr_b * cur_ub_c - cur_ub_b * cur_lr_c) / D;
            cross_y = (cur_ub_a * cur_lr_c - cur_lr_a * cur_ub_c) / D;
            cross_lst.push({'x':parseInt(cross_x), 'y':parseInt(cross_y)});
//            console.log(cur_u_y,cur_u_x,cur_b_y,cur_b_x);
//            console.log(cur_ub_a,cur_ub_b,cur_ub_c,D);
        }
    }
    return cross_lst;
}