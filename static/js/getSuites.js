function getSuites() {
    $.ajax({
        url: '/ajax/getSuites/',

        dataType: 'json',

        success: function (data) {
            $("#id_suites").empty();

            var select;
             $(data.suites).each(function(index) {
                if ($("#id_suite_select").val() == this.id) {
                    select = " selected";
                }
                else {
                    select = "";
                }
                $("#id_suites").append('<option value="' + this.id + '"' + select + '>' + this.name + '</option>');
             });
        }
    });
}