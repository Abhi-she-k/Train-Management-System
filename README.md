# Train-Management-System

The Traffic Management System (TMS) was designed to help monitor, track, and control traffic in an efficient and safe manner. The system allows for creating train schedules, track and show train times/routes, rerouting and canceling trains, and coordinating trains. The TMS was enhanced in the second iteration of the design to integrate more features for a safer and robust system. The system design allows for flexibility by leaving room for future enhancements, creating a scalable, maintainable, and secure Traffic Management System.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python Installed on System

### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone github repo onto system
2. Open terminal and move into the Train-Management-System directory
3. Change file path for json in the admin.py file in objects to the path of adminInfo.json for the relative system
4. Change file path for json in the trainSchedule.py file in objects to the path of trainSchedule.json for the relative system
5. Set FLASK_APP variable in through terminal with command

```
FLASK_APP=/Backend/Deployment/app.py
```

6. Install Flask

```
pip install Flask
```

7. run flask server

```
python -m flask run
```

or

```
flask run
```



## Running the tests

To run the tests:

Change this code snippets in admin.py: 

```
from objects.user import user
from objects.trainSchedule import trainSchedule
# from user import user
# from trainSchedule import trainSchedule
```

To:

```
# from objects.user import user
# from objects.trainSchedule import trainSchedule
 from user import user
 from trainSchedule import trainSchedule
```

Run the test.py file 


## Built With

* [Flask](https://flask.palletsprojects.com/en/2.2.x/) - The web framework used
* [Python](https://www.python.org/doc/) - Backend
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Developement of Frontend
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Styling Frontend



## Authors

* **Abhishek Paul** - (https://github.com/Abhi-she-k)
* **Nathan Chan** - (https://github.com/NatlC)
* **Sufyan Ghani** - (https://github.com/SufyanG20)
* **Shahrukh Saeed** - (https://github.com/shahrukh-saeed)
* **Diego Diaz** - (https://github.com/towel-cool)
* **Shakeer Nawaz** - (https://github.com/shakeern)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.



