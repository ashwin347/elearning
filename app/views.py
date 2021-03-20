from django.shortcuts import render
import sys
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
sys.path.append(r'C:\Users\best\Anaconda3\Lib\site-packages')
import mysql.connector
# Create your views here.
def sessionCheck(request,sesType):
    if request.session['type'] == sesType:
        return request.session['id'] 
    else:
        return 'false'
def renderFaculityLogin(request):
    return render(request,'faculityLogin.html')
def renderWelcome(request):
    if 'id' in request.session:
        if request.session['type']=='f':
            return renderFaculityHome(request)
        else:
            return renderStudentHome(request)
    return render(request,'welcome.html')
def renderFaculityHome(request):
    id=sessionCheck(request,'f')
    if id!='false':
        return render(request,'faculityHome.html')  
    else:
        return render(request,'welcome.html')
def renderFaculityQueries(request):
    id=sessionCheck(request,'f')
    if id=='false':
        dom='s'
        id=str(sessionCheck(request,'s'))
    else:
        dom='f'    
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    if dom=='f':
        file='faculityManageQueries.html'
        cursor.execute('SELECT q.id,s.studentname , q.querytopic, q.status FROM queries q join students s on q.studentid=s.id')
    else:
        file='studentManageQueries.html'
        cursor.execute("SELECT q.id , q.querytopic, q.status FROM queries q join students s on q.studentid=s.id where s.id='"+id+"'")
    queries=cursor.fetchall()
    return render(request,file,{'queries':queries})

@csrf_exempt
def faculityLoginValidation(request):          # validates user login
    email=request.POST['email']
    password=request.POST['password']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    print(email,password)
    cursor.execute('SELECT * FROM `faculities` where email="'+email+'" and password= "'+password+'"')
    users=cursor.fetchall()
    if len(users)==0:
        return render(request,'faculityLogin.html',{'error':'True'})
    else:
        request.session['type']='f'
        request.session['id']=users[0][0]
        return renderFaculityHome(request)
def logout(request):
    if 'id' in request.session:
        del request.session['id']
    return render(request,'welcome.html')
