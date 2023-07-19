## Set up the project

- Copy the previous project to old

```bash
cp -r App_Project App_Project_old
```

- Downoload the new zip project
- Extract the zip project

```bash
unzip App_Project.zip
```

- Create virtual environment

```bash
python3 -m venv venv
```

- Activate virtual environment

```bash
source venv/bin/activate
```

- Install requirements

```bash
pip install -r requirements.txt
```
- Replace the previous run.py with the new run.py

- export FLASK_APP

```bash
export FLASK_APP=run.py
```

- run the project

```bash
flask run
```

- Open the browser and go to the url to test

```bash
http://127.0.0.1:5000/home
```

If all good you will the test page

## Next stage

- Test the database
  run the following command

```bash
sqlite3 database.db
```

- Check users table

```sqlite
.tables
```

- select users from table

```sqlite
select * from users;
```

If good you will see the users in the table and the datas

### Next is creating your HTML pages and routes

since you have all your already set up in the views.py you can start creating your HTML pages
ignore the auth.py you don't need that anymore.

Create your HTML pages in the templates folder

- home.html (this page is alreday created for you)
- login.html (the login page)
- signup.html (the register page)

### Test your pages by going to the following urls

- http://127.0.0.1:5000/login for the login page
- http://127.0.0.1:5000/signup for the signup page
