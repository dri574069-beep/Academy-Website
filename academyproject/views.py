from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import UserRegis,LoginForm,StudentAccForm,TeacherForms,CourseForms,ClassesForm,AttendenceForms,AdminLogin,deleteAttends,deletestudents,deleteTeacher,DeleteCourses,deleteclass,EnrollForms,subjectForms,deleteAttenforTeacher,WhyCooseUsForm,ContactInfoForm,AdmissionForm,DeleteEnroll
from .models import registeration,StudentAcc,TeacherAcc,Course,Classes,Attendence,Enrollment,SubjectsModel,WhychooseUsModel,CantactInfoModel,AddmissionModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
# Create your views here.
def signIn(request):
    # user=User.objects.create_superuser(
    #     username="Admin",
    #     email="dri574069@gmail.com",
    #     password="Blood_Suckers@Midnight47"
    # )
    # print("Super User successfully created")
    regis=UserRegis()
    if request.method=="POST":
        regis=UserRegis(request.POST)
        if regis.is_valid():
            Name=regis.cleaned_data['Name']
            password=regis.cleaned_data['password']
            email=regis.cleaned_data['email']
            role=regis.cleaned_data['role']
            DateofBirth=regis.cleaned_data['DateofBirth']
            age=regis.cleaned_data['age']
            if User.objects.filter(username=Name).exists():
                print("user already exists")
                return redirect("userauthentication")
            user=User.objects.create_user(
                username=Name,
                password=password,
                email=email
            )
            registeration.objects.create(
                user=user,
                role=role,
                DateofBirth=DateofBirth,
                age=age
            )
            print("User created!!")
            return redirect("userauthentication")
    return render(request,"registeration.html",{"regis":regis})
def userauthentication(request):
    log=LoginForm()
    if request.method=="POST":
        log=LoginForm(request.POST)
        if log.is_valid():
            username=log.cleaned_data["username"]
            password=log.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user is not None:
                print("LOGIN:", user.username)
                print("SUPERUSER:", user.is_superuser)
                login(request,user)
                if user.is_superuser:
                    return redirect("Admin")
                elif user.registeration.role=="Teacher":
                    return redirect("TeacherHome")
                elif user.registeration.role=="User":
                    return redirect("UserHomie")
                else:
                    return redirect("home")
            else:
                print("user does not exists")
                return redirect("signIn")
    return render(request,"login.html",{"log":log})
def UserHomie(request):
    return render(request,"UserHomePage.html")
def showAllTeachersForUser(request):
    teacher=TeacherAcc.objects.all()
    return render(request,"AllTeachersForUser.html",{"teacher":teacher})
def showTeachersForUsers(request,id):
    teacher=TeacherAcc.objects.filter(id=id)
    return render(request,"TeachersInfoForUsers.html",{"teacher":teacher})
def Admin(request):
    return render(request,"Admin.html")
def TeacherHome(request):
    return render(request,"TeacherHome.html")
def AdminAuthentication(request):
    admin=AdminLogin()
    if request.method=="POST":
        admin=AdminLogin(request.POST)
        if admin.is_valid():
            username=admin.cleaned_data["user_name"]
            password=admin.cleaned_data["password"]
            user=authenticate(
                request,
                username=username,
                password=password
            )
            if user is not None:
                print("Welcome superuser")
                login(request,user)
                return redirect("AdminHome")
            else:
                print("sorry wrong password or username")
                return redirect("Admin")
    return render(request,"AdminForm.html",{"admin":admin})
def is_admin(user):
    return user.is_superuser
@user_passes_test(is_admin,)
def showStudentsForAdmin(request,id):
    student=StudentAcc.objects.filter(id=id)
    return render(request,"StudentsDataForAdmin.html",{"student":student})
@user_passes_test(is_admin,)
def EditStudent(request,id):
    student=StudentAcc.objects.get(id=id)
    if request.method=="POST":
        form=StudentAccForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect("showStudentsForAdmin",id=id)
    else:
        form=StudentAccForm(instance=student)
    return render(request,"EditStudent.html",{"form":form,"id":id})
@user_passes_test(is_admin)
def student(request):
    stName=StudentAcc.objects.all()
    return render(request,"student.html",{"stName":stName})
