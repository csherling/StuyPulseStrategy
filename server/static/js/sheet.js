$("#new-sheet-form").on("submit", function(e) {
    e.preventDefault();
    var mid = $("#mid").val();
    var tid = $("#tid").val();
    new_sheet(mid, tid);
})

$("[name=delete]").on("click", function(e) {
    var button = $(this);
    var sid = button.val();
    delete_sheet(sid, button);
})

function new_sheet(mid, tid) {
    $("#new-sheet").prop("disabled", "disabled");
    $.post("/api/sheet/new", {
        mid: mid,
        tid: tid
    }, function(data) {
        if (data["success"] == 1) {
            display_message("new-sheet-status", "success", data["message"], function() {
                $("#new-sheet").removeAttr("disabled");
            });
        } else {
            display_message("new-sheet-status", "warning", data["message"], function() {
                $("#new-sheet").removeAttr("disabled");
            });
        }
    });
}

function delete_sheet(sid, button) {
    button.prop("disabled", "disabled");
    $.post("/api/sheet/delete", {
        sid: sid
    }, function(data) {
        if (data["success"] == 1) {
            display_message("status", "success", data["message"], function() {
                button.removeAttr("disabled");
                remove_row(button);
            });
        } else {
            display_message("status", "danger", data["message"], function() {
                button.removeAttr("disabled");
            })
        }
    })
}
