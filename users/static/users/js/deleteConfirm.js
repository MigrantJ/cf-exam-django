$('#deleteConfirm').on('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = $(event.relatedTarget);
    // Extract info from data-* attributes
    var href = button.data('href');
    var name = button.data('name');
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('.delete-warning').text('Are you sure you want to delete ' + name + '?');
    modal.find('.delete-button').attr('href', href);
});