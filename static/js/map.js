// function initMap() {
//     var map = new google.maps.Map(document.getElementById('map'), {
//         center: {
//             lat: 0,
//             lng: 0
//         },
//         zoom: 10
//     });

//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(function (position) {
//             var userLatLng = {
//                 lat: position.coords.latitude,
//                 lng: position.coords.longitude
//             };
//             map.setCenter(userLatLng);
//         }, function () {
//             handleLocationError(true, map.getCenter());
//         });
//     } else {
//         handleLocationError(false, map.getCenter());
//     }

//     function handleLocationError(browserHasGeolocation, pos) {
//         var infoWindow = new google.maps.InfoWindow();
//         infoWindow.setPosition(pos);
//         infoWindow.setContent(browserHasGeolocation ?
//             'Error: The Geolocation service failed.' :
//             'Error: Your browser doesn\'t support geolocation.');
//         infoWindow.open(map);
//     }

//     var events = [
//         {% for event in events %}
//         {
//             "title": "{{ event.title }}",
//             "lat": {{ event.latitude }},
//             "lng": {{ event.longitude }},
//             "event_genre": "{{ event.event_genre }}",
//             "event_venue": "{{ event.event_venue }}",
//             "event_date": "{{ event.event_date }}",
//             "url": "{% url 'event_details' slug=event.slug %}"
//         },
//         {% endfor %}
//     ];

//     for (var i = 0; i < events.length; i++) {
//         createMarker(events[i]);
//     }

//     function createMarker(event) {
//         var marker = new google.maps.Marker({
//             position: {
//                 lat: event.lat,
//                 lng: event.lng
//             },
//             map: map,
//             title: event.title
//         });

//         var infowindow = new google.maps.InfoWindow({
//             content: `<div>
//                 <h2>${event.title}</h2>
//                 <p>Genre: ${event.event_genre}</p>
//                 <p>Venue: ${event.event_venue}</p>
//                 <p>Date: ${event.event_date}</p>
//                 <p><a href="#" >Save event <i class="far fa-heart"></i></a></p>
//                 <p><a href="${event.url}" target="_blank">Event Details</a></p>
//             </div>`
//         });

//         marker.addListener('click', function () {
//             infowindow.open(map, marker);
//         });
//     }
// }