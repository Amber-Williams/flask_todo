## install
1. Install python3, pip3 and virtualenv
2. In repo, run ‘virtualenv venv’ and it will create python project dependences folder
3. Then run 'source venv/bin/activate’ to get into the projects’ python environment
4. Run `flask db upgrade` to apply ORM to newly created app.db file (which will act as our database)
    - When working with database servers such as MySQL and PostgreSQL, you have to create the database in the database server before running upgrade.

## running
1. `cd`  into flask_todo/microblog
2. run `source venv/bin/activate` 
3. install packages running `pip3 install -r requirements.txt`
    1. Anytime a package is added run `pip freeze > requirements.txt` to update repo with your local env
4. Create a .env file with a SECRET_KEY variable to whatever you want
5. create a .flaskenv with `FLASK_APP=microblog.py`
6. run `flask db upgrade`
7. Finally run `flask run` to run app


## Playing with database
run `flask shell` to runs Python shell - python interpreter in the context of the application
using commands from object created in `make_shell_context`