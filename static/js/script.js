
$(document).ready(function () {
    $("#form").submit(function (event) {
        $(".form-group").removeClass("has-error");
        $(".help-block").remove();
        var formData = {
            titolo: $("#titolo").val(),
            autore: $("#autore").val(),
            tipo: $("#tipo").val(),
            stato: $("#stato").val(),
            pubblicazione: $("#pubblicazione").val(),
            pagine: $("#pagine").val(),
            prezzo: $("#prezzo").val(),
            inizio: $("#inizio").val(),
            fine: $("#fine").val(),
            note: $("#note").val(),
        };

        $.ajax({
            type: "POST",
            url: "/form",
            data: formData,
            dataType: "json",
            encode: true,
        }).done(function (data) {
            console.log(data);

            if (!data.success) {
                if (data.errors.titolo) {
                    $("#titolo-group").addClass("has-error");
                    $("#titolo-group").append(
                        '<div class="help-block">' + data.errors.titolo + "</div>"
                    );
                }

                if (data.errors.stato) {
                    $("#stato-group").addClass("has-error");
                    $("#stato-group").append(
                        '<div class="help-block">' + data.errors.stato + "</div>"
                    );
                }

                if (data.errors.tipo) {
                    $("#tipo-group").addClass("has-error");
                    $("#tipo-group").append(
                        '<div class="help-block">' + data.errors.tipo + "</div>"
                    );
                }
            } else {
                alert(data.message);
                $('#modal').modal('hide');
                $("#form").trigger("reset");
                $("#libri").append(
                    data.markup
                );
            }
        })      
        .fail(function (data) {
        $("#form").html(
          '<div class="alert alert-danger">Impossibile raggiungere il server.</div>'
        );
      });
        event.preventDefault();
    });

    $(".add-row").click(function () {
        var name = $("#name").val();
        var email = $("#email").val();
        var markup = "<tr><td><input type='checkbox' name='record'></td><td>" + name + "</td><td>" + email + "</td></tr>";
        $("table tbody").append(markup);
    });

    // Find and remove selected table rows
    $(".delete-row").click(function () {
        $("table tbody").find('input[name="record"]').each(function () {
            if ($(this).is(":checked")) {
                $(this).parents("tr").remove();
            }
        });
    });
    
    //
    $("li.elimina a:contains('Elimina')").click(function(){
        $.post("prova",
        {
            id: $(this).attr("value")
        },
        function(data,status){
            console.log(data);
            alert("Data: " + data.id);
        });
    });
});
