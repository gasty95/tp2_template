

$(document).ready(function(){
    start_get_temperature();
    $('#modal-result').modal({backdrop: 'static', keyboard: false, show:false});
});

var control_temperature;

$(window).on("unload", function(e) {
    $.get("/samples/stop/" + id_sample, function(data){
        console.log(data);
    });
});

function start_get_temperature() {
    control_temperature = setInterval(temperature,frec);
}

function stop_get_temperature() {
    clearInterval(control_temperature);
    stop_chrono();
}

function temperature() {
    $.get("/samples/" + id_sample, function(data) {
        $("#temperature-" + id_sample).html(data.temperature);
        $("#windspeed-" + id_sample).html(data.windspeed);
        $("#pressure-" + id_sample).html(data.pressure);      
        $("#humidity-" + id_sample).html(data.humidity);
    });
}

$("#stop-samples").click(function() {    
    stop_get_temperature();
    $.get("/samples/stop/" + id_sample, function(data) {
        console.log(data);
    }).done(function() {        
        $.get("/samples/" + id_sample, function(data) {
            var text = "Algo";
            $("#text-result").html(text);
            $('#modal-result').modal('show');
        });
    });
});


