//获取url中的参数
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}
function movePixels(){
    batch_op = $("input[name='batch_op']").val();
    pixel_val = Number($("input[name='pixel_val']").val());
    if($("input[name='batch_op']").val().indexOf('-') != -1){
        step = 1;
        arr = $("input[name='batch_op']").val().split('-');
        st = Number(arr[0]);
        ed = Number(arr[1]);
    }else{
        step = 10;
        arr = $("input[name='batch_op']").val().split(',');
        st = Number(arr[0]);
        ed = Number(arr[1]);
    }
    for(var i=st;i<=ed;i+=step){
        if($("#move_updown_forward").is(":checked")==true)
            mark_list[i]['y'] += pixel_val;
        else
            mark_list[i]['x'] += pixel_val;
        $("#mark_list li[idx="+i+']').html("(" + mark_list[i]['x'] + ',' + mark_list[i]['y'] + ")");
        for(var j=0;j<mark_div_list[i].circle.length;j++){
            document.body.removeChild(mark_div_list[i].circle[j]);
        }
        delete mark_div_list[i];
        point= new Object();
        point.x = WIDTH_OFFSET + parseInt(mark_list[i]['x']);
        point.y = HEIGHT_OFFSET + parseInt(mark_list[i]['y']);
        ret = SolidCircle(point.x,point.y,5,2,COLOR_MARK, i);
        point.circle = ret;
        mark_div_list[i] = point;
    }
}
// 绘制标记点
function SolidCircle(cx, cy, r, p, color, idx){
    var s = 1/(r/p);
    ret = new Array();
    for (var i = 0; i < Math.PI*2; i+=s) {
        div = document.createElement("div");
        ret.push(div);
        div.style.position = "absolute";
        div.style.left = Math.sin(i)*r+cx+"px";
        div.style.top = Math.cos(i)*r+cy+"px";
        div.style.width = p+"px";
        div.style.height = p+"px";
        div.style.backgroundColor = color;
        if (i == CIRCLE_IDX_LOC){

            if(SWITCH_SHOW_MARK_IDX){
                div.style.color = COLOR_MARK_IDX;
                div.innerHTML = idx;
            }
        }
        document.body.appendChild(div);
    }
    return ret;
}