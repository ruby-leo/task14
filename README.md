### Framework Structure Overview:

* config -> config.json: Base URL, test account credentials and explicit wait are defined here
* pages: It has the base_page with implementation for all the actions. They are implemented using Explicit Wait so it waits until the desired condition is met or timed out. It also has all the subpages like login and dashboard page and their elements and action methods. Page Object Model is implemented in these pages.
* tests: It has all the tests given in the task (Testing of Login and Logout functions)
* utilities: It has reas_json.py that helps to read the config.json file
* conftest.py: It has all the fixtures necessary for setup and tear town
* requirements.txt: It has all the packages and their version details needed for this framework

HTML Report Screenshot:

![HTML Report Screenshot](HTML%20Report%20Screenshot.jpg)