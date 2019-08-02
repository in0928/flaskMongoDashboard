document.querySelector("#people-search").oninput = applySearch;

function applySearch() {
    search();
    alternate();
}


function search() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("people-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("people-list")
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


function alternate(){
  if(document.getElementsByTagName){
    var table = document.getElementById("people-list")
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

