# RepRepApp is a self-replicating GitHub repository #

The application forks itself to another user's account. **Keep in mind** that you cannot fork your own repositories in your 
(same) account!

## Technical aspects ##
1. The app is written using Flask--python microframework for web development--in Python v3.8. The app is compatible with
Python v3.7 but will not work with older version.

2. See external packages and their versions, used in this application, in the `requirements.txt` file.

3. To authenticate users via GitHub, OAuth protocol was applied using the GitHub-Flask extension.

4. BootstrapCDN was used to apply core CSS and add JavaScript functionality to the web-pages.

## Package description ##

- `run.py` is the root file of the packages and is used to run the app only.

- `requirements.txt` contains info about external modules that need to be installed prior to deployment.

- `Procfile` and `runtime.txt` are required for the app deployment to a server. `Procfile` ensures that the app is run in the web, while `runtime.txt` set the version of Python to use.

- `installation.md` contains instructions for local or server deployment.

- `LISENCE` contains the lisence description, whereas `README.txt` contains a short description of the application

**The `flaskapp` Folder**

- `__init__.py` is the initialization file that creates instances of the app.

- `config.py` contains configuration constanst in the form of environmental variables.

- `models.py` contains just a single `User` class that allows us authorize users in GitHub and keep track of current sessions.

- `routes.py` contains all the routes used in this app. It serves as a 'navigation map' as well as adds some crucial functionality.

**The `templates` Folder** contains HTML files to render. `new_home.html` and `new_about.html` extend the `layout.html`.

**The `static` Folder** contains a CSS file that adds eye-catching cosmetics to the layout of the rendered web-pages.


## How it functions ##

After clicking on the link reprepapp.herokuapp.com, a user is redirected to the home page of the web-application.
At the top of the home page, a user sees a navigation bar which allows them to switch between the HOME and ABOUT pages.

At the bottom of the two pages, there is a footer with a link to the DataRobot official web-site
and the app developer's LinkedIn page.

## HOME Page ##
In the center of the page, a user sees a short instruction about how to activate the disabled `REPLICATE`
button in the middle of the screen. To do that, a user has to click on the login link.

### Authorization ###
The authorization process is handled mainly by the **github_flask** package using **OAuth** technology.
The user gets redirected to GitHub where they have to enter their login and password.

**NOTE** The app does not receive any information about the user's login or password. The OAuth technology ensures
the sensitive info if acceesed by GitHub only. GitHub then sends a request to the app to check the legitimacy of the login.
After that, RepRepApp send another request to GitHub to receive a user_token. Since this moment, the user is logged in.
To notify the user, a message `Authorization successful.` is flashed (functions thanks to flash method of flask).

### Repository replication ###
The text in the center of the page changes. Now the user sees their GitHub username and can click a link to logout from their GitHub account (which should be done always to terminate the security token!).
Below that link, the `REPLICATE` button activates which allows the user to clone the app source code into their own repository.
This is done via a POST request from the app to GitHub. The user will be notified about the success of failure of the operation by a flashed message.

### Logout ###
A user should always logout. To do so, they have to click on logout link in the middle of the screen. The user will be notified about the logout via a flashed message.

### Flash messages ###
Flash messages notify a user about successful or failed authorization, successful or failed logout, authorization status before a replication attempt, authorization attempt while being logged, and attempts to log out while not being logged in.

## ABOUT Page ##
The page contains a short description of the app, several important notes about its funcitonality and a link to the GitHub repository with the source code. 
