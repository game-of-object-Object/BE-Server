# BE-Server

Deploy: <https://g-o-o-o.herokuapp.com/>

To edit migrations on heroku, run the commands:
python app.py db migrate
python app.py db upgrade

If you receive a message saying that something is not up to date, you may have to run:
python app.py db stamp head

If other issues occur with migrations, try deleting database first and re-running commands.