@user_passes_test(is_admin)
def deleteStudents(request):
    student=deletestudents()
    if request.method=="POST":
        student=deletestudents(request.POST)
        if student.is_valid():
            stId=student.cleaned_data["stId"]
            std=StudentAcc.objects.filter(id=stId)
            if std.exists():
                std.delete()
                return redirect("student")
            else:
                print("object dosent exists")
    return render(request,"AttendenceLinks.html",{"student":student})
@user_passes_test(is_admin)
def Teacher(request):
    teacher=TeacherAcc.objects.all()
    return render(request,"teacher.html",{"teacher":teacher})
@user_passes_test(is_admin)
def EditTeachers(request,id):
    teacher=TeacherAcc.objects.get(id=id)
    if request.method=="POST":
        teacherForm=TeacherForms(request.POST,request.FILES,instance=teacher)
        if teacherForm.is_valid():
            teacherForm.save()
            return redirect('ShowTeachersForAdmin',id=id)
    else:
        teacherForm=TeacherForms(instance=teacher)
    return render(request,"EditTeachers.html",{'Tform':teacherForm,"id":id})
@user_passes_test(is_admin)
def ShowTeachersForAdmin(request,id):
    teachers=TeacherAcc.objects.filter(id=id)
    return render(request,"TeachersForAdmin.html",{"teachers":teachers})
@user_passes_test(is_admin)
def deleteTeachers(request):
    teacher=deleteTeacher()
    if request.method=="POST":
        teacher=deleteTeacher(request.POST)
        if teacher.is_valid():
            TId=teacher.cleaned_data["TId"]
            th=TeacherAcc.objects.filter(id=TId)
            if th.exists():
                th.delete()
                return redirect("Teacher")
            else:
                print("object does not exist")
    return render(request,'attendenceLinks.html')          
@user_passes_test(is_admin)
def Courses(request):
    courses=Course.objects.all()
    return render(request,"Courses.html",{"course":courses})
@user_passes_test(is_admin)
def CourseForAdmin(request,id):
    courses=Course.objects.filter(id=id)
    return render(request,"CoursesForAdmin.html",{"courses":courses})
@user_passes_test(is_admin)
def editCourses(request,id):
    course=Course.objects.get(id=id)
    if request.method=="POST":
        Cform=CourseForms(request.POST,request.FILES,instance=course)
        if Cform.is_valid():
            Cform.save()
            return redirect('CourseForAdmin',id=id)
    else:
        Cform=CourseForms(instance=course)
    return render(request,'EditCourse.html',{"Cform":Cform,"id":id})
@user_passes_test(is_admin)
def DeleteCourse(request):
    course=DeleteCourses()
    if request.method=="POST":
        course=DeleteCourses(request.POST)
        if course.is_valid():
            CId=course.cleaned_data["CId"]
            courses=Course.objects.filter(id=CId)
            if courses.exists():
                courses.delete()
                return redirect("Courses")
            else:
                print("object dosent exist")
    return render(request,"Courses.html")
@user_passes_test(is_admin)
def Claas(request):
    classes=Classes.objects.all()
    return render(request,"classes.html",{"Cls":classes})
@user_passes_test(is_admin)
def showClassesDataForAdmin(request,id):
    classData=Classes.objects.filter(id=id)
    return render(request,"ClassesDataForAdmin.html",{"class":classData})
@user_passes_test(is_admin)
def EditClasses(request,id): #class
    classs=Classes.objects.get(id=id)
    if request.method=="POST":
        ClassForm=ClassesForm(request.POST,request.FILES,instance=classs)
        if ClassForm.is_valid():
            ClassForm.save()
            return redirect("showClassesDataForAdmin",id=id)
    else:
        ClassForm=ClassesForm(instance=classs)
    return render(request,"EditClasses.html",{"form":ClassForm,"id":id})
@user_passes_test(is_admin)
def deleteClass(request):
    clas=deleteclass()
    if request.method=="POST":
        clas=deleteclass(request.POST)
        if clas.is_valid():
            ClId=clas.cleaned_data["ClId"]
            cl=Classes.objects.filter(id=ClId)
            if cl.exists():
                cl.delete()
                return redirect("Claas")
            else:
                print("object dosent exists")
    return render(request,"Courses.html")
