$("#new-sheet-form").on("submit", function(e) {
    e.preventDefault();
    var mid = $("#mid").val();
    var tid = $("#tid").val();
    var alliance = $("#alliance").val();
    new_sheet(mid, tid, alliance);
});

$("[name=delete]").on("click", function(e) {
    var button = $(this);
    var sid = button.val();
    delete_sheet(sid, button);
});

$("#edit-sheet-form").on("submit", function(e) {
    e.preventDefault();
    var sid = $("#edit-sid").val();
    var mid = $("#edit-mid").val();
    var tid = $("#edit-tid").val();
    var alliance = $("#edit-alliance").val();
    update_sheet(sid, mid, tid, alliance);
});

$("[name=edit-sheet-button]").on("click", function(e) {
    var row = $(this).closest("tr");
    var sid = $(this).attr("value");
    $("#edit-sid").val(sid);
    row.each(function() {
        var mid = this.cells[0].innerHTML;
        var tid = this.cells[1].innerHTML;
        var alliance = this.cells[2].innerHTML;
        $("#edit-mid").val(mid);
        $("#edit-tid").val(tid);
        $("#edit-alliance").val(alliance);
    });
});

function new_sheet(mid, tid, alliance) {
    $("#new-sheet").prop("disabled", "disabled");
    $.post("/api/sheet/new", {
        mid: mid,
        tid: tid,
        alliance: alliance
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
            });
        }
    });
}

function update_sheet(sid, mid, tid, alliance) {
    $("#edit-sheet").prop("disabled", "disabled");
    $.post("/api/sheet/update", {
        sid: sid,
        mid: mid,
        tid: tid,
        alliance: alliance
    }, function(data) {
        if (data["success"] == 1) {
            display_message("edit-sheet-status", "success", data["message"], function() {
                $("#edit-sheet").removeAttr("disabled");
            });
        } else {
            display_message("edit-sheet-status", "danger", data["message"], function() {
                $("#edit-sheet").removeAttr("disabled");
            });
        }
    });
}
