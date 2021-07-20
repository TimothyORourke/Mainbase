$('.follow-button').on('click', (e) => {
    const followeeName = $(e.target).attr('data-followee');
    console.log(`Followee: ${followeeName}`);
});