@user_passes_test(is_admin)
def attendence(request):
    attendence=Attendence.objects.all()
    return render(request,"AttendenceLinks.html",{"attendence":attendence})
@user_passes_test(is_admin)
def AttendenceDataForUser(request,id):
    attendence=Attendence.objects.filter(id=id)
    return render(request,"attendenceforAdmin.html",{"attendence":attendence,"attend":id})
def EditAttendence(request,id):
    attend=Attendence.objects.get(id=id)
    if request.method=="POST":
        AForm=AttendenceForms(request.POST,request.FILES,instance=attend)
        if AForm.is_valid():
            AForm.save()
            return redirect("AttendenceDataForUser",id=id)
    else:
        AForm=AttendenceForms(instance=attend)
    return render(request,"EditAttendence.html",{"Aform":AForm,"id":id})
@user_passes_test(is_admin)
def deleteAttendence(request):
    attend=deleteAttends()
    if request.method=="POST":
        attend=deleteAttends(request.POST)
        if attend.is_valid():
            attId=attend.cleaned_data["attId"]
            ate=Attendence.objects.filter(id=attId)
            if ate.exists():
                ate.delete()
                return redirect("attendence")
            else:
                print("object dosent exists")
    return render(request,"attendenceforAdmin.html")
@user_passes_test(is_admin,login_url="AdminAuthentication")
def AdminHome(request):
    return render(request,"AdminHome.html")
def home(request):
    stdData=StudentAcc.objects.all()
    AllCourses=Course.objects.all()
    classs=Classes.objects.all()
    Atten=Attendence.objects.all()
    return render(request,"Homepage.html",{"stdData":stdData,"Courses":AllCourses,"class":classs,"attendence":Atten})
def studentForms(request):
    std=StudentAccForm()
    if request.method=="POST":
        std=StudentAccForm(request.POST)
        if std.is_valid():
            studentName=std.cleaned_data["studentName"]
            dateOfBirth=std.cleaned_data["dateOfBirth"]
            gender=std.cleaned_data["gender"]
            phone_number=std.cleaned_data["ParentphoneNum"]
            address=std.cleaned_data["address"]
            Parent_or_guardian_name=std.cleaned_data["parentOrGuardianName"]
            AddmissionDate=std.cleaned_data["AdsmissionDate"]
            status=std.cleaned_data["status"]
            if StudentAcc.objects.filter(studentName=studentName).exists():
                print("student already exists")
                return redirect("home")
            student=StudentAcc.objects.create(
                    studentUser=request.user,
                    studentName=studentName,
                    dateOfBirth=dateOfBirth,
                    gender=gender,
                    ParentphoneNum=phone_number,
                    address=address,
                    parentOrGuardianName=Parent_or_guardian_name,
                    AdsmissionDate= AddmissionDate,
                    status=status
            )
            return redirect("showStudentData")
    return render(request,"studentForm.html",{"student":std})
def showStudentData(request):
    norm=request.user
    student=StudentAcc.objects.get(studentName=norm.username)
    return render(request,"showStudetnData.html",{"std":student})
def GetTeacherData(request):
    Tforms=TeacherForms()
    if request.method=="POST":
        Tforms=TeacherForms(request.POST)
        if Tforms.is_valid():
            Teacher_name=Tforms.cleaned_data["Teacher_name"]
            phoneNumber=Tforms.cleaned_data["phoneNumber"]
            qualification=Tforms.cleaned_data["qualification"]
            specialization=Tforms.cleaned_data["specialization"]
            joining_date=Tforms.cleaned_data["joining_date"]
            status=Tforms.cleaned_data["status"]
            if TeacherAcc.objects.filter(Teacher_name=Teacher_name).exists():
                print("Sorry user already exists")
                return redirect("home")
            teacher=TeacherAcc.objects.create(
                TeacherUser=request.user,
                Teacher_name=Teacher_name,
                phoneNumber=phoneNumber,
                qualification=qualification,
                specialization=specialization,
                joining_date=joining_date,
                status=status,
            )
            print("user successfully made")
            return redirect("showTeacherData",id=teacher.id)
    return render(request,"TeacherForms.html",{"forms":Tforms})
