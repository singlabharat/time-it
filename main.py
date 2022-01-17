from plyer import notification
import threading
import time
from flask import Flask, render_template, request
import my_functions
from colorama import Fore, Back, Style
import datetime

time_per = str()
app = Flask(__name__)

print(Fore.GREEN + 'Loading...')
print(Style.RESET_ALL)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/recreation')
def recreation():
    my_fact = my_functions.get_fact()
    my_quote = my_functions.get_qoute()[0]
    author = my_functions.get_qoute()[1]
    link = my_functions.get_youtube_vid()
    hack = my_functions.get_study_hack()
    return render_template('recreation.html', fact=my_fact, quote=my_quote, source=link, hack=hack)


@app.route('/reminders', methods=['POST', 'GET'])
def reminders():
    if request.method == "POST":
        # Get
        water = request.form.get('water')
        meditation = request.form.get('meditation')
        exercise = request.form.get('exercise')
        rest = request.form.get('rest')
        entertain = request.form.get('entertain')
        # Set
        my_functions.set_reminder('water', water)
        my_functions.set_reminder('meditate', meditation)
        my_functions.set_reminder('exercise', exercise)
        my_functions.set_reminder('rest', rest)
        my_functions.set_reminder('entertain', entertain)

        water_bool = str(my_functions.reminder_check('water'))
        meditate_bool = str(my_functions.reminder_check('meditate'))
        exercise_bool = str(my_functions.reminder_check('exercise'))
        rest_bool = str(my_functions.reminder_check('rest'))
        entertain_bool = str(my_functions.reminder_check('entertain'))
        arg = {
            "water": water_bool,
            "meditate": meditate_bool,
            "exercise": exercise_bool,
            "relax": rest_bool,
            "entertain": entertain_bool
        }
        return render_template('reminders.html', **arg)
    water_bool = str(my_functions.reminder_check('water'))
    meditate_bool = str(my_functions.reminder_check('meditate'))
    exercise_bool = str(my_functions.reminder_check('exercise'))
    rest_bool = str(my_functions.reminder_check('rest'))
    entertain_bool = str(my_functions.reminder_check('entertain'))
    arg = {
        "water": water_bool,
        "meditate": meditate_bool,
        "exercise": exercise_bool,
        "relax": rest_bool,
        "entertain": entertain_bool
    }
    return render_template('reminders.html', **arg)


@app.route('/timetable', methods=['POST', 'GET'])
def timetable():
    if request.method == 'POST':
        task = request.form.get('name')
        link = request.form.get('link')
        time_per = request.form.get('curr_row')
        if task == "":
            task == "nan"
        if link == "":
            link = "nan"
        my_functions.set_time_table(time_per, task, link)
        array = my_functions.check_time_table()
        for i in range(len(array)):
            slot = array[i][0]
            if slot == '9-10':
                task1 = array[i][1]
                link1 = array[i][2]
            elif slot == '10-11':
                task2 = array[i][1]
                link2 = array[i][2]
            elif slot == '11-12':
                task3 = array[i][1]
                link3 = array[i][2]
            elif slot == '12-13':
                task4 = array[i][1]
                link4 = array[i][2]
            elif slot == '13-14':
                task5 = array[i][1]
                link5 = array[i][2]
            elif slot == '14-15':
                task6 = array[i][1]
                link6 = array[i][2]
            elif slot == '15-16':
                task7 = array[i][1]
                link7 = array[i][2]
            elif slot == '16-17':
                task8 = array[i][1]
                link8 = array[i][2]
            elif slot == '17-18':
                task9 = array[i][1]
                link9 = array[i][2]
            elif slot == '18-19':
                task10 = array[i][1]
                link10 = array[i][2]
            elif slot == '19-20':
                task11 = array[i][1]
                link11 = array[i][2]
            elif slot == '20-21':
                task12 = array[i][1]
                link12 = array[i][2]
        task_list = {
            "task1": task1,
            "task2": task2,
            "task3": task3,
            "task4": task4,
            "task5": task5,
            "task6": task6,
            "task7": task7,
            "task8": task8,
            "task9": task9,
            "task10": task10,
            "task11": task11,
            "task12": task12,
            "link1": link1,
            "link2": link2,
            "link3": link3,
            "link4": link4,
            "link5": link5,
            "link6": link6,
            "link7": link7,
            "link8": link8,
            "link9": link9,
            "link10": link10,
            "link11": link11,
            "link12": link12}
        for j in range(1, 13):
            if str(task_list["task"+str(j)]) == "nan":
                task_list["task"+str(j)] = ""
            if str(task_list["link"+str(j)]) == "nan":
                task_list["link"+str(j)] = ""
        return render_template('timetable.html', **task_list)

    # Normal
    array = my_functions.check_time_table()
    for i in range(len(array)):
        slot = array[i][0]
        if slot == '9-10':
            task1 = array[i][1]
            link1 = array[i][2]
        elif slot == '10-11':
            task2 = array[i][1]
            link2 = array[i][2]
        elif slot == '11-12':
            task3 = array[i][1]
            link3 = array[i][2]
        elif slot == '12-13':
            task4 = array[i][1]
            link4 = array[i][2]
        elif slot == '13-14':
            task5 = array[i][1]
            link5 = array[i][2]
        elif slot == '14-15':
            task6 = array[i][1]
            link6 = array[i][2]
        elif slot == '15-16':
            task7 = array[i][1]
            link7 = array[i][2]
        elif slot == '16-17':
            task8 = array[i][1]
            link8 = array[i][2]
        elif slot == '17-18':
            task9 = array[i][1]
            link9 = array[i][2]
        elif slot == '18-19':
            task10 = array[i][1]
            link10 = array[i][2]
        elif slot == '19-20':
            task11 = array[i][1]
            link11 = array[i][2]
        elif slot == '20-21':
            task12 = array[i][1]
            link12 = array[i][2]
    task_list = {
        "task1": task1,
        "task2": task2,
        "task3": task3,
        "task4": task4,
        "task5": task5,
        "task6": task6,
        "task7": task7,
        "task8": task8,
        "task9": task9,
        "task10": task10,
        "task11": task11,
        "task12": task12,
        "link1": link1,
        "link2": link2,
        "link3": link3,
        "link4": link4,
        "link5": link5,
        "link6": link6,
        "link7": link7,
        "link8": link8,
        "link9": link9,
        "link10": link10,
        "link11": link11,
        "link12": link12}
    for j in range(1, 13):
        if str(task_list["task"+str(j)]) == "nan":
            task_list["task"+str(j)] = ""
        if str(task_list["link"+str(j)]) == "nan":
            task_list["link"+str(j)] = ""
    return render_template('timetable.html', **task_list)


