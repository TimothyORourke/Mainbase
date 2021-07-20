$('.post-delete-button').on('click', (e) => {
    e.stopPropagation();

    const pk = $(e.target).attr('data-pk');
    $('#postDeleteModalButton').attr('data-pk', pk);
});

$('#postDeleteModalButton').on('click', (e) => {
    e.stopPropagation();

    const pk = $(e.target).attr('data-pk');
    console.log(pk);
    $.ajax({
        url: `p/${pk}/delete`,
        type: 'DELETE',
        dataType: 'json',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        success: () => {
            $(`button[data-pk=${pk}]`).closest('.post-wrapper').remove();
            $('#postDeleteModal').modal('toggle');
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}