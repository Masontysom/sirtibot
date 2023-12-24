# Sirtibot
Automatic Question Paper Generator
need python version == Python 3.8.6

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
python -m spacy download en
pip install torch
pip install bert-extractive-summarizer
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


Change the api to get the question to be generated, dashboard/view.py line 385 and setting line 41
https://github.com/Masontysom/sirtibot/blob/297df97261c52a3540a0ffdc3682af0fee3da7cb/dashboard/views.py#L384
https://github.com/Masontysom/sirtibot/blob/297df97261c52a3540a0ffdc3682af0fee3da7cb/sertibot/settings.py#L41

(error)
if the pke is not working run this: -
```
pip install git+https://github.com/boudinfl/pke.git
```


if any error in data base :
```
python manage.py migrate
```

