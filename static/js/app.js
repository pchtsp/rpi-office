
turn_light_off = function() {
    $.getJSON($SCRIPT_ROOT + '/turn_light_off', {}, function(data) {
        console.log(data.result);
    });    
}

turn_light_on = function() {
    $.getJSON($SCRIPT_ROOT + '/turn_light_on', {}, function(data) {
        console.log(data.result);
    });
}

    
mouseUp = function() {
    console.log("LIBERA!!");
    turn_light_off();
};

mouseDown = function() {
    console.log("PRESIONA");
    turn_light_on();
    setTimeout(turn_light_off, 5000);
};