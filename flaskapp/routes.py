from flask import Flask, g, render_template, url_for, flash, redirect, request, session
from flaskapp import app, github
from flask_github import GitHubError


@app.route('/')
@app.route('/home')
def home():
    return render_template('new_home.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('new_about.html', title='About the App')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user.authorized:
        flash('Already logged in.', category='warning')
        return redirect(url_for('home'))
    return github.authorize(scope='public_repo', redirect_uri=url_for('auth', _external=True))

@app.route('/auth', methods=['GET', 'POST'])
@github.authorized_handler
def auth(oauth_token):
    next_url = request.args.get('next') or url_for('home')
    #oauth_token is a token received from GitHub, None if authorization failed
    if oauth_token is None:
        flash("Authorization failed.", category='error')
        #return redirect(url_for('home'))
        return redirect(next_url)

    g.user.oauth_token = oauth_token
    flash("Authorization successful.", category='success')

    try:
        response = github.get('/user')
        g.user.username = response['login']
        g.user.profile_url = response['html_url']
    except GitHubError:
        flash('Failed to get user info: {}'.format(GitHubError), category='error')

    #return redirect(url_for('home'))
    return redirect(next_url)

@app.route('/replicate', methods=['GET', 'POST'])
def replicate():
    #Do not delete the authorization check! A user could use the route as
    #the address in the browser and replicate a repository without being
    #authorized!
    if not g.user.authorized:
        flash('You are not authorized. Please log in to your GitHub account first.', category='warning')
        return redirect(url_for('home'))

    try:
        response = github.post('/repos/{}/forks'.format(app.config['ORIGINAL_REPO']))
        g.user.repo_url = response['html_url']
    except GitHubError:
        flash('Forking the repo failed: {}'.format(GitHubError), category='error')
        return redirect(url_for('home'))

    flash('Repository successfully cloned.', category='success')

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    if not g.user.authorized:
        flash('You are not logged in.', category='warning')
    else:
        g.user.reset()
        flash('You have logged out.', category='success')
    return redirect(url_for('home'))