def allTeacherData(request):
    teacher=TeacherAcc.objects.all()
    return render(request,"teacherdatalinks.html",{"teacher":teacher})
def showTeacherData(request,id):
    teacher=TeacherAcc.objects.filter(id=id)
    return render(request,"ActualTeacherData.html",{"teacher":teacher})
def GetCourseData(request):
    course=CourseForms()
    user=request.user
    if request.method=="POST":
        course=CourseForms(request.POST)
        if course.is_valid():
            CourseName=course.cleaned_data["CourseName"]
            description=course.cleaned_data["description"]
            duration=course.cleaned_data["duration"]
            fee=course.cleaned_data['fee']
            CourseTeacher=course.cleaned_data["CourseTeacher"]
            level=course.cleaned_data["level"]
            start_date=course.cleaned_data["start_date"]
            end_date=course.cleaned_data["end_date"]
            status=course.cleaned_data["status"]
            if Course.objects.filter(CourseName=CourseName).exists():
                print("Object already exists")
                return  redirect("home")
            courses=Course.objects.create(
                CourseName=CourseName,
                description=description,
                duration=duration,
                fee=fee,
                CourseTeacher=CourseTeacher,
                level=level,
                start_date=start_date,
                end_date=end_date,
                status=status
            )
            print("objects course created")
            return redirect("showCourses",id=courses.id)
    return render(request,"CourseForm.html",{"course":course})
def showCourses(request,id):
    courses=Course.objects.filter(id=id)
    return render(request,"ShowCourses.html",{'courses':courses})
def getClassesData(request):
    classes=ClassesForm()
    if(request.method=="POST"):
        classes=ClassesForm(request.POST)
        if classes.is_valid():
            className=classes.cleaned_data["className"]
            Teacher=classes.cleaned_data["Teacher"]
            days=classes.cleaned_data["days"]
            start_time=classes.cleaned_data["start_time"]
            end_time=classes.cleaned_data["end_time"]
            room=classes.cleaned_data['room']
            capacity=classes.cleaned_data["capacity"]
            if Classes.objects.filter(className=className).exists():
                print("object already exists")
                return render("home")
            data=Classes.objects.create(
                className=className,
                Teacher=Teacher,
                days=days,
                start_time=start_time,
                end_time=end_time,
                room=room,
                capacity=capacity
            )
            print("object Classes successfully created")
            return redirect("showClasses",id=data.id)
    return render(request,"ClassesForms.html",{"classes":classes})
def showClasses(request,id):
    clas=Classes.objects.filter(id=id)
    return render(request,"showClasses.html",{"class":clas})
def getAttenDate(request):
    atten=AttendenceForms()
    if request.method=="POST":
        atten=AttendenceForms(request.POST)
        if atten.is_valid():
            student=atten.cleaned_data["student"]
            isPresent=atten.cleaned_data["isPresent"]
            courseOrClass=atten.cleaned_data["courseOrClass"]
            date=atten.cleaned_data["date"]
            status=atten.cleaned_data["status"]
            Teacher=atten.cleaned_data["Teacher"]
            attendence=Attendence.objects.create(
                student=student,
                isPresent=isPresent,
                courseOrClass=courseOrClass,
                date=date,
                status=status,
                Teacher=Teacher
            )
            print("object attendence successfully created ")
            studentobj=StudentAcc.objects.get(studentName=student)
            return redirect("showAttendenceForTeachers")
    return render(request,"attendence.html",{"att":atten})
def allStudents(request):
    students=StudentAcc.objects.all()
    return render(request,"allstudentsAttendence.html",{"student":students})
def allStudentsforAdmin(request):
    students=StudentAcc.objects.all()
    return render(request,"allstudentsAttenforAdmin.html",{"student":students})
def showSataforAdmin(request,id):
    attend=Attendence.objects.filter(id=id)
    return render(request,"showSataforAdmin.html",{"attend":attend})
def showSata(request,id):
    attend=Attendence.objects.filter(id=id)
    return render(request,"showsttendence.html",{"attend":attend})
