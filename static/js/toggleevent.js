
// Function for button that toggles between past and upcoming events

document.addEventListener('DOMContentLoaded', function () {
    const upcomingEvents = document.getElementById('upcoming-events');
    const pastEvents = document.getElementById('past-events');
    const upcomingBtn = document.getElementById('upcoming-btn');
    const pastBtn = document.getElementById('past-btn');

    function toggleEventsSelection(isUpcoming) {

        if (isUpcoming) {
            upcomingEvents.style.display = 'block';
            pastEvents.style.display = 'none';
            upcomingBtn.classList.add('active');
            pastBtn.classList.remove('active');
        } else {
            upcomingEvents.style.display = 'none';
            pastEvents.style.display = 'block';
            upcomingBtn.classList.remove('active');
            pastBtn.classList.add('active');
        }
    }

    upcomingBtn.addEventListener('click', function () {
        toggleEventsSelection(true);
    });

    pastBtn.addEventListener('click', function () {
        toggleEventsSelection(false);
    });

});