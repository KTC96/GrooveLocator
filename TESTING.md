# Testing

## Code validation

### HTML

I used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Because my project uses Jinja syntax, I copied source data from each page and validated by input.


| Page | Screenshot | Notes |
| --- | --- | --- |
|Home Logged Out  | ![Home](documentation/testing/home_logged_out.png)|Pass |
|Home Logged In  | ![Home](documentation/testing/home_logged_in.png)|Pass |
|Login | ![Login](documentation/testing/login_page.png)|Pass |
|Sign up|   ASK MENTOR|Fail |
|Logout  | ![Logout](documentation/testing/signout_page.png)|Pass |
|Events Logged Out  | ![Events](documentation/testing/events_logged_out.png)|Pass |
|Events Logged In  | ![Events](documentation/testing/events_logged_in.png)|Pass |
|Saved Events | ![Events](documentation/testing/saved_events_logged_in.png)|Pass |
|Event Details Logged Out | ![Events](documentation/testing/event_details_logged_out.png)|Pass |
|Event Details Logged In | ![Events](documentation/testing/event_details_logged_in.png)|Pass |


### CSS

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!">
    </a>
</p>
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!">
    </a>
</p>
        
### Javascript

My current implementation combines JavaScript with Jinja and Django template language, which complicates the validation process. To enhance the structure for future iterations, I intend to separate my JavaScript code into dedicated files. Additionally, I plan to securely pass the Google Maps API key through a Django view.

Despite this, thorough inspection using Google Dev Tools in the browser console reveals no errors related to my JavaScript code.


### Python

I have used the [CI Python Linter](https://pep8ci.herokuapp.com) to validate my Python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| settings.py | ![settings](documentation/testing/settings.png) | Pass|
| models.py | ![models](documentation/testing/models.png) | Pass |
| urls.py (GrooveLocator) | ![urls](documentation/testing/main_urls.png) | Pass |
| urls.py (Map) | ![urls](documentation/testing/urls_map.png) | Pass |
| views.py (Map) | ![views](documentation/testing/views.png) | Pass |
| forms.py | ![forms](documentation/testing/forms.png) | Pass |

## Lighthouse

| Page | Device | Screenshot|
| --- | --- | --- |
| Home (Logged In) | Desktop | ![home](documentation/testing/lighthouse_home_logged_in_desktop.png)  |
| Home (Logged In) | Mobile | ![home](documentation/testing/lighthouse_home_logged_in_mobile.png)  |
| Home (Logged Out) | Desktop | ![home](documentation/testing/lighthouse_home_logged_out_desktop.png)  |
| Home (Logged Out) | Mobile | ![home](documentation/testing/lighthouse_home_logged_out_mobile.png)  |
| Events List | Desktop | ![Events List](documentation/testing/lighthouse_events_list_desktop.png)  |
| Events List | Mobile | ![Events List](documentation/testing/lighthouse_events_list_mobile.png)  |
| Event details (Logged In) | Desktop | ![Event Details](documentation/testing/lighthouse_event_details_logged_in_desktop.png)  |
| Event details (Logged In) | Mobile | ![Event Details](documentation/testing/lighthouse_event_details_logged_in_mobile.png)  |
| Event details (Logged Out) | Desktop | ![Event Details](documentation/testing/lighthouse_event_details_logged_out_desktop.png)  |
| Event details (Logged Out) | Mobile | ![Event Details](documentation/testing/lighthouse_event_details_logged_out_desktop.png)  |
| Login | Desktop | ![Login](documentation/testing/lighthouse_login_desktop.png)  |
| Login | Mobile | ![Login](documentation/testing/lighthouse_login_mobile.png)  |
| Logout | Desktop | ![Logout](documentation/testing/lighthouse_logout_desktop.png)  |
| Logout | Mobile | ![Logout](documentation/testing/lighthouse_logout_mobile.png)  |
| Sign Up| Desktop | ![Sign Up](documentation/testing/lighthouse_signup_desktop.png)  |
| Sign Up| Mobile | ![Sign Up](documentation/testing/lighthouse_signup_mobile.png)  |

## Defensive Programming 

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | Click on Logo | Redirection to Home page | Pass | |
| Home | Click  on "Get my location" | Map gets geolocation data and zooms on your area | Pass | |
| Home | Click on the "Choose a genre dropdown" | A dropdown of available genres can be seen | Pass | |
| Home | Click on the filter button after choosing a genre | The map repopulates only with events that match that genre | Pass | |
| Home | Click on the "toggle legend" button| The legend opens displaying icons and associated genres | Pass | |
| Home | Click on event icon on the map | The infowindow for the event opens with relevant information | Pass | |
| Home | Click on "event details" within an open infowindow | The user is redirected to the event details for that event  | Pass | |






