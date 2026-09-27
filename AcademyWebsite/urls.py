"""
URL configuration for AcademyWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from academyproject.views import signIn,userauthentication,UserHomie,Admin,TeacherHome,home,studentForms,showStudentData,GetTeacherData,allTeacherData,showTeacherData,GetCourseData,showCourses,getClassesData,showClasses,getAttenDate,showSata,AdminAuthentication,AdminHome,showStudentsForAdmin,student,Teacher,ShowTeachersForAdmin,Courses,CourseForAdmin,Claas,showClassesDataForAdmin,attendence,AttendenceDataForUser,deleteAttendence,deleteStudents,deleteTeachers,DeleteCourse,deleteClass,StudEnrollment,getSubjectData,allsubjects,showTeachersData,TeacherDataForm,showTeacherCouurse,showTeachersClasses,SubjectInfoForTeacher,showAttendenceForTeachers,DeleteAttenForTeachers,showAllTeachersForUser,showTeachersForUsers,ShowUserCourses,WhyChooseUs,showWhyChooseUs,ContactInfo,ShowContactInfo,EditStudent,EditTeachers,editCourses,EditClasses,EditAttendence,getSubjects,EditSubjects,EditReason,EditContactInfo,showWhyChooseUsForAdmin,ShowContactInfoForAdmin,showAllEnStd,showallEnrollForAdmin,Addmission,ShowAllRegisForadmin,showRegisInfoForAdmin,EditRegist,SubjectDataforUsers,showUserSingleCourse,allStudents,DeleteEnrollment,showSataforAdmin,allStudentsforAdmin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signIn,name="signIn"),
    path('userauthentication/',userauthentication,name="userauthentication"),
    path('Admin/',Admin,name="Admin"),
    path('TeacherHome/',TeacherHome,name="TeacherHome"),
    path('home/',home,name="home"),
    path('studentForms/',studentForms,name="studentForms"),
    path('showStudentData/',showStudentData,name="showStudentData"),
    path('GetTeacherData/',GetTeacherData,name="GetTeacherData"),
    path('allTeacherData/',allTeacherData,name="allTeacherData"),
    path('showTeacherData/<int:id>/',showTeacherData,name="showTeacherData"),
    path('GetCourseData/',GetCourseData,name="GetCourseData"),
    path('showCourses/<int:id>/',showCourses,name="showCourses"),
    path('getClassesData/',getClassesData,name="getClassesData"),
    path('showClasses/<int:id>/',showClasses,name="showClasses"),
    path('getAttenDate/',getAttenDate,name="getAttenDate"),
    path('showSata/<int:id>/',showSata,name="showSata"),
    path('AdminAuthentication/',AdminAuthentication,name="AdminAuthentication"),
    path('AdminHome/',AdminHome,name="AdminHome"),
    path('showStudentsForAdmin/<int:id>/',showStudentsForAdmin,name="showStudentsForAdmin"),
    path('student/',student,name="student"),
    path('Teacher/',Teacher,name="Teacher"),
    path('ShowTeachersForAdmin/<int:id>/',ShowTeachersForAdmin,name="ShowTeachersForAdmin"),
    path('Courses/',Courses,name="Courses"),
    path('CourseForAdmin/<int:id>/',CourseForAdmin,name="CourseForAdmin"),
    path('Claas/',Claas,name="Claas"),
    path('showClassesDataForAdmin/<int:id>/',showClassesDataForAdmin,name="showClassesDataForAdmin"),
    path('attendence/',attendence,name="attendence"),
    path('AttendenceDataForUser/<int:id>/',AttendenceDataForUser,name="AttendenceDataForUser"),
    path('deleteAttendence/',deleteAttendence,name="deleteAttendence"),
    path('deleteStudents/',deleteStudents,name="deleteStudents"),
    path('deleteTeachers/',deleteTeachers,name="deleteTeachers"),
    path('DeleteCourse/',DeleteCourse,name="DeleteCourse"),
    path('deleteClass/',deleteClass,name="deleteClass"),
    path('StudEnrollment/',StudEnrollment,name="StudEnrollment"),
    path('getSubjectData/',getSubjectData,name="getSubjectData"),
    path('allsubjects/',allsubjects,name="allsubjects"),
    path('showTeachersData/',showTeachersData,name="showTeachersData"),
    path('TeacherDataForm/',TeacherDataForm,name="TeacherDataForm"),
    path('showTeacherCouurse/',showTeacherCouurse,name="showTeacherCouurse"),
    path('showTeachersClasses/',showTeachersClasses,name="showTeachersClasses"),
    path('SubjectInfoForTeacher/',SubjectInfoForTeacher,name="SubjectInfoForTeacher"),
    path('showAttendenceForTeachers/',showAttendenceForTeachers,name="showAttendenceForTeachers"),
    path('DeleteAttenForTeachers/',DeleteAttenForTeachers,name="DeleteAttenForTeachers"),
    path('UserHomie/',UserHomie,name="UserHomie"),
    path('showAllTeachersForUser/',showAllTeachersForUser,name="showAllTeachersForUser"),
    path('showTeachersForUsers/<int:id>/',showTeachersForUsers,name="showTeachersForUsers"),
    path('ShowUserCourses/',ShowUserCourses,name="ShowUserCourses"),
    path('WhyChooseUs/',WhyChooseUs,name="WhyChooseUs"),
    path('showWhyChooseUs',showWhyChooseUs,name="showWhyChooseUs"),
    path('ContactInfo/',ContactInfo,name="ContactInfo"),
    path('ShowContactInfo/',ShowContactInfo,name="ShowContactInfo"),
    path('EditStudent/<int:id>/',EditStudent,name="EditStudent"),
    path('EditTeachers/<int:id>/',EditTeachers,name="EditTeachers"),
    path('editCourses/<int:id>/',editCourses,name="editCourses"),
    path('EditClasses/<int:id>/',EditClasses,name="EditClasses"),
    path('EditAttendence/<int:id>/',EditAttendence,name="EditAttendence"),
    path('getSubjects/<int:id>/',getSubjects,name="getSubjects"),
    path('EditSubjects/<int:id>/',EditSubjects,name="EditSubjects"),
    path('EditReason/<int:id>/',EditReason,name="EditReason"),
    path('DeleteEnrollment/',DeleteEnrollment,name="DeleteEnrollment"),
    path('showSataforAdmin/<int:id>/',showSataforAdmin,name="showSataforAdmin"),
    path('allStudentsforAdmin/',allStudentsforAdmin,name="allStudentsforAdmin"),
    path('EditContactInfo/<int:id>/',EditContactInfo,name="EditContactInfo"),
    path('showWhyChooseUsForAdmin/',showWhyChooseUsForAdmin,name="showWhyChooseUsForAdmin"),
    path('ShowContactInfoForAdmin/',ShowContactInfoForAdmin,name="ShowContactInfoForAdmin"),
    path('showAllEnStd/',showAllEnStd,name="showAllEnStd"),
    path('showallEnrollForAdmin/<int:id>/',showallEnrollForAdmin,name="showallEnrollForAdmin"),
    path('Addmission/',Addmission,name='Addmission'),
    path('ShowAllRegisForadmin/',ShowAllRegisForadmin,name="ShowAllRegisForadmin"),
    path('showRegisInfoForAdmin/<str:status>/',showRegisInfoForAdmin,name='showRegisInfoForAdmin'),
    path('EditRegist/<int:id>/',EditRegist,name="EditRegist"),
    path('SubjectDataforUsers/',SubjectDataforUsers,name="SubjectDataforUsers"),
    path('showUserSingleCourse/<int:id>/',showUserSingleCourse,name="showUserSingleCourse"),
    path('allStudents/',allStudents,name="allStudents"),
]


