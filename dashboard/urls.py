from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("tables/", views.tables, name="tables"),
    path("grid/", views.grid, name="grid"),
    path("form-basic/", views.form_basic, name="form-basic"),
    path("form-wizard/", views.form_wizard, name="form-wizard"),
    path("buttons/", views.buttons, name="buttons"),
    path("elements/", views.elements, name="elements"),
    path("mcqtopdf/", views.mcqtopdf, name="mcqtopdf"),
    path("theorytopdf/", views.theorytopdf, name="theorytopdf"),  
    path("generate_mcqs/", views.generate_mcqs, name="generate_mcqs"),
    path("manual_mcq/", views.manual_mcq, name="manual_mcq"),
    path("addquestion/", views.addquestion, name="addquestion"),
    path("manual_result/",views.manual_result, name="manual_result"),
    path('generate_questions/', views.generate_questions, name='generate_questions'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('display_question_paper/', views.display_question_paper, name='display_question_paper'),
    path('generate_question_paper/', views.generate_question_paper, name='generate_question_paper'),
    path("generate_question_paper_form/", views.generate_question_paper_form, name="generate_question_paper_form"),
    path('display_question_form/', views.display_question_form, name='display_question_form'),
    path('generate_questions_from_text/', views.generate_questions_from_text, name='generate_questions_from_text'),
    path('remove_mcq/', views.remove_mcq, name='remove_mcq'),
    

    path('remove_question/', views.remove_question, name='remove_question'),
    
    path("viewprofile",views.view_profile, name='viewprofile'),
    path("upload_and_display_excel",views.upload_and_display_excel, name='upload_and_display_excel'),

    #path(theorytotext,user_mcqs)
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)