$(document).ready(function () {
    $('#loading').hide();     
    console.log($('#id_birthdate').val());       
    const datepicker = flatpickr("input[name='birthdate']", {
        dateFormat: "d/m/Y", 
        locale: "pt", 
        allowInput: true,
        altFormat: "d/m/Y",
    });  
   
    $('#id_birthdate').mask('00/00/0000');
    $('#id_phone').mask('(00) 00000-0000');
    $('#id_company_document_number').mask('00.000.000/0000-00');
    $('#id_owner_document_number').mask('000.000.000-00');
    

    changeDocumentType();

    $('#id_company_document_number').focus();
});

$('#id_photo').on('change', function(event) {
    console.log('photo change');
    var input = event.target;
    var imagemPreview = $('<img id="image-preview" class="rounded-full">');
    var divImagePreview = $('div[for="image-icon"]');
    var arquivo = input.files[0];

    if (arquivo) {
        var leitor = new FileReader();
        leitor.onload = function() {
            aux = $('#id_photo').val().split("\\");
            name_preview = aux[aux.length - 1];
            $('#name-image-preview').text(name_preview);
            $('#name-image').show();
            imagemPreview.attr('src', leitor.result);
            imagemPreview.css('display', 'block');
            imagemPreview.css('width', '48px');
            imagemPreview.css('height', '48px');
            divImagePreview.html(imagemPreview);
        };
        leitor.readAsDataURL(arquivo);
    } else {
        imagemPreview.attr('src', '#');
        imagemPreview.css('display', 'none');
    }
});

$('#id_cnd').on('change', function(event) {
    var input = event.target;
    var filePreview = $('<i class="fa-solid fa-file-pdf text-purple-500 text-3xl"></i>');
    var divFilePreview = $('#file-icon');
    var arquivo = input.files[0];
    if (arquivo) {
        var leitor = new FileReader();
        leitor.onload = function() {
            aux = $('#id_cnd').val().split("\\");
            name_preview = aux[aux.length - 1];
            $('#name-file-preview').text(name_preview);
            $('#name-file').show();
            divFilePreview.html(filePreview);
        };
        leitor.readAsDataURL(arquivo);
    } else {
        filePreview.css('display', 'none');
    }
});

// Change labels in form according to document type
$('#id_document_type').on('change', function(){
    changeDocumentType();

});

// Change labels in form according to document type
function changeDocumentType(){
    var doc_type = $('#id_document_type').val()
    if (doc_type == 'CPF'){
        $('#id_company_document_number').mask('000.000.000-00').attr('placeholder', '000.000.000-00').val('').focus();
        $('#label_company_document').text('CPF');
        $('#label_company_name').text('Nome do Profissional');
        $('#id_birthdate').attr('disabled', false);
        $('#div_birthdate').show();
    }else{
        $('#id_company_document_number').mask('00.000.000/0000-00').attr('placeholder', '00.000.000/0000-00').val('').focus();
        $('#label_company_document').text('CNPJ');
        $('#label_company_name').text('Nome da Empresa');
        $('#id_birthdate').attr('disabled', true);
        $('#div_birthdate').hide();

    }
}

// Get company information by document number
function GetCompanyInformation(){
    if ($('#id_company_document_number').val().length < 18) return false;  
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
                $('#id_company_name').val(data['nome']);
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

// Get professional information by document number
function GetProfessionalInformation(){
    if ($('#id_company_document_number').val().length < 14) return false;
    if ($('#id_birthdate').val().length < 10) return false;
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
                $('#id_company_name_show').focus();
            },
            error: function() {
                alert('Informe um CPF e Data de Nascimento Válido.'); // TROCAR PARA MODAL MESSAGE
                $('#loading').hide();
                $('input').not('#id_company_name').attr('disabled', false);
            }
        });
    }, 1500)     
}

$('#id_company_document_number').on('keyup', function () {
    console.log('key up');
    console.log($('#id_document_type').val());
    console.log($('#id_company_document_number').val());
    if ($('#id_document_type').val() == 'CPF'){
        GetProfessionalInformation();
    }else{
        GetCompanyInformation();
    }
    
})

// Get owner information by document number
$('#id_birthdate').on('change', function() {        
    GetProfessionalInformation();
});

$('form').submit(function (e) {
    $('#loading').show();
    $('input[type="text"]').removeAttr('disabled')
})


