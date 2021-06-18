function search(){
    var input = $("#input").value().toUpperCase()
    var items = $("td")

    for (i=0;i<items.length;i++){
        item= items[i].innerHTML.toUpperCase()
        if(item.indexOf(input)>1){
            item.style.display="";
        }else{
            item.style.display="none";

        }
    }
}