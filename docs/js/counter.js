var ctr = 0;
const EUROPE_MEAL_INCR = 26.9;
const AFRICA_MEAL_INCR = 1.66;
const EUROPE_KCAL_INCR = 18831;
const AFRICA_KCAL_INCR = 1159;

function incr() {
    if (ctr > 60) return;    
    var extra = "";
    if (ctr < 10) extra = "0"
    document.getElementById('seconds_ctr').innerHTML = extra + ctr.toString();
    document.getElementById('meal_europe').innerHTML = Math.round(ctr*EUROPE_MEAL_INCR);
    document.getElementById('kcal_europe').innerHTML = ctr*EUROPE_KCAL_INCR;
    document.getElementById('meal_africa').innerHTML = Math.round(ctr*AFRICA_MEAL_INCR);
    document.getElementById('kcal_africa').innerHTML = ctr*AFRICA_KCAL_INCR;
    ctr++;
    setTimeout(incr, 1000);
}