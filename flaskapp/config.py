import os

#Setting variables with secret info
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')
    ORIGINAL_REPO = os.getenv('ORIGINAL_REPO')
    #CLIENT_ID = os.getenv('CLIENT_ID')
    #CLIENT_SECRET = os.getenv('CLIENT_SECRET')
