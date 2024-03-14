$(document).ready(function() {
    var phone_mask = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
    }, opt = {
        onKeyPress: function(val, e, field, options) {
            field.mask(phone_mask.apply({}, arguments), options);
            }
        };            
    $('#id_phone').mask(phone_mask, opt);
});

$('#id_email').on('keyup', function(){
    
    if ($(this).val().includes('@') == false) {
        $('#id_email').css('border-color', '#D1D5DB');
        $('#svg_id_email').attr('src', '/static/images/mail.svg');
        return false
    };            
    if ($(this).val().split('@')[1].length < 3) return false;                   
    
    $.ajax({
        type: "GET",
        url: "/supplier/validate_email",
        data: {
            'email':  $(this).val()
        },
        dataType: 'json',
        success: function (data) {
            if (data['exists']) {
                $('#svg_id_email').attr('src', '/static/images/mail-error.svg');
                $('#id_email').css('border-color', 'red');
                return false;
            }else{
                $('#id_email').css('border-color', 'green');
                $('#svg_id_email').attr('src', '/static/images/mail-check.svg');    
            }
        },
        error: function(){
            console.log('error');
        }
    });
});