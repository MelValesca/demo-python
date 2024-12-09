// Cette fonction utilise un bubble sort.
function trierParNom() {
  var table;
  var rows;
  var i, y, x;
  var shouldSwitch;
  var switching = true;

  table = document.getElementById("table");
  // condition pour controler la boucle while de trie tant qu'il y a des données à trier
  while (switching) {
    // On suppose que toutes les données ont été déjà triées
    switching = false;
    rows = table.rows;

    for (i = 1; i < rows.length - 1; i++) {
      // On suppose que les cellules x et y ne doivent pas être interchangées
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("td")[0];
      y = rows[i + 1].getElementsByTagName("td")[0];

      if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
        shouldSwitch = true;
        break;
      }
    }

    if (shouldSwitch) {
      // le parent de td est tr
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}
