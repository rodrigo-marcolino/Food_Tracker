# Food Tracker App
One of the project task from [O'Reilly - The Ultimate Flask Course Course ](https://learning.oreilly.com/videos/the-ultimate-flask/9781839219924)


![screen](https://github.com/rodrigo-marcolino/Food_Tracker/blob/master/SharedScreenshot.jpg)

### Demo add food

![add_food](https://user-images.githubusercontent.com/51892785/86201015-64ec4500-bbb2-11ea-93e2-3c328c0409e3.gif)

### Demo add a day

![add_day](https://user-images.githubusercontent.com/51892785/86201336-5e120200-bbb3-11ea-88ff-7f747cc57ee9.gif)

# Run Project Locally
### Create Virtual Environment
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
