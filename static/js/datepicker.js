
// JS to initialize the datepicker

document.addEventListener('DOMContentLoaded', function() {
    flatpickr("#event-date-picker", {
        dateFormat: "Y-m-d",
        allowInput: true,
    });
});