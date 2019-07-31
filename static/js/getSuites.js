function getSuites() {
    $.ajax({
        url: '/ajax/getSuites/',

        dataType: 'json',

        success: function (data) {
            $("#id_suites").empty();

             $(data.suites).each(function(index) {
                $("#id_suites").append('<option value="' + this.id + '">' + this.name + '</option>');
             });
        }
    });
}