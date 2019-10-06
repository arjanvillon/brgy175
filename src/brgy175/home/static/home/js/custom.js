$(document).ready(function() {

    /* ---------------------------------------------------
    INITIALIZATIONS
    ----------------------------------------------------- */
    // Datepicker
    $('.datepicker').datepicker();

    // Select2
    $('.select2').select2();


    // Main SideBar
    $('#sidebarCollapse').on('click', function() {
        $('#mainSidebar').toggleClass('active');
        $(this).toggleClass('active');
    });

    // Datatables Customization
    // remove and replace the default datatable searchbox
    var katBrgySearchBox = $('#changethis').DataTable({
        "sDom": "tipr",
        "length": 10
    });

    $('#changethisSearchBox').keyup(function() {
        katBrgySearchBox.search($(this).val()).draw();
    })

    // VALIDATIONS
    // check if empty


    function display_c() {
        var refresh = 1000; // Refresh rate in milli seconds
        mytime = setTimeout('display_time()', refresh)
    }

    function display_time() {
        var x = new Date()
        document.getElementById('timeBar').innerHTML = x;
        display_c();
    }

});
$(function() {
    $('input').attr('autocomplete','off');

    var pillTab = $(".tabSwitch");
    pillTab.find(".pillTab").on("click", function() {
        var $this = $(this);

        if ($this.hasClass("active")) return;

        var direction = $this.attr("pillTab-direction");

        pillTab.removeClass("left right").addClass(direction);
        pillTab.find(".pillTab.active").removeClass("active");
        $this.addClass("active");
    });

});