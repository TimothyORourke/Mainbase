$(document).ready( () => {
    $('a.active').removeClass('active');
    $('a.nav-link[href="' + location.pathname + '"]').addClass('active'); 
});

$('.follow-button').on('click', (e) => {
    const followeeName = $(e.target).attr('data-followee');
    console.log(`Followee: ${followeeName}`);
});