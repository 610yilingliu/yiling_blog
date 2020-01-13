function add_shadow(elem){
    $(elem).css("filter","drop-shadow(2px 2px 1px black)");
    $(elem).css("color","black")
}

function rm_shadow(elem){
    $(elem).css("filter","drop-shadow(0px 0px 0px white)")
}

function selected(elem){
    $(elem).css("background-color","rgb(240, 240, 240)")
}

function unselected(elem){
    $(elem).css("background-color","white")
}

function on_current(tag_id){
    var tag=document.getElementById(tag_id);
    tag.classList.add("active");
}