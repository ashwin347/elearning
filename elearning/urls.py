"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('faculity',views.renderFaculityLogin),
    path('welcome',views.renderWelcome),
    path('',views.renderWelcome),
    path('faculityloginvalidation',views.faculityLoginValidation),
    path('faculityhome',views.renderFaculityHome),
    path('faculitymanagequeries',views.renderFaculityQueries),
    path('faculitydeletequery',views.faculityDeleteQuery),
    path('faculitymanagechats',views.renderFaculityChats),
    path('faculityacceptrequest',views.faculityAcceptRequest),
    path('faculitydeleterequest',views.faculityDeleteRequest),
    path('faculitydeletefile',views.faculityDeleteFile),
    path('faculityprofile',views.renderFaculityProfile),
    path("updatefilerequest",views.updateFileRequest),
    path('downloadfile',views.downloadFile),
    path('showfilerequestlist',views.showFileRequestList),
    path('updatefaculityprofile',views.updateFaculityProfile),
    path('faculityhome',views.renderFaculityHome),
    path('faculityuploadfile',views.faculityUploadFile),
    path('faculitymanagefiles',views.renderFaculityFiles),
    path('student',views.renderStudentLogin),
    path('studentloginvalidation',views.studentLoginValidation),
    path('studenthome',views.renderStudentHome),
    path('studentviewmaterials',views.renderStudentMaterials),
    path('studentrequestfile',views.studentRequestFile),
    path('studentprofile',views.renderStudentProfile),
    path('updatestudentprofile',views.updateStudentProfile),
    path('studentmanagechats',views.renderStudentChats),
    path('displayqueryinfo',views.showQueryInfo),
    path('submitqueryreply',views.submitQueryReply),
    path('studentnewchatrequest',views.studentInsertChatRequest),
    path('logout',views.logout),

]