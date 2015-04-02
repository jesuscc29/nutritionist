/**
 * Created by jesuscc29 on 3/5/15.
 */

ERRORS = {
    "field-errors": "Error, revise los campos obligatorios!"
};

showErrorMessage = function (title, message) {
    $("#error-title").html(title);
    $("#error-message").html(message);
    $("#errorModal").modal("show");
};

showSuccessMessage = function(title, message) {
    $("#success-title").html(title);
    $("#success-message").html(message);
    $("#successModal").modal("show");
};