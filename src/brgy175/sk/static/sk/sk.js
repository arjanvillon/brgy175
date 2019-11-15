document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
  
    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: [ 'dayGrid', 'timeGrid', 'list', 'bootstrap' ],
        timeZone: 'UTC',
        themeSystem: 'standard',
        height: 508,
        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },
          defaultDate: '2019-11-18',
          events: [
          {
              start: '2019-11-11T10:00:00',
              end: '2019-11-11T16:00:00',
              rendering: 'background',
              color: '#ff9f89'
          },
          {
              start: '2019-11-13T10:00:00',
              end: '2019-11-13T16:00:00',
              rendering: 'background',
              color: '#ff9f89'
          },
          {
              start: '2019-11-22',
              end: '2019-11-28',
              overlap: false,
              rendering: 'background'
          },
          {
              start: '2019-11-06',
              end: '2019-11-08',
              overlap: false,
              rendering: 'background'
          }
          ]
      });
  
      calendar.render();
      });

    