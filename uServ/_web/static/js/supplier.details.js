$(document).ready(function () {
    $('#loading').hide();            
    const datepicker = flatpickr("#id_birthdate", {
        dateFormat: "d/m/Y", 
        locale: "pt", 
        allowInput: true
    });            
    $('#id_phone').mask('(00) 00000-0000');
    $('#id_company_phone').mask('(00) 00000-0000');
    $('#id_company_document_number').mask('00.000.000/0000-00');
    $('#id_owner_document_number').mask('000.000.000-00');
    // $('#id_company_document_type').change();
    $('#id_company_document_number').focus();
})

// Change labels in form according to document type
$('#id_document_type').on('change', function(){
    var doc_type = $(this).val()
    if (doc_type == 'CPF'){
        $('#id_company_document_number').mask('000.000.000-00').attr('placeholder', '000.000.000-00');
        $('label[for="id_company_document_number"]').text('CPF');
        $('label[for="id_company_name"]').text('Nome do Profissional');
        $('label[for="id_company_phone"]').text('Telefone do Profissional');
        $('label[for="id_birthdate"]').text('Data de Nascimento');
        $('#id_birthdate').attr('disabled', false);

    }else{
        $('#id_company_document_number').mask('00.000.000/0000-00').attr('placeholder', '00.000.000/0000-00');
        $('label[for="id_company_document_number"]').text('CNPJ');
        $('label[for="id_company_name"]').text('Nome da Empresa');
        $('label[for="id_company_phone"]').text('Telefone da Empresa');
        $('label[for="id_birthdate"]').text('Data da Constituição');
        $('#id_birthdate').attr('disabled', true);
    }
    var token = $('input[name="csrfmiddlewaretoken"]').val()
    $('input').not('#id_owner_name').val('');
    $('input[name="csrfmiddlewaretoken"]').val(token)

});

// Get company/professional information by document number
function GetCompanyInformation(origem=null){
    if ($('#id_company_document_type').val() == 'CPF'){
        if ($('#id_company_document_number').val().length < 14) return false;
        $('#id_birthdate').click().focus();
        return false;
    }else{
        if ($('#id_company_document_number').val().length < 18) return false;
    }
    var company_document_number = $('#id_company_document_number').val().replace(/\D/g, '')
    
    $('#loading').show();//your code to be executed after 1 second
    $('input').attr('disabled', true);
    setTimeout(function() {
        $.ajax({
            url: "/supplier/get_company_from_document",
            type: 'GET',
            data: {
                company_document_number: company_document_number
            },
            dataType: 'json',
            async: false,
            success: function (data) {
                $('#id_postal_code').val(data['cep']);
                $('#id_street').val(data['logradouro']);
                $('#id_number').val(data['numero']);
                $('#id_complement').val(data['complemento']);
                $('#id_neighborhood').val(data['bairro']);
                $('#id_city').val(data['municipio']);
                $('#id_state').val(data['uf']);
            
                $('#id_company_name').val(data['nome']);
                $('#id_company_phone').val(data['telefone']);
                $('#id_birthdate').val(data['data_situacao']);
                
                $('input').not('#id_company_name').attr('disabled', false);
                $('#loading').hide();

                $('#id_company_name_show').val(data['fantasia']).focus()
            },
            error: function () {
                alert('Informe um Cnpj Válido.'); // TROCAR PARA MODAL MESSAGE
                $('input').not('#id_company_name').attr('disabled', false);
                $('#loading').hide();

            }
        })
    }, 1500);
}

$('#id_company_document_number').on('keyup', function () {
    GetCompanyInformation();
})

// Get owner information by document number
$('#id_birthdate').on('change', function() {        
    if ($('#id_company_document_number').val().length < 14) return false;
    if ($('#id_company_document_type').val() == 'CNPJ') return false;
    if ($('#id_birthdate').val().split('/')[2] < 1940 || $('#id_birthdate').val().split('/')[2] > 2100){
        alert('Informe um ano acima de 1940 e menor que 2100.'); // TROCAR PARA MODAL MESSAGE
        return false;
    }
    var company_document_number = $('#id_company_document_number').val().replace(/\D/g,'');
    var birthdate = $('#id_birthdate').val().replaceAll('/','-');
    $('#loading').show();  
    setTimeout(function(){
        $.ajax({
            url: "/supplier/get_professional_from_document",
            type: "GET",
            data: {
                'document_number': company_document_number,
                'birthdate': birthdate
            },
            dataType: "json",
            async: false,
            success: function(data) {  
                $('#id_company_name').val(data['nome']);
                $('#loading').hide();
                $('input').not('#id_company_name').attr('disabled', false);
                $('#id_company_phone').focus();
            },
            error: function() {
                alert('Informe um CPF e Data de Nascimento Válido.'); // TROCAR PARA MODAL MESSAGE
                $('#loading').hide();
                $('input').not('#id_company_name').attr('disabled', false);
            }
        });
    }, 1500)            
});

// Get address information by postal code
$('input[name=postal_code]').on('keyup', function () {
    if ($(this).val().length < 10) return false
    //if ($('#manual').is(':checked')) {
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
    //}
})

$('form').submit(function (e) {
    $('#loading').show();
    $('input[type="text"]').removeAttr('disabled')
})