def StudEnrollment(request):
    enl=EnrollForms()
    if request.method=="POST":
        enl=EnrollForms(request.POST)
        if enl.is_valid():
            print("RAW POST:", request.POST)
            print("CLEANED:", enl.cleaned_data)
            student=enl.cleaned_data["student"]
            classs=enl.cleaned_data["classs"]
            subjects=enl.cleaned_data["subjects"]
            course=enl.cleaned_data["course"]
            DateOfBirth=enl.cleaned_data['DateOfBirth']
            gender=enl.cleaned_data['gender']
            PrevSchool=enl.cleaned_data["PrevSchool"]
            PrevClass=enl.cleaned_data['PrevClass']
            Address=enl.cleaned_data["Address"]
            Parent_Guardian_Name=enl.cleaned_data["Parent_Guardian_Name"]
            Relation_with_student=enl.cleaned_data["Relation_with_student"]
            phone_number=enl.cleaned_data["phone_number"]
            Email=enl.cleaned_data["Email"]
            print("Student =",subjects)
            print("Course = ",course)
            enroll=Enrollment.objects.create(
                student=student,
                classs=classs,
                DateOfBirth=DateOfBirth,
                gender=gender,
                PrevSchool=PrevSchool,
                PrevClass=PrevClass,
                Address=Address,
                Parent_Guardian_Name=Parent_Guardian_Name,
                Relation_with_student=Relation_with_student,
                phone_number=phone_number,
                Email=Email,
            )
            enroll.course.set(course)
            enroll.subjects.set(subjects)
            print("object enrollment successfully created")
            return redirect("showallEnrollForAdmin",id=enroll.id)
    return render(request,"enrollform.html",{"enroll":enl})
def showAllEnStd(request):
    end=Enrollment.objects.all()
    return render(request,"AllEnStd.html",{"end":end})
def showallEnrollForAdmin(request,id):
    enroll=Enrollment.objects.filter(id=id)
    return render(request,"EnrollmentData.html",{"enrolls":enroll})
def DeleteEnrollment(request):
    id=DeleteEnroll()
    if request.method=="POST":
        id=DeleteEnroll(request.POST)
        if id.is_valid():
            enId=id.cleaned_data["enId"]
            eobj=Enrollment.objects.filter(id=enId)
            if eobj.exists():
                eobj.delete()
                return redirect("showAllEnStd")
            else:
                print("objects dosent exists")
    return render(request,"EnrollmentData.html",{"id":id})
def getSubjectData(request):
    subj=subjectForms()
    if request.method=="POST":
        subj=subjectForms(request.POST)
        if subj.is_valid():
            name=subj.cleaned_data["name"]
            description=subj.cleaned_data["description"]
            level=subj.cleaned_data["level"]
            status=subj.cleaned_data["status"]
            Teacher=subj.cleaned_data["Teacher"]
            subject=SubjectsModel.objects.create(
                    name=name,
                    description=description,
                    level=level,
                    status=status,
                    Teacher=Teacher
            )
            return redirect('SubjectInfoForTeacher')
    return render(request,"subjectForms.html",{"subj":subj})
def allsubjects(request):
    subjects=SubjectsModel.objects.all()
    return render(request,"Subject.html",{"subss":subjects})
def getSubjects(request,id):
    subjects=SubjectsModel.objects.filter(id=id)
    return render(request,"subjectsHome.html",{"subbs":subjects})
def EditSubjects(request,id):
    subjects=SubjectsModel.objects.get(id=id)
    if request.method=="POST":
        subFor=subjectForms(request.POST,request.FILES,instance=subjects)
        if subFor.is_valid():
            subFor.save()
            return redirect("getSubjects",id=id)
    else:
        subFor=subjectForms(instance=subjects)
    return render(request,"EditSubjects.html",{"subs":subFor,"id":id})
#for teacher
def showTeachersData(request):
    teacher=TeacherAcc.objects.filter(Teacher_name=request.user.username)
    return render(request,"teacherData.html",{"teacher":teacher})
