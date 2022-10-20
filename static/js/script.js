
$(document).ready(function () {
    $("#form-modal").submit(function (event) {
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
                $(".modal-body #form-modal").trigger("reset");
                $("#libri").append(
                    data.markup
                );
            }
        })      
        .fail(function (data) {
        $("#form-modal").html(
          '<div class="alert alert-danger">Impossibile raggiungere il server.</div>'
        );
      });
        event.preventDefault();
    });

   $("#libri").on("click","li.modifica .dropdown-item",function(){
        $('#modal').modal('show')
        $(".modal-body #btn_modifica").hide();
        $(".modal-body #btn_submit").show();
       $(".modal-body #btn_c_modifica").hide();
    });

    
    
    //CACELLA il libro dalla lista e dal database
    $("#libri").on("click","li.elimina .dropdown-item",function(){
        if (confirm("Vuoi cancellare il libro?") == true) {
            $.post("cancella",{
                id: $(this).parent().parent().data("id")
            },
            function(data,status){
                console.log(data);
                $(data.codice).remove()
                alert('libro cancellato');
            }); 
        } else { 
            alert('libro non cancellato');
        }
    });

    //MOSTRA le informazioni del libro in questione
    $("#libri").on("click","li.info .dropdown-item",function(){
        $.post("info",{
            id: $(this).parent().parent().data("id")
        },
        function(data,status){
            console.log(data);
            $(".modal-header #exampleModalLabel").text("Modifica libro");
            $(".modal-body #form-modal").data("id",data.id)
            alert($(".modal-body #form-modal").data("id"))
            $(".modal-body :input").prop( "disabled", true );
            $(".modal-body button").prop( "disabled", false );
            $(".modal-body #btn_submit").hide();
            $(".modal-body #btn_modifica").show();
            $(".modal-body #btn_c_modifica").hide();
            $(".modal-body #titolo").val(data.titolo);
            $(".modal-body #autore").val(data.autore);
            $(".modal-body #tipo").val(data.tipo);
            $(".modal-body #stato").val(data.stato);
            $(".modal-body #pubblicazione").val(data.pubblicazione);
            $(".modal-body #pagine").val(data.pagine);
            $(".modal-body #prezzo").val(data.prezzo);
            $(".modal-body #inizio").val(data.inizio);
            $(".modal-body #fine").val(data.fine);
            $(".modal-body #note").val(data.note);
        }); 
    });

    //MODIFICA le informazioni del libro in questione
    $("#libri").on("click","li.modifica .dropdown-item",function(){
        $.post("info",{
            id: $(this).parent().parent().data("id")
        },
        function(data,status){
            console.log(data);
            alert(data.id)
            $(".modal-header #exampleModalLabel").text("Informazioni libro");
            $(".modal-body #form-modal").data("id",data.id)
            //$(".modal-body :input").prop( "disabled", true );
            //$(".modal-body button").prop( "disabled", false );
            $(".modal-body #btn_submit").hide();
            $(".modal-body #btn_modifica").hide();
            $(".modal-body #btn_c_modifica").show();
            $(".modal-body #titolo").val(data.titolo);
            $(".modal-body #autore").val(data.autore);
            $(".modal-body #tipo").val(data.tipo);
            $(".modal-body #stato").val(data.stato);
            $(".modal-body #pubblicazione").val(data.pubblicazione);
            $(".modal-body #pagine").val(data.pagine);
            $(".modal-body #prezzo").val(data.prezzo);
            $(".modal-body #inizio").val(data.inizio);
            $(".modal-body #fine").val(data.fine);
            $(".modal-body #note").val(data.note);
        }); 
    });

    $("#btn_add").click(function () {
        $('#modal').modal('show')
        $(".modal-body #btn_modifica").hide();
        $(".modal-body #btn_submit").show();
        $(".modal-body #btn_c_modifica").hide();
    });

    $('#modal').on('hidden.bs.modal', function () {
        $(".modal-body #form-modal").trigger("reset");
        $(".modal-body :input").prop( "disabled", false );
    })

    $("#btn_modifica").click(function () {
        alert("ciao");
        //$('#modal').modal('show')
        //$(".modal-body #btn_modifica").hide();
        //$(".modal-body #btn_submit").show();
    });

    $("#btn_c_modifica").click(function () {
        if (confirm("Vuoi modificare il libro?") == true) {
            $.post("modifica",{
                id: $(".modal-body #form-modal").data("id"),
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
            },
            function(data,status){
                console.log(data);
                if($('#codice'+data.id+' #titoloLibro').text() !==data.titolo){
                    $('#codice'+data.id+' #titoloLibro').text(data.titolo) 
                    alert("il titolo è cambiato")
                }else{
                    alert(($('#codice'+data.id+' #titoloLibro').text() + ' ' + data.titolo))
                }
                alert('Modifiche confermate');  
                $('#modal').modal('hide');
            }); 
        } else { 
            alert('Modifiche annullate');
        }
    });
});
