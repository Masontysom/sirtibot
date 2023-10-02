# Sertibot
Automatic Question Paper Generator

In today’s educational landscape, the demand for efficient and streamlined processes has grown exponentially. One such critical task is the generation of question papers, which requires careful consideration of various factors like question bank management, subject distribution, difficulty levels, and formatting. To address this challenge, we have developed an automated Question Paper Generator using Django Python. 

Introducing Sirtibot: Revolutionizing Question Paper Generation
In the fast-paced world of education, where instructors strive to provide high quality assessments and enriching learning experiences, a cutting-edge tool emerges to simplify a critical task – the creation of question papers. 
Welcome to Sirtibot, your indispensable partner in crafting thoughtful, diverse, and impeccably balanced question papers.

To run the file user should run the folling pip commands in the command prompt : 
```
pip install django
pip install nltk
pip install transformers
pip install openai
pip install flashtext
pip install Pywsd
pip install summarizer
pip install fpdf
pip install openpyxl
```

MCQ Generation Logic: The logic for preprocessing text, extracting keywords, generating summaries, and generating MCQs from the processed text. It follows the pattern of uploading a text file, reading its content, and then performing the required processing steps.

Question : openai, Api is used in it.

After all the pip are installed last step :

Go to the folder where the manage.py file is seen usualy on the first page and open cmd their then run 
```
py manage.py runserver
```

It will take some time for nltk to download and pwd so be patient.


(Optional)if want virtual Environment :
  ```
  py -m venv venv
  ```
  The name of the virtual environment is your choice my name is venv
  
  
  Then we have to activate it by the command:
  ```
  venv\Scripts\activate
  ```
  to run the file run all the ** pip commands ** in the virtual Environment 
  done then manage.py command and set to go.



(error)
if any error in data base :
```
python manage.py migrate
```

