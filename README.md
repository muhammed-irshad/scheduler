# scheduler


* **Clone Repo**
  * `git clone https://github.com/shajal01/scheduler.git`
* **Install requirements**
  * `pip install -r requirements.txt`
* **Migrate**
  * `python manage.py migrate`
* **Run django server**
  * `python manage.py runserver`


### Endpoints

* **Register users**

  * url: `http://127.0.0.1:8000/api/v1/core/register_time/`
  * method: `post`
  * request body: `{ from_time:10:00 am to_time:1:00 pm }`
* **Available time slots**

  * url: `http://127.0.0.1:8000/api/v1/core/available_slots/`
  * method: `get`
  * query params: `interviewer, candidate`
  * eg: `http://127.0.0.1:8000/api/v1/core/available_slots/?interviewer_id=1&candidate_id=2`
  * output: `{ "Time available": [[10, 11],[11, 12]] }`
