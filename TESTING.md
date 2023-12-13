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






