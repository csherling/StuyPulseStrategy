$("#new-team-form").on("submit", function(e) {
    e.preventDefault();
    var tid = $("#tid").val();
    new_team(tid);
    $("#tid").val("");
});

function new_team(tid) {
    $("#new-team").prop("disabled", "disabled");
    $.post("/api/team/add", {
        tid: tid
    }, function(data) {
        if (data["success"] == 1) {
            display_message("new-team-status", "success", data["message"], function() {
                $("#new-team").removeAttr("disabled");
            });
        } else {
            display_message("new-team-status", "danger", data["message"], function() {
                $("#new-team").removeAttr("disabled");
            });
        }
    });
}
