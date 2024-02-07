$(document).ready(function() {
    $('#id_card_number').mask('0000 0000 0000 0000');
    $('#id_expiration_date').mask('00/00');
    $('#id_security_code').mask('000');   

});

$('#id_card_number').on('keyup', function() {
    if ($(this).val().length < 5) {
        $('#svg_cc_type').attr('src', '/static/images/generic.svg');
        return false;
    }
    if ($(this).val().length < 5 || $(this).val().length > 6) return false;
    if ($(this).val().length == 19) {
        $('#id_expiration_date').focus();
        return false;
    }

    $.ajax({
        type: 'GET',
        url: '/supplier/get_cc_type',
        data: {
            'card_number': $(this).val().replace(/\s/g, '')
        },
        dataType: 'json',
        success: function(data) {
            $('#svg_cc_type').attr('src', '/static/images/' + data['cc_type'] + '.svg');
        },
        error: function(data){
            $('#svg_cc_type').attr('src', '/static/images/generic.svg');
        },
    });

});