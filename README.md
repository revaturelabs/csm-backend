# csm-backend
flask backend for Caliber Staging Module

## Setup
1. Create a virtual environment in the root directory by running `python -m venv .` or `python3 -m venv .`
2. Start the virtual environment according to your system
3. Install dependencies by running `pip install -r requirements.txt`
4. Set the environment variables (see below)
5. Run `python -m src.data.instatiate_db` to initialize the database
6. `cd` into the src directory and run `flask run` to start the app

### Environment variables
* MONGO_URI_PJ3: The connection URI for the Mongo Database
* FLASK_APP: The location of the flask app in relation to your .env file, if your .env file is in the root it should be `src/app.py`
* EXTERNAL_API: The base URI for the Caliber API

## Developing
All code should be written within either the `/src` directory or a subfolder of the `/src` directory.

Unit tests should be put in `/src/unittest`

API Routes that will be accessed should be placed in `/src/router`

Models for database documents should be placed in `/src/models`

The `/src/external` folder is for calling the Caliber API, please use the appropriate file for the caliber endpoint you are accessing.

Database functions should go into `/src/data/data.py`

Additional information will be added once it is available.
