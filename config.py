HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ
    from dotenv import load_dotenv
    
    load_dotenv()  # take environment variables from .env.
    API_ID = 4040599
    API_HASH = ce338573ca4a25aa36c9b505465e1c96
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    ARQ_API_KEY = MGDNPH-GZYATI-ADQRCS-OZNZKA-ARQ

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
