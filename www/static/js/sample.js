

$(document).ready(function(){
    start_get_temperature();
});


var control_temperature;
function start_get_temperature() {
    control_temperature = setInterval(function(){
        $.get("/samples/" + id_sample, function(data) {
            $("#temperature-" + id_sample).html(data.temperature);
            $("#windspeed-" + id_sample).html(data.windspeed);
            $("#pressure-" + id_sample).html(data.pressure);      
            $("#humidity-" + id_sample).html(data.humidity);
        });},inlineFormCustomSelect);
}

function temperature() {
    $.get("/samples/" + id_sample, function(data) {
        $("#temperature-" + id_sample).html(data.temperature);
        $("#windspeed-" + id_sample).html(data.windspeed);
        $("#pressure-" + id_sample).html(data.pressure);      
        $("#humidity-" + id_sample).html(data.humidity);
    });
}
