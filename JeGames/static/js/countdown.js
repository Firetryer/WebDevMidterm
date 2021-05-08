function getTimeRemaining(endtime){
const total = Date.parse(endtime) - Date.parse(new Date());
const seconds = Math.floor( (total/1000) % 60 );
const minutes = Math.floor( (total/1000/60) % 60 );
const hours = Math.floor( (total/(1000*60*60)) % 24 );
const days = Math.floor( total/(1000*60*60*24) );

return {
    total,
    days,
    hours,
    minutes,
    seconds
};
}


function initializeClock(endtime) {
    const timeinterval = setInterval(() => {
        const t = getTimeRemaining(endtime);
        document.getElementById("countdown-hour").innerHTML = t.hours
        document.getElementById("countdown-minute").innerHTML = t.minutes
        document.getElementById("countdown-second").innerHTML = t.seconds
        
        if (t.total <= 0) {
        clearInterval(timeinterval);
        }
    },1000);
}
