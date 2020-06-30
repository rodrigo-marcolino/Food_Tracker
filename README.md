# Food Tracker App
One of the course projects from [O'Reilly - The Ultimate Flask Course Course ](https://learning.oreilly.com/videos/the-ultimate-flask/9781839219924)


![screen](https://github.com/rodrigo-marcolino/Food_Tracker/blob/master/SharedScreenshot.jpg)
# Create Virtual Environment
In a terminal run the following commands from the root folder of the forked project.

Windows

```bash 
python -m venv .\venv
```

macOS & Linux

```bash 
python -m venv ./venv
```
Once that completes, also run this command from the same folder.

Windows

```bash
venv\Scripts\activate.bat
```

macOS & Linux

```bash
source venv/bin/activate
```
Now that you are working in the virtualenv, install the project dependencies with the following command.
```bash
pip install -r requirements.txt
```
After install [sqlite3](https://www.sqlite.org/index.html)
```bash
sqlite3 data.db < food_tracker.sql
```

Start the App
```bash
flask run
```
