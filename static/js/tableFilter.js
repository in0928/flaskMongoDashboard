document.querySelector("#union-name-dropdown").onchange = applyFilter;

function applyFilter() {
    filter();
    alternate();
}


function filter() {
    // Declare variables
    var selection, filter, table, tr, td, i, txtValue;
    selection = document.getElementById("union-name-dropdown");
    filter = selection.value.toUpperCase();
    table = document.getElementById("com-schedule")
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.innerText;
//          reset the display style
            console.log("I got reset")
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }
        }
    }
}

function changeRowColor() {
    document.querySelector("tr:nth-of-type(even)").style.backgroundColor = "red";
}

function alternate(){
 console.log("something")
  if(document.getElementsByTagName){
    var table = document.getElementById("com-schedule");
    var rows = table.getElementsByTagName("tr");
    for(i = 0; i < rows.length; i++) {
        if(rows.style.display != 'none'){
        }
        var filteredRows.push()
    }
    var filteredRows = rows.style.display != 'none';
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

