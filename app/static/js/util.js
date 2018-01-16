//获取url中的参数
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
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