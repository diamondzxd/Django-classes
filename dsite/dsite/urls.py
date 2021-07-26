"""dsite URL Configuration

The `urlpatterns` list routes URLs to main. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function main
    1. Add an import:  from my_app import main
    2. Add a URL to urlpatterns:  path('', main.home, name='home')
Class-based main
    1. Add an import:  from other_app.main import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views as main
from formsdemo import views as forms
from modelsdemo import views as models
from modelformdemo import views as modelform
from filedemo import views as filedemo
from foreigndemo import views as foreign
from cookiedemo import views as cookie
from sessiondemo import views as session
from ajaxdemo import views as ajax

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main.Index),
    path('page1/', main.Page1),
    path('page2/',main.Page2),
    path('page3/',main.Page3),
    path('page4/',main.Page4),
    path('page5/',main.Page5),
    path('page6/',main.Page6),
    path('page7/',main.Page7),
    path('page8/',main.Page8),
    path('page9/',main.Page9),
    path('form1/',main.form1),
    path('form2/',main.form2),


    #Forms Demo App
    path('formsdemo/form1', forms.form1),
    path('formsdemo/form2', forms.form2),
    path('formsdemo/form3', forms.form3),
    path('formsdemo/form4', forms.form4),
    path('formsdemo/form5', forms.form5),


    #Models Demo App
    path('modelsdemo/model1', models.AddRequest),
    path('modelsdemo/model2', models.DisplayRecord),
    path('modelsdemo/model3', models.UpdateStudent),
    path('modelsdemo/model4', models.DeleteStudent),
    path('modelsdemo/form1', models.form1),
    path('modelsdemo/displayastable', models.DisplayRecordsAsTable),
    path('modelsdemo/displayasgrid', models.DisplayRecordsAsGrid),
    path('modelsdemo/updateform', models.UpdateRecordForm),
    path('modelsdemo/deleteform', models.DeleteRecordForm),
    path('modelsdemo/updateform2/<id>',models.UpdateRecordForm2),
    path('modelsdemo/deleteform2/<id>',models.DeleteRecordForm2),


    #ModelFormDemo App
    path('modelformdemo/add', modelform.AddStudent),
    path('modelformdemo/display', modelform.DisplayStudent),
    path('modelformdemo/update', modelform.UpdateStudent),
    path('modelformdemo/delete', modelform.DeleteStudent),

    #FileDemo App
    path('filedemo/form1', filedemo.form1),
    path('filedemo/display', filedemo.display),
    path('filedemo/multi', filedemo.multi),

    #ForeignDemo APP
    path('foreigndemo/addcategory', foreign.AddCategory),
    path('foreigndemo/displaycategory', foreign.DisplayCategory),
    path('foreigndemo/addproduct', foreign.AddProduct),
    path('foreigndemo/displayproduct', foreign.DisplayProduct),
    path('foreigndemo/addbrand', foreign.AddBrand),
    path('foreigndemo/displaybrand', foreign.DisplayBrand),

    #CookieDemo App
    path('cookiedemo/savecookie', cookie.SaveCookie),
    path('cookiedemo/readcookie', cookie.ReadCookie),
    path('cookiedemo/deletecookie', cookie.DeleteCookie),
    path('cookiedemo/citypref', cookie.CityPref),
    path('cookiedemo/cookiedemo_home', cookie.cookiedemo_Home),
    path('cookiedemo/cookiedemo_logout', cookie.cookiedemo_logout),

    #SessionDemo App
    path('sessiondemo/addsession', session.AddSession),
    path('sessiondemo/readsession', session.ReadSessionData),
    path('sessiondemo/deletesession', session.DeleteSession),
    path('sessiondemo/question_home', session.Questions_home),
    path('sessiondemo/question_main', session.Questions_main),

    #AJAX Demo App
    path('ajaxdemo/basicajax', ajax.BasicAjax),
    path('ajaxdemo/basicresponse', ajax.BasicResponse),
    path('ajaxdemo/bootstrapdemo1', ajax.BootStrapDemo1),
    path('ajaxdemo/bootstrapdemo2', ajax.BootStrapDemo2),
    path('ajaxdemo/displayorders', ajax.DisplayOrders),
    path('ajaxdemo/fetchorders', ajax.FetchOrders),
    path('ajaxdemo/addorder', ajax.AddOrder),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)