def TeacherDataForm(request):
    Tforms=TeacherForms()
    if request.method=="POST":
        Tforms=TeacherForms(request.POST)
        if Tforms.is_valid():
            Teacher_name=Tforms.cleaned_data["Teacher_name"]
            phoneNumber=Tforms.cleaned_data["phoneNumber"]
            qualification=Tforms.cleaned_data["qualification"]
            specialization=Tforms.cleaned_data["specialization"]
            joining_date=Tforms.cleaned_data["joining_date"]
            status=Tforms.cleaned_data["status"]
            if TeacherAcc.objects.filter(Teacher_name=Teacher_name).exists():
                print("Sorry user already exists")
                return redirect("showTeachersData")
            teacher=TeacherAcc.objects.create(
                TeacherUser=request.user,
                Teacher_name=Teacher_name,
                phoneNumber=phoneNumber,
                qualification=qualification,
                specialization=specialization,
                joining_date=joining_date,
                status=status,
            )
            print("user successfully made")
            return redirect("showTeachersData")
    return render(request,"TeacherForms.html",{"forms":Tforms})
def showTeacherCouurse(request):
    user=request.user
    teacher=TeacherAcc.objects.get(Teacher_name=user.username)
    course=Course.objects.filter(CourseTeacher=teacher)
    return render(request,"teacherCourse.html",{"course":course})
def showTeachersClasses(request):
    user = request.user

    try:
        teacher = TeacherAcc.objects.get(TeacherUser=user)
        classes = Classes.objects.filter(Teacher=teacher)

        return render(
            request,
            "ClassesForTeacher.html",
            {"classes": classes}
        )

    except TeacherAcc.DoesNotExist:
        return render(
            request,
            "ClassesForTeacher.html",
            {"classes": []}
        )
def SubjectInfoForTeacher(request):
    try:
        teacher = TeacherAcc.objects.get(TeacherUser=request.user)

        subjects = SubjectsModel.objects.filter(Teacher=teacher)

        return render(
            request,
            "SubjectInfoForTeacher.html",
            {"subs": subjects}
        )

    except TeacherAcc.DoesNotExist:
        return render(
            request,
            "SubjectInfoForTeacher.html",
            {"subs": []}
        )

@login_required
def showAttendenceForTeachers(request):

    teacher = TeacherAcc.objects.filter(
        TeacherUser=request.user
    ).first()

    if teacher is None:
        print("teacher doesnot exists")
    attend = Attendence.objects.filter(
        Teacher=teacher
    )

    return render(
        request,
        "AttendenceForTeachers.html",
        {"attend": attend}
    )
def DeleteAttenForTeachers(request):
    attend=deleteAttenforTeacher()
    if request.method=="POST":
        attend=deleteAttenforTeacher(request.POST)
        if attend.is_valid():
            atTIf=attend.cleaned_data["atTIf"]
            attendence=Attendence.objects.get(id=id)
            if attendence.exists():
                attendence.delete()
                return redirect("showAttendenceForTeachers")
            else:
                print("object doesnot exists")
                return redirect("showAttendenceForTeachers")
    return render(request,"AttendenceForTeachers.html")
def ShowUserCourses(request):
    courses=Course.objects.all()
    return render(request,"CourseForUser.html",{"courses":courses})
def showUserSingleCourse(request,id):
    course=Course.objects.filter(id=id)
    return render(request,"CourseForUserSingles.html",{"courses":course})
def WhyChooseUs(request):
    form=WhyCooseUsForm()
    if request.method=="POST":
        form=WhyCooseUsForm(request.POST)
        if form.is_valid():
            reason=form.cleaned_data["reason"]
            WhychooseUsModel.objects.create(
                reason=reason
            )
            return redirect("showWhyChooseUsForAdmin")
    return render(request,"WhyChooseUsForm.html",{"form":form})
def showWhyChooseUs(request):
    Model=WhychooseUsModel.objects.all()
    return render(request,"showWhyChooseUs.html",{"model":Model})
def showWhyChooseUsForAdmin(request):
    Model=WhychooseUsModel.objects.all()
    return render(request,"WhyChooseUsForAdmin.html",{"model":Model})
