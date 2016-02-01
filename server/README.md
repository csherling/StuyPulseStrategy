### Deploying the server

This server uses [Flask](http://flask.pocoo.org/), and does not require an Internet connection to run.

1. Ensure dependencies are installed by running the `setup.sh` script inside the `scripts` folder.
	* When mysql gets installed, make sure that the password is set to `password`. If you want to use a different password,
make sure that [this](https://github.com/csherling/StuyPulseStrategy/blob/flask-app/server/app.py#L10) and
[this](https://github.com/csherling/StuyPulseStrategy/blob/flask-app/server/scripts/setup.sh#L3) gets changed.

2. Run `./deploy`, with an optional `--debug` flag to enable debug mode.

3. View the server at [localhost:1337](http://localhost:1337).
