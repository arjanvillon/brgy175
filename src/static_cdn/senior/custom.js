// Datatables Customization
// remove and replace the default datatable searchbox
var katBrgySearchBox = $('#seniorTable').DataTable({
    "sDom": "tipr",
    "length": 10,
    "responsive": true
});
$('#seniorSearchBox').keyup(function() {
    katBrgySearchBox.search($(this).val()).draw();
})