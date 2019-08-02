document.addEventListener("DOMContentLoaded", fill_dropdown(getId()));
document.querySelector("#table-search").oninput = applySearch;

//get tableId
function getId() {
    var element = document.querySelector(".table-striped")
    var id = element.id;
    return id;
}

tableId = getId();
//if(tableId === "dream-list"){
//
//}

function applySearch() {
    search();
    alternate();
}


function fill_dropdown() {
//    get col names
    console.log("i am called")
    var table = document.getElementsByClassName("table-responsive")[0];
    var th = table.getElementsByTagName("th");
//    get dropdown menu
    var dropdown = document.getElementById("search-by-col-name");
    console.log(dropdown);
    for(i = 0; i < th.length; i++) {
        opt = document.createElement("option")
        opt.appendChild(document.createTextNode(th[i].innerText))
        dropdown.appendChild(opt)
    }
}

function search(tableId) {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("table-search");
    filter = input.value.toUpperCase();
    table = document.getElementById(tableId)
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }
        }
    }
}


function alternate(tableId){
  if(document.getElementsByTagName){
    var table = document.getElementById(tableId)
    var rows = table.getElementsByTagName("tr");
    var filteredRows = []
    for(i = 0; i < rows.length; i++) {
        if(rows[i].style.display != 'none'){
            filteredRows.push(rows[i])
        }
    }
    console.log(filteredRows)
    for(i = 1; i < filteredRows.length; i++){
  //manipulate rows
      if(i % 2 == 0){
        filteredRows[i].style.background = "whitesmoke";
      }else {
        filteredRows[i].style.background = "white";
      }
    }
  }
}

