var ractiveShowStatus = new Ractive({
    el: 'ractive-show-status',
    template: '#template-show-status',
});


function updateStatus(){
    $.get(api.status + taskId)
    .done(function(status) {
        console.log(status);
        ractiveShowStatus.set("status", status);   
    });
}

setInterval(updateStatus, 1500);
