document.addEventListener("DOMContentLoaded", wrapper());

function wrapper(){
    checkRadioButton();
    selectDropdown();
    otherCheck();
}

function checkRadioButton(){
    var gender = document.getElementsByClassName("form-radio-buttons")[0].getAttribute("name");
    var radioButtons = document.getElementsByName("gender");

    switch(gender){
        case "F":
            var femaleButton = radioButtons[1];
            femaleButton.checked = true;
            break;
        case "O":
            var otherButton = radioButtons[2];
            otherButton.checked = true;
            break;
        default:
            var maleButton = radioButtons[0];
            maleButton.checked = true;
            break;
    }
}

function selectDropdown(){
    var status = document.getElementsByName("status")[0].getAttribute("class");
    console.log(status)
    var dropdown = document.getElementById("status-dropdown");
    var options = dropdown.options;
    var index = dropdown.selectIndex;

    for (i = 0; i < options.length; i++){
        if (status === options[i].text) {
            dropdown.selectedIndex = i.toString();
        }
        if (i === options.length -1) {
            dropdown.selectedIndex = i.toString();
        }
    }
}

function otherCheck() {
    var dropdown = document.getElementById("status-dropdown");
    if (dropdown.value === "others") {
        document.getElementById("input-status").style.display = "flex";
    } else {
        document.getElementById("input-status").style.display = "none";
    }
}