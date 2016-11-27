var ractiveShowStatus = new Ractive({
    el: 'ractive-show-status',
    template: '#template-show-status',
});

var previewHtml = null;
function updateStatus(){
    $.get(api.status + taskId)
    .done(function(status) {
        ractiveShowStatus.set("status", status);
        if(status.info["type"] == "new-task"){
            taskId = status.info["task-id"];
            ractiveShowStatus.set("previewHtml", status.info["preview-html"]);
        } else if(status.state == "SUCCESS") {
            console.log("clearing interval")
            clearInterval(updateStatusInterval);
        }
    });
}

updateStatus();
var updateStatusInterval = setInterval(updateStatus, 1500);
