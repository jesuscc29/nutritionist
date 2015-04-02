/**
 * Created by jesuscc29 on 4/2/15.
 */

validateRequiredFields = function (currentForm) {
    var is_valid = true;
    currentForm.find('input.required, select.required').each(
        function (index) {
            var $this = $(this);
            var parent = $this.parent();
            if ($this.val() == '') {
                parent.removeClass('has-success');
                parent.addClass('has-error');
                is_valid = false;
            } else {
                parent.removeClass('has-error');
                //parent.addClass('has-success');
                is_valid = true;
            }
        });
    return is_valid
};