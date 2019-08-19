document.addEventListener("DOMContentLoaded", modifyCards());

function modifyCards(){
    colorCards();
    giveClass();
}

function colorCards(){
    var panePeople, cardsPeople, paneBA, cardsBA, paneNotes, cardsNotes;
    panePeople = document.getElementById("people")
    paneBA = document.getElementById("ba")
    paneNotes = document.getElementById("notes")

    cardsPeople = panePeople.getElementsByClassName("card")
    for(i = 0; i < cardsPeople.length ;i++){
        if(i % 2 == 1){
            cardsPeople[i].style.background = "antiquewhite";
        }
    }

    cardsBA = paneBA.getElementsByClassName("card")
    for(i = 0; i < cardsBA.length ;i++){
        if(i % 2 == 1){
            cardsBA[i].style.background = "#cbf0fc";
        }
    }

    cardsNotes = paneNotes.getElementsByClassName("card")
    for(i = 0; i < cardsNotes.length ;i++){
        if(i % 2 == 1){
            cardsNotes[i].style.background = "mistyrose";
        }
    }
}


function giveClass(){
    var stars = document.getElementsByClassName("star");
    var cards = document.getElementsByClassName("card");
    for(i = 0; i < stars.length; i++){
        stars[i].classList.add("favorite");
    }
}

function toggleIcon(target) {
    target.classList.toggle('favorite');
    target.classList.toggle('non-favorite');
}


