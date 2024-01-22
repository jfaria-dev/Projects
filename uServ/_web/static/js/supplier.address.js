$(document).ready(function () {           
    $('#id_postal_code').mask('00.000-000');
    $('#id_phone').mask('(00) 00000-0000');
    $('#loading').hide();
});

// Get address information by postal code
$('input[name=postal_code]').on('keyup', function () {
    if ($(this).val().length < 10) return false
    var postal_code = $(this).val().replace(/\D/g, '')
    
    $('#loading').show();
    setTimeout(function() {
        $.ajax({
            url: "/supplier/get_address_from_postal_code",
            type: 'GET',
            data: {
            postal_code: postal_code
            },
            dataType: 'json',
            async: false,
            success: function (data) {
                $('input[name=street').val(data['street'])
                $('input[name=neighborhood').val(data['neighborhood'])
                $('input[name=city').val(data['city'])
                $('input[name=state').val(data['state'])
                $('#loading').hide();

                $('input[name=number').focus()
            },
            error: function () {
            alert('Informe um CEP Válido.')
            }
        })
    }, 1500);
});