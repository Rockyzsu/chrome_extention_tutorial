function Update() {
  console.log("start to change table");
  var table = document.getElementById("flex_stock");
  var row = table.rows; // Getting the rows
  console.log(row.length);
  let deleteRow = [];
  for (var i = 1; i < row.length; i++) {
    console.log(row[i].cells[4].textContent);
    if (row[i].cells[5].textContent < 100) {
    //   table.deleteRow(i);
    // console.log("delete row");
    deleteRow.push(i);
    }
  }

    for (var i = 0; i < deleteRow.length; i++) {
        console.log(deleteRow[i])
        table.deleteRow(deleteRow[i]);
    }
}

Update();
