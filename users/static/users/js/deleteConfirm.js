$('#deleteConfirm').on('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = $(event.relatedTarget);
    // Extract info from data-* attributes
    var href = button.data('href');
    var name = button.data('name');
    var modal = $(this);
    modal.find('.delete-warning').text('Are you sure you want to delete ' + name + '?');
    modal.find('.delete-button').attr('href', href);
});