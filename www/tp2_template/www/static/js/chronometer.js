var centesimas = 0;
var segundos = 0;
var minutos = 0;
var horas = 0;
var control_chrono;

$(document).ready(function(){
    start_chrono ();
});

function start_chrono () {
    control_chrono = setInterval(chronometro,10);
}

function stop_chrono () {
    clearInterval(control_chrono);            
}

function chronometro () {
    if (centesimas < 99) {
        centesimas++;
        if (centesimas < 10) { centesimas = "0"+centesimas }                
        $('#centesimas').html(":"+centesimas);
    }
    if (centesimas == 99) {
        centesimas = -1;
    }
    if (centesimas == 0) {
        segundos ++;
        if (segundos < 10) { segundos = "0"+segundos }
        $('#segundos').html(":"+segundos);
    }
    if (segundos == 59) {
        segundos = -1;
    }
    if ( (centesimas == 0)&&(segundos == 0) ) {
        minutos++;
        if (minutos < 10) { minutos = "0"+minutos }
        $('#minutos').html(":"+minutos);
    }
    if (minutos == 59) {
        minutos = -1;
    }
    if ( (centesimas == 0)&&(segundos == 0)&&(minutos == 0) ) {
        horas ++;
        if (horas < 10) { horas = "0"+horas }
        $('#horas').html(horas);                
    }
}