def EditReason(request,id):
    model=WhychooseUsModel.objects.get(id=id)
    if request.method=="POST":
        forms=WhyCooseUsForm(request.POST,request.FILES,instance=model)
        if forms.is_valid():
            forms.save()
            return redirect("showWhyChooseUsForAdmin")
    else:
        forms=WhyCooseUsForm(instance=model)
    return render(request,"EditReasons.html",{"forms":forms,"id":id})
def ContactInfo(request):
    contact=ContactInfoForm()
    if request.method=="POST":
        contact=ContactInfoForm(request.POST)
        if contact.is_valid():
            AcademyAddress=contact.cleaned_data["AcademyAddress"]
            phone_Number=contact.cleaned_data["phone_Number"]
            Email=contact.cleaned_data["Email"]
            OpeningHours=contact.cleaned_data['OpeningHours']
            CantactInfoModel.objects.create(
                AcademyAddress=AcademyAddress,
                phone_Number=phone_Number,
                Email=Email,
                OpeningHours=OpeningHours
            )
            print("object created")
            return redirect("ShowContactInfoForAdmin")
    return render(request,"ContactInfoForms.html",{"contact":contact})
def ShowContactInfo(request):
    contacts=CantactInfoModel.objects.all()
    return render(request,"showContactInfo.html",{"contacts":contacts})
def ShowContactInfoForAdmin(request):
    contacts=CantactInfoModel.objects.all()
    return render(request,"ContactInfoForAdmin.html",{"contacts":contacts})
def EditContactInfo(request,id):
    contact=CantactInfoModel.objects.get(id=id)
    if request.method=="POST":
        con=ContactInfoForm(request.POST,request.FILES,instance=contact)
        if con.is_valid():
            con.save()
            return redirect("ShowContactInfoForAdmin")
    else:
        con=ContactInfoForm(instance=contact)
    return render(request,"EditContactInfo.html",{"con":con,"id":id})
def Addmission(request):
    add=AdmissionForm()
    if request.method=="POST":
        add=AdmissionForm(request.POST)
        if add.is_valid():
            StudentName=add.cleaned_data['Student_Name']
            DateOfBirth=add.cleaned_data['DateOfBirth']
            gender=add.cleaned_data['gender']
            PrevSchool=add.cleaned_data["PrevSchool"]
            PrevClass=add.cleaned_data['PrevClass']
            Address=add.cleaned_data["Address"]
            Parent_Guardian_Name=add.cleaned_data["Parent_Guardian_Name"]
            Relation_with_student=add.cleaned_data["Relation_with_student"]
            phone_number=add.cleaned_data["phone_number"]
            Email=add.cleaned_data["Email"]
            Course=add.cleaned_data['Course']
            Classs=add.cleaned_data['Class']
            AddmissionModel.objects.create(
                Student_Name=StudentName,
                DateOfBirth=DateOfBirth,
                gender=gender,
                PrevSchool=PrevSchool,
                PrevClass=PrevClass,
                Address=Address,
                Parent_Guardian_Name=Parent_Guardian_Name,
                Relation_with_student=Relation_with_student,
                phone_number=phone_number,
                Email=Email,
                Course=Course,
                Class=Classs
            )
            print("object admission created !!")
            return redirect("UserHomie")
    return render(request,"AdmissionForm.html",{"add":add})
@user_passes_test(is_admin)
def ShowAllRegisForadmin(request):
    add=AddmissionModel.objects.all()
    return render(request,"AllAddmissionForAdmin.html",{"adds":add})
@user_passes_test(is_admin)
def showRegisInfoForAdmin(request,status):
    add=AddmissionModel.objects.filter(status='Pending')
    return render(request,"ShowAddmissionForAdmin.html",{"adds":add})
@user_passes_test(is_admin)
def EditRegist(request,id):
    add=AddmissionModel.objects.get(id=id)
    if request.method=="POST":
        forms=AdmissionForm(request.POST,request.FILES,instance=add)
        if forms.is_valid():
            forms.save()
            return redirect("ShowAllRegisForadmin")
    else:
        forms=AdmissionForm(instance=add)
    return render(request,"EditRegis.html",{"forms":forms,"id":id})
def SubjectDataforUsers(request):
    sub=SubjectsModel.objects.all()
    return render(request,"SubDataForUsers.html",{"sub":sub})