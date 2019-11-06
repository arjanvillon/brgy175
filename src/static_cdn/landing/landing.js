showEditor() {
    $("#EditModal").modal("show");
    $("#EditModal").appendTo("body");
}

ngOnDestroy(){
  $("body>#EditModal").remove();
}