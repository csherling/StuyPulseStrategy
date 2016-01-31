$("#new-team-form").on("submit", function(e) {
    e.preventDefault();
    var tid = $("#tid").val();
    new_team(tid);
    $("#tid").val("");
});

$("[name=delete]").on("click", function(e) {
    var button = $(this);
    var tid = button.val();
    delete_team(tid, button);
})

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

function delete_team(tid, button) {
    button.prop("disabled", "disabled");
    $.post("/api/team/delete", {
        tid: tid
    }, function(data) {
        if (data["success"] == 1) {
            display_message("status", "success", data["message"], function() {
                button.removeAttr("disabled");
                remove_row(button);
            });
        } else {
            display_message("status", "danger", data["message"], function() {
                button.removeAttr("disabled");
            });
        }
    });
}

// Remove and animate table row
function remove_row(item) {
    item.closest("tbody")
        .find('td')
        .wrapInner('<div style="display: block;" />')
        .parent()
        .find('td > div')
        .slideUp("fast", "swing", function(){
            $(this).parent().parent().remove();
        });
}
