// Datatables Customization
// remove and replace the default datatable searchbox
var katBrgySearchBox = $('#katBrgyTable').DataTable({
    "sDom": "tipr",
    "length": 10
});
$('#katBrgySearchBox').keyup(function() {
    katBrgySearchBox.search($(this).val()).draw();
})