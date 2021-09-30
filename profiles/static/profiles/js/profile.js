/* change default color of country field in profile */
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'rgb(44, 70, 43, 0.5)');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'rgb(44, 70, 43, 0.5)');
    } else {
        $(this).css('color', '#000');
    }
});