function AddRow(id, n) {
  var t = document.getElementById(id);
  var fltrow = t.insertRow(0);
  var inpclass = "flt";
  for (var i = 0; i < n; i++) {
    var fltcell = fltrow.insertCell(i);
    var inp = document.createElement("input");
    inp.setAttribute("id", "flt" + i + "_" + id);
    inp.setAttribute("type", "text");
    inp.setAttribute("class", i == n - 1 ? "flt_s" : "flt");
    inp.setAttribute('placeholder', 'Filter');
    inp.addEventListener('keyup', Filter);
    fltcell.appendChild(inp);
  }
}