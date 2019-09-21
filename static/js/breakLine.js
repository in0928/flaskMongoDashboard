document.addEventListener("DOMContentLoaded", breakLine());

function breakLine() {
    var cardText = document.getElementsByClassName("card-text")
    for (i=0; i < cardText.length; i++) {
        var text = cardText[i].innerHTML;
        var str = text.split("\n").join("<br/>");
        document.getElementsByClassName("card-text")[i].innerHTML = str;
    }
}

