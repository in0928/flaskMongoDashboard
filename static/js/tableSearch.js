//document.addEventListener("DOMContentLoaded", fill_dropdown(tableId));


//get tableId
$(document).ready(function(){
    var tableId = "people-list";
    fill_dropdown(tableId);
    $('.nav-tabs a').on('shown.bs.tab', function(event){
        var tableLabel = $(event.target).text();
        switch(tableLabel){
            case "BA":
                tableId = "ba-list";
                break;
            case "My Dreams":
                tableId = "dream-list";
                break;
            case "Restaurants & Bars":
                tableId = "restaurants-bars-list";
                break;
            default:
                tableId = "people-list"
        };
        fill_dropdown(tableId);
        });
    });

document.querySelector("#table-search").oninput = applySearch;

function applySearch() {
    search();
    alternate();
}


function fill_dropdown(tableId) {
//    get col names

    var table = document.getElementById(tableId);
    var th = table.getElementsByTagName("th");
//    get dropdown menu
    var dropdown = document.getElementById("search-by-col-name");
    dropdown.options.length = 0;

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

