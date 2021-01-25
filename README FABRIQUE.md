# FABRIQUE_2
Задача: спроектировать и разработать API для системы опросов пользователей

## Installation requirements
  * python3.9.0
  * Django==3.1.5
  * djangorestframework==3.12.2
  
## Installation guide
```
cd FABRIQUE_2/
pip install -r requirements.txt
cd FABRIQUE_2/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## API documentation

Full description:
http://127.0.0.1:8000/swagger/

### To create a survey:
* Request method: POST
* URL: http://127.0.0.1:8000/survey/surveys/
* Authorization: Basic Auth
* Body:
    * survey_name: name of the survey, string
    * end_date: the survey end date, format: YYYY-MM-DD HH:MM:SS
    * survey_description: description of the survey, string


### To update a survey:
* Request method: PATCH
* URL: http://127.0.0.1:8000/survey/surveys/[survey_id]/
* Authorization: Basic Auth
* Param:
    * survey_id 
* Body:
    * survey_name: name of the survey, string
    * end_date: the survey end date, format: YYYY-MM-DD HH:MM:SS (start date sets automatically)
    * survey_description: description of the survey, string


### To delete a survey:
* Request method: DELETE
* URL: http://127.0.0.1:8000/survey/surveys/[survey_id]/
* Authorization: Basic Auth
* Param:
    * survey_id


### To view all surveys:
* Request method: GET
* URL: http://127.0.0.1:8000/survey/surveys/
* Authorization: No



### To create a question:
* Request method: POST
http://127.0.0.1:8000/survey/questions/
* Authorization: Basic Auth
* Body:
    * survey: id of the survey, int
    * question_text: text of the question, string
    * question_type: one of the Choise model, ForeignKey


### To update a question:
* Request method: PATCH
* URL: http://127.0.0.1:8000/survey/questions/[question_id]/
* Authorization: Basic Auth
* Param:
    * question_id
* Body:
    * survey: id of the survey, int
    * question_text: text of the question, string
    * question_type: one of the Choise model, ForeignKey


### To delete a question:
* Request method: DELETE
* URL: http://127.0.0.1:8000/survey/questions/[question_id]/
* Authorization: Basic Auth
* Param:
    * question_id


### To create a choice:
* Request method: POST
* URL: http://127.0.0.1:8000/survey/choices/
* Authorization: Basic Auth
* Body:
    * choice_type: description of the choice, string



### To update a choice:
* Request method: PATCH
* URL: http://127.0.0.1:8000/survey/choices/[choice_id]/
* Authorization: Basic Auth
* Param:
    * choice_id
* Body:
    * choice_type: description of the choice, string


### To delete a choice:
* Request method: DELETE
* URL: http://127.0.0.1:8000/survey/choices/[choice_id]/
* Authorization: Basic Auth
* Param:
    * choice_id


### To create an answer:
* Request method: POST
* URL: http://127.0.0.1:8000/survey/answers/
* Authorization: No
* Body:
    * user_id: id the user, int
    * survey: answer's survey, ForeignKey
    * question: answer's question, ForeignKey
    * choice: question's choice, ForeignKey
	* answer_text: text of the answer, string


### To view all answers:
* Request method: GET
* URL: http://127.0.0.1:8000/survey/answers/
* Authorization: No







  
