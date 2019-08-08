document.addEventListener("DOMContentLoaded", colorCards());



function colorCards(){
    var pane = document.getElementById("people")
// TODO: add id as a variable
    var cards = pane.getElementsByClassName("card")
    for(i = 0; i < cards.length ;i++){
        if(i % 2 == 0){
            cards[i].style.background = "antiquewhite";
        }
        else{
            cards[i].style.background = "lightgoldenrodyellow";
        }
    }
}