def showQueryInfo(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    qid=request.GET['id']
    cursor.execute('select id,querytopic,querydescription,status FROM `queries` where id= "'+qid+'"')
    query=cursor.fetchall()
    if query[0][3]=='replied':
        cursor.execute('select q.repliedfaculityid,q.reply,f.faculityname FROM queries q join faculities f on q.repliedfaculityid=f.id where q.id= "'+qid+'"')
        extra=cursor.fetchall()
    query=query+extra
    return render(request,'displaySingleQuery.html',{'query':query})
@csrf_exempt
def submitQueryReply(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    id=sessionCheck(request,'f')
    reply=request.GET['reply']
    qid=request.GET['qid']
    if id=='false':
        return HttpRespone('none')
    cursor.execute("UPDATE queries SET status='replied',repliedfaculityid='"+str(id)+"',reply='"+reply+"' WHERE id = '"+str(qid)+"'")
    return HttpResponse('success')
@csrf_exempt
def faculityDeleteQuery(request):
    id=request.POST['id']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute('Delete FROM `queries` where id= "'+id+'"')
    connection.commit()
    cursor.close()
    return renderFaculityQueries(request)
@csrf_exempt
def renderFaculityChats(request):
    id=sessionCheck(request,'f')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute("SELECT c.id,s.studentname FROM chatrequests c JOIN faculities f on c.faculityid="+str(id)+" JOIN students s on s.id=c.studentid WHERE f.id=1 AND c.status='pending'")
    requests=cursor.fetchall()
    return render(request,'faculityChatRequests.html',{'requests':requests})
@csrf_exempt
def faculityDeleteRequest(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    id=request.POST['id']
    cursor.execute('Update `chatrequests` set status="rejected" where id= "'+id+'"')
    connection.commit()  
    print('yes')  
    return renderFaculityChats(request)
@csrf_exempt
def updateFileRequest(request):
    fid=request.POST['fid']
    sid=request.POST['sid']
    status=request.POST['status']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    print("update filerequests set status='"+status+"' where fileid='"+fid+"' and studentid='"+sid+"'")
    cursor.execute("update filerequests set status='"+status+"' where fileid='"+fid+"' and studentid='"+sid+"'")
    connection.commit()
    return showFileRequestList(request)
def showFileRequestList(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    try:
        fid=request.GET['id']
    except:
        fid=request.POST['fid']
    cursor.execute("SELECT f.studentid,s.studentname FROM filerequests f LEFT JOIN students s on s.id=f.studentid WHERE f.status='pending' and f.fileid='"+fid+"'")
    requests=cursor.fetchall()
    connection.commit()
    return render(request,'showFileRequestList.html',{'requests':requests,'fid':fid})
@csrf_exempt
def faculityAcceptRequest(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    id=request.POST['id']
    cursor.execute('Update `chatrequests` set status="accepted" where id= "'+id+'"')
    connection.commit()
    return render(request,'faculityChatRequests.html')
def renderFaculityProfile(request):
    id=request.session['id']
    id=str(id)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute('select * from faculities where id= "'+id+'"')
    faculity=cursor.fetchall()
    connection.commit()
    faculity=faculity[0]
    print(faculity)
    return render(request,'faculityProfile.html',{'faculity':faculity})

def renderStudentLogin(request):
    return render(request,'studentLogin.html')

@csrf_exempt
def studentLoginValidation(request):          # validates user login
    email=request.POST['email']
    password=request.POST['password']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    print(email,password)
    cursor.execute('SELECT * FROM `students` where email="'+email+'" and password= "'+password+'"')
    users=cursor.fetchall()
    if len(users)==0:
        return render(request,'studentLogin.html',{'error':'True'})
    else:
        request.session['type']='s'
        request.session['id']=users[0][0]
        return renderStudentHome(request)
def renderStudentHome(request):
    return render(request,'studentHome.html')
def renderStudentMaterials(request):
    id=sessionCheck(request,'s')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    if 'q' in request.GET:
        q=request.GET['q']
        print(q)
        cursor.execute("select *,'pending' from files WHERE filename LIKE '%"+q+"%' OR fileinfo LIKE '%"+q+"%'")
    else:
        cursor.execute("SELECT `files`.`id`,`files`.`filename`,`files`.`fileinfo`, `filerequests`.`status` FROM `files` LEFT JOIN `filerequests` ON files.id = filerequests.fileid AND filerequests.studentid = "+str(id))
    files=cursor.fetchall()
    return render(request,'studentMaterials.html',{'files':files})
def studentRequestFile(request):
    id=sessionCheck(request,'s')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    fileid=request.GET['fileid']
    cursor.execute("INSERT INTO `filerequests`(`fileid`, `studentid`, `status`) VALUES ('"+str(fileid)+"','"+str(id)+"','pending')")
    connection.commit()
    return renderStudentMaterials(request)
def renderStudentChats(request):
    return render(request,'studentChats.html')
def renderStudentProfile(request):
    id=sessionCheck(request,'s')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `students` where id="'+str(id)+'"')
    profile=cursor.fetchall()[0]
    return render(request,'studentProfile.html',{'profile':profile})
@csrf_exempt
def updateStudentProfile(request):
    id=sessionCheck(request,'s')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    password=request.POST['password']
    print("UPDATE `students` SET `studentname`='"+name+"',`email`='"+email+"',`password`='"+password+"',`phone`='"+phone+"' WHERE id='"+str(id)+"'")
    cursor.execute("UPDATE `students` SET `studentname`='"+name+"',`email`='"+email+"',`password`='"+password+"',`phone`='"+phone+"' WHERE id='"+str(id)+"'")
    connection.commit()
    return render(request,'studentProfile.html')
@csrf_exempt
def updateFaculityProfile(request):
    id=sessionCheck(request,'f')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    name=request.POST['name']
    phone=request.POST['department']
    email=request.POST['email']
    password=request.POST['password']
    cursor.execute("UPDATE `faculities` SET `faculityname`='"+name+"',`email`='"+email+"',`password`='"+password+"',`department`='"+department+"' WHERE id='"+str(id)+"'")
    connection.commit()
    return render(request,'studentProfile.html')
@csrf_exempt
def downloadFile(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    fid=request.POST['id']
    cursor.execute('select filename from files where id="'+fid+'"')
    fname=cursor.fetchall()[0][0]
    try:
        os.chdir('tmp')
    except:
        pass
    file=open(fname,'rb')
    response = HttpResponse(file.read(), content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'inline; filename=tmp\\' + fname
    return response
def renderFaculityFiles(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute('SELECT f.*, COUNT(r.fileid) AS "counts" FROM files f LEFT JOIN filerequests r on f.id=r.fileid  GROUP BY f.id')
    files=cursor.fetchall()   
    return render(request,'faculityManageFiles.html',{'files':files})
@csrf_exempt
def faculityUploadFile(request):
    file=request.FILES['file']
    path = default_storage.save('tmp/'+file._name, ContentFile(file.read()))
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `files`(`filename`, `fileinfo`) VALUES ('"+file._name+"',' ')")
    connection.commit()
    return HttpResponse('None')
@csrf_exempt
def faculityDeleteFile(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    id=request.POST['id']
    cursor.execute("delete from files where id='"+id+"'")
    connection.commit()
    return HttpResponse('none')
def studentInsertChatRequest(request):
    id=sessionCheck(request,'s')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    facid=request.GET['faculityid']
    req=request.GET['req']
    if req=='yes':
        print("Update chatrequests set  status='pending' where studentid='"+str(id)+"' and faculityid='"+facid+"'")
        cursor.execute("Update chatrequests set  status='pending' where studentid='"+str(id)+"' and faculityid='"+facid+"'")
    else:
        cursor.execute("INSERT INTO chatrequests(studentid, faculityid, status) VALUES ('"+str(id)+"','"+facid+"','pending')")
    connection.commit()

    return renderStudentChats(request)

@csrf_exempt
def renderStudentChats(request):
    id=sessionCheck(request,'s')
    if id=='false':
        return renderWelcome(request)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='elearning')
    cursor=connection.cursor()
    cursor.execute("SELECT f.id,f.faculityname,c.status FROM faculities f LEFT JOIN chatrequests c ON f.id = c.faculityid AND c.studentid = '"+str(id)+"'")
    faculities=cursor.fetchall()   
    return render(request,'studentChatRequests.html',{'faculities':faculities})
