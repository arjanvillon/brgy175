    // Custom Toggle
    $('.toggleAnswer').click(function() {
        $(this).find('.btn').toggleClass('active');

        if ($(this).find('.btn-warning').length > 0) {
            $(this).find('.btn').toggleClass('btn-warning');
        }

        $(this).find('.btn').toggleClass('btn-default');
    });