## NOTE: To run the app, you do not have to install it!
Just use the link below to open it in your browser

https://reprepapp.herokuapp.com

If you do need to install it, follow the steps described below.

## Installation
The app can be deployed in two ways--either locally (on your own computer) or to a WSGI server ('in the web').

### Prerequisits
- This app runs on Python 3.7+, it will not work correctly with older versions.
- You need to register an new OAuth app in your GitHub account. Go to your account `Settings`->`Developer settings`->`OAuth Apps`. There, click on 'New OAuth App`.
Fill in the `Application name`, then `Homepage URL` and `Authorization callback URL`.

  - `Application name`: put whatever you want
  - `Homepage URL`: http://127.0.0.1:5000 in case you deploy locally. If you deploy using Heroku, put `https://[your_app_name_as_registered_in_Heroku].herokuapp.com/`
  - `Authorization callback URL`: http://127.0.0.1:5000/auth in case you deploy locally. If you deploy using Heroku, put `https://[your_app_name_as_registered_in_Heroku].herokuapp.com/auth`
- Click on the `Register Application` button. You will be redirected to a page with the `Client_ID` and the `Client_Secret` sequences, you will need to set them as environmantal variables, so pay close attention to them!
### Local installation
1. **Get the source code**

To do so, [open the repository with the source code](https://github.com/AndriiPernatii/repository_replicator) and click on the 'CLONE OT DOWNLOAD' button--you will download a .zip file. It is absolutely your choice where to unzip it.

2. **Set up a virtual environment**

It is better to keep app-specific packages away from another-app-specific packages. Open your terminal, and type:
```
pip install virtualenv
cd Desktop
virtualenv new_environment
source new_environment/bin/activate
pip install -r requirements.txt
```
Now, you have a separate environment which contains all the needed modules for the correct work of the app.

3. **Set secret variables**

This can be done in the config.py file (it works but is **extremely not recommended**). Change it to look like this:
```
SECRET_KEY = put_the_app_secret_key_here
GITHUB_CLIENT_ID = put_the_oauth_client_ID_here
GITHUB_CLIENT_SECRET = put_the_oauth_client_secret_key_here
```
Alternalively, and **way better than the first one**, open you terminal and set the environmental variables like this:
```
export SECRET_KEY = put_the_app_secret_key_here
export GITHUB_CLIENT_ID = put_the_oauth_client_ID_here
export GITHUB_CLIENT_SECRET = put_the_oauth_client_secret_key_here
```
You can use the built-in `secrets` module in your terminal to get a random sequence, e.g. '351baacb37ed5dbb4f9f45dc4764ea8f',  for `SECRET_KEY`, like this:
```
import secrets
secrets.token_hex(16)
```
**Remember!** All the above variables are supposed to be secret, you must not share them with anyone (thus use the second method to set the variables).

4. **Run the app!**

In your terminal, navigate to the directory with the source code (the virtual environment must be running), print this line:
```python run.py```
If everything is fine, you will see this line among the others:

```Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```


Now just open http://127.0.0.1:5000/ in your browser and have fun with the app!

### Cloud installation
This type depends a lot on the deployment option you like most. See [the Flask documentation](https://flask.palletsprojects.com/en/1.1.x/deploying/) for instruction on several of them.

Here, Heroku deployment is described.
1. **Create a new app in Heroku and give it a name**

For this, you need a Heroku account.

2. **Choose the deployment method you like and follow simple instructions**

The GitHub-connection option is the easiest, because it does not require to return git commands in your terminal. But your will need to first download the source code and then upload is to your own GitHub repository.

3. **Set the environmental variables**

Under the Settings tab of your deployed (and most-probably not working) app, find the `Config Var` section and put the actual values for the environmental variables (`SECRET_KEY`, `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`, and `ORIGINAL_REPO`) there. Do not change anything in the config.py file this time!

4. **Open the web-site of the app**

Click on the `View` button at the bottom of the `Deploy` tab. You will be redirected to the web-page with your application. The corresponding URL can be used to acces the app by any person. Have fun!





