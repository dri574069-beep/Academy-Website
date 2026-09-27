from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class registeration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=200)
    role=models.CharField(max_length=200,null=True)
    DateofBirth=models.DateField()
    age=models.IntegerField()
    def __str__(self):
        return self.user
class UserLogin(models.Model):
    userName=models.CharField(max_length=200)
    password=models.CharField(max_length=500)
class StudentAcc(models.Model):
    studentUser=models.OneToOneField(User,on_delete=models.CASCADE)
    studentName=models.CharField(max_length=200)
    dateOfBirth=models.DateField()
    gender=models.CharField(max_length=200)
    ParentphoneNum=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    parentOrGuardianName=models.CharField(max_length=200)
    AdsmissionDate=models.DateField()
    status=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="studentPro/",null=True,blank=True)
    def __str__(self):
        return self.studentName
class TeacherAcc(models.Model):
    TeacherUser=models.ForeignKey(User,on_delete=models.CASCADE)
    Teacher_name=models.CharField(max_length=200)
    phoneNumber=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    joining_date=models.DateField()
    profile_pic=models.ImageField(upload_to="teacher_prof/",null=True,blank=True)
    status=models.CharField(max_length=200)
    def __str__(self):
        return self.Teacher_name
class Course(models.Model):
    CourseName=models.CharField(max_length=200)
    description=models.TextField()
    duration=models.CharField()
    fee=models.CharField(max_length=300)
    CourseTeacher=models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=200)
    def __str__(self):
        return self.CourseName
class Classes(models.Model):
    className=models.CharField(max_length=200)
    Teacher=models.ForeignKey(TeacherAcc,on_delete=models.SET_NULL,null=True)   #make a dropdown of teachers
    days=models.CharField(max_length=300)
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.CharField(max_length=200)
    capacity=models.CharField(max_length=200)
    def __str__(self):
        return self.className
class Attendence(models.Model):
    student=models.ForeignKey(StudentAcc,on_delete=models.CASCADE)
    isPresent=models.CharField(max_length=200)
    courseOrClass=models.CharField(max_length=200)
    date=models.DateField()
    status=models.CharField(max_length=200)
    Teacher=models.ForeignKey(TeacherAcc,on_delete=models.CASCADE)
    def __str__(self):
        return self.student
class SubjectsModel(models.Model): 
    name=models.CharField(max_length=200)
    description=models.TextField(null=True)
    level=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=200,null=True)
    Teacher=models.ForeignKey(TeacherAcc,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class WhychooseUsModel(models.Model):
    reason=models.CharField(max_length=200)
    def __str__(self):
        return self.reason
class CantactInfoModel(models.Model):
    AcademyAddress=models.CharField(max_length=200)
    phone_Number=models.CharField(max_length=200)
    Email=models.EmailField()
    OpeningHours=models.CharField(max_length=200)
    def __str__(self):
        return self.AcademyAddress
class AddmissionModel(models.Model):
    Student_Name=models.CharField(max_length=200)
    DateOfBirth=models.DateField()
    gender=models.CharField(max_length=200)
    PrevSchool=models.CharField(max_length=200)
    PrevClass=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Parent_Guardian_Name=models.CharField(max_length=200)
    Relation_with_student=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    Email=models.EmailField()
    Course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    Class=models.ForeignKey(Classes,on_delete=models.CASCADE,blank=True,null=True)
    Registeration_Date=models.DateField(auto_now_add=True)
    status=models.CharField(default='Pending')
    def __str__(self):
        return self.StName
class Enrollment(models.Model):
    student=models.CharField(max_length=200)
    course=models.ManyToManyField("Course",blank=True)
    classs=models.ForeignKey("Classes",on_delete=models.CASCADE,blank=True,null=True)
    subjects=models.ManyToManyField("SubjectsModel",blank=True)
    gender=models.CharField(max_length=200)
    DateOfBirth=models.DateField()
    PrevSchool=models.CharField(max_length=200)
    PrevClass=models.CharField(max_length=200)
    Address=models.CharField(max_length=200,null=True)
    Parent_Guardian_Name=models.CharField(max_length=200)
    Relation_with_student=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    Email=models.EmailField()
    Registeration_Date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.student)