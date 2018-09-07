

$(document).ready(function(){
    start_get_temperature();
    $('#modal-result').modal({backdrop: 'static', keyboard: false, show:false});
});

var control_temperature; // variable para controlar la frecuencia de muestreo de los valores


function start_get_temperature() {
    control_temperature = setInterval(temperature,frec); //la variable frecuencia se obtiene del samples.html. Esta tendrá un valor en ms, se utilizara para controlar el periodo de muestreo de los datos en la página.
}


function temperature() {  //función encargada de mostrar los datos obtenidos. Se obtiene un sample con el ID.
    $.get("/samples/" + id_sample, function(data) {
        $("#temperature-" + id_sample).html(data.temperature);
        $("#windspeed-" + id_sample).html(data.windspeed);
        $("#pressure-" + id_sample).html(data.pressure);      
        $("#humidity-" + id_sample).html(data.humidity);
    });
}



