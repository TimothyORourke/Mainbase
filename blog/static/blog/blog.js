$(document).ready( () => {
    $('a.active').removeClass('active');
    $('a.nav-link[href="' + location.pathname + '"]').addClass('active'); 
});

$('.follow-button').on('click', (e) => {
    const username = $(e.target).attr('data-username');

    $.ajax({
        url: `/users/follow/${username}`,
        type: 'PUT',
        dataType: 'json',
        data: {
            username: username,
        },
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        success: (res) => {
            $(`button[data-username=${username}]`).closest('.follow-card').remove();
        }
    });
});

$('.unfollow-button').on('click', (e) => {
    const username = $(e.target).attr('data-username');

    $.ajax({
        url: `/users/follow/${username}`,
        type: 'DELETE',
        dataType: 'json',
        data: {
            username: username,
        },
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        success: (res) => {
            console.log(res);
            $(`button[data-username=${username}]`).remove();
        }
    });
});