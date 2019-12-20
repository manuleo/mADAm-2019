var ctr = 0;
const EUROPE_MEAL_INCR = 26.9;
const AFRICA_MEAL_INCR = 1.66;

var meal_europe, meal_africa, seconds;

var od;

function init() {
    meal_europe = document.getElementById('meal_europe');
    meal_africa = document.getElementById('meal_africa');
    seconds = document.getElementById('seconds_ctr');
}

function zfill(string, size) {
    return "0".repeat(size - string.length) + string;
}

function incr() {
    if (ctr > 60) return;    
    seconds.innerHTML = zfill(ctr.toString(),3)
    meal_europe.innerHTML = zfill(Math.round(ctr*EUROPE_MEAL_INCR).toString(), 5);
    meal_africa.innerHTML = zfill(Math.round(ctr*AFRICA_MEAL_INCR).toString(), 5);
    ctr += 2;
    setTimeout(incr, 2000);
}