def alert():
    while True:
        current_time = datetime.datetime.now()
        if current_time.second == 0:
            while True:
                curr_time = datetime.datetime.now()
                water = str(my_functions.reminder_check('water')).lower()
                meditate = str(my_functions.reminder_check('meditate')).lower()
                exercise = str(my_functions.reminder_check('exercise')).lower()
                rest = str(my_functions.reminder_check('rest')).lower()
                entertain = str(
                    my_functions.reminder_check('entertain')).lower()
                if water == "true" and curr_time.minute == 0:
                    title = 'Pani peelo friends 😂'
                    message = 'Drink Water reminder by Time-it'
                    notification.notify(
                        title=title, message=message, app_icon="static/images/logo.ico", timeout=5, toast=False, app_name="Time-it")
                if meditate == "true":
                    if curr_time.hour == 9 and curr_time.minute == 0 or curr_time.hour == 18 and curr_time.minute == 0:
                        title = 'Meditate to relax your soul!'
                        message = 'Meditation reminder by Time-it'
                        notification.notify(
                            title=title, message=message, app_icon="static/images/logo.ico", timeout=5, toast=False, app_name="Time-it")
                if exercise == "true":
                    if curr_time.hour == 10 or curr_time.hour and curr_time.minute == 0 or curr_time.hour == 19:
                        title = 'Sometimes a workout is the only therapy you need!'
                        message = 'Exercise reminder by Time-it'
                        notification.notify(
                            title=title, message=message, app_icon="static/images/logo.ico", timeout=5, toast=False, app_name="Time-it")
                if rest == "true":
                    if curr_time.hour % 4 == 0 and curr_time.minute == 0 and 8 <= curr_time.hour <= 20:
                        title = 'Take a 5 min break to boost your productivity!'
                        message = 'Relax reminder by Time-it'
                        notification.notify(
                            title=title, message=message, app_icon="static/images/logo.ico", timeout=5, toast=False, app_name="Time-it")
                if entertain == "true":
                    if curr_time.hour % 3 == 0 and curr_time.minute == 0 and 9 <= curr_time.hour <= 21:
                        title = 'Did you watch the stand up of the day on the Time.It site?'
                        message = 'Entertainment reminder by Time-it'
                        notification.notify(
                            title=title, message=message, app_icon="static/images/logo.ico", timeout=5, toast=False, app_name="Time-it")
                time.sleep(60)


thread = threading.Thread(target=alert)
thread.start()

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
# app.run(use_reloader=False)
