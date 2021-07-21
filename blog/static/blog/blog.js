$(document).ready( () => {
    $('a.active').removeClass('active');
    $('a.nav-link[href="' + location.pathname + '"]').addClass('active'); 
});

$('.follow-button').on('click', onFollowButtonClicked);
$('.unfollow-button').on('click', onUnfollowButtonClicked);
$('.darkmode-button').on('click', onDarkmodeButtonClicked);

function toggleFollowButtonType(button) {
    let isFollowButton = button.hasClass('follow-button');
    console.log(button);
    button.toggleClass('follow-button unfollow-button');
    button.toggleClass('btn-outline-primary btn-outline-danger');
    button.off('click');

    if (isFollowButton) {
        button.on('click', onUnfollowButtonClicked);
        button.text('Unfollow');
    }
    else {
        button.on('click', onFollowButtonClicked);
        button.text('Follow');
    }
}

function onFollowButtonClicked(e) {
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
        success: () => {
            toggleFollowButtonType($(`button[data-username=${username}]`));
        }
    });
}

function onUnfollowButtonClicked(e) {
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
        success: () => {
            toggleFollowButtonType($(`button[data-username=${username}]`));
        }
    });
}

function onDarkmodeButtonClicked(e) {
    $('#darkmode').prop('disabled', (i, v) => !v);

    $.ajax({
        url: '/users/settings/',
        type: 'PUT',
        data: {
            darkmode: !$('#darkmode').prop('disabled')
        },
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        success: (res) => {
            console.log("Website theme toggled.");
        }
    });
}