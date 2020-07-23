# csm-backend
flask backend for Caliber Staging Module

## Wiki
https://github.com/revaturelabs/csm-backend/wiki

## Setup
To preface, you may need to use `pip3` and `python3` in lieu of `pip` and `python`, you can use `pip --version` or `pip3 --version` to see which version of the `pip` command workd for you, likewise for `python --version` or `python3 --version`. If neither work, you need to install Python. This should be done first before proceeding.

1. Create a virtual environment in the root directory by running `python -m venv .` or `python3 -m venv .`
2. Start the virtual environment according to your system
3. Install dependencies by running `pip install -r requirements.txt`
4. Set the environment variables (see below)
5. Run `python -m src.data.instantiate_db` to initialize the database
6. Run `flask run` to start the app

### Environment variables
* MONGO_URI: The connection URI for the Mongo Database. A mongo connection URI should start with `mongodb://` or `mongodb+srv://` followed by the host name (for a locally running mongodb server, for instance, `mongodb://127.0.0.1:27017`). If you are using MongoDB Atlas, the connection string will include your credentials and any arguments that you may need.
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
