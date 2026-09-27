from django import forms
from .models import TeacherAcc,StudentAcc,Enrollment,SubjectsModel,registeration,Attendence,WhychooseUsModel,CantactInfoModel,Course,Classes,AddmissionModel
# create your forms here

class DeleteEnroll(forms.Form):
    enId=forms.IntegerField()
class deleteAttenforTeacher(forms.Form):
    atTIf=forms.IntegerField(widget=forms.NumberInput)
class deletestudents(forms.Form):
    stId=forms.IntegerField(widget=forms.NumberInput)
class DeleteCourses(forms.Form):
    CId=forms.IntegerField(widget=forms.NumberInput)
class deleteclass(forms.Form):
    ClId=forms.IntegerField(widget=forms.NumberInput)
class deleteTeacher(forms.Form):
    TId=forms.IntegerField(widget=forms.NumberInput)
class deleteAttends(forms.Form):
    attId=forms.IntegerField(widget=forms.NumberInput)
class AdminLogin(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
class UserRegis(forms.ModelForm):
    class Meta:
        model=registeration
        fields=['Name','age']
    DateofBirth=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(widget=forms.EmailInput)
    role=forms.ChoiceField(choices=[('Teacher','Teacher'),('Admin','Admin'),('User','User'),('Student','Student')])
class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput)
class StudentAccForm(forms.ModelForm):
    class Meta:
        model=StudentAcc
        fields=['studentName','gender','ParentphoneNum','address','parentOrGuardianName','status']
    dateOfBirth=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    AdsmissionDate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
class TeacherForms(forms.ModelForm):
    class Meta:
        model = TeacherAcc
        fields = [
            'Teacher_name',
            'phoneNumber',
            'qualification',
            'specialization',
            'status'
        ]
    joining_date=forms.DateField(widget=forms.DateInput(attrs={"type":'date'})) 
class CourseForms(forms.ModelForm):
    class Meta:
        model=Course
        fields=['CourseName','description','duration','fee','CourseTeacher','level','status']
    start_date=forms.DateField(widget=forms.DateInput(attrs={"type":'date'})) 
    end_date=forms.DateField(widget=forms.DateInput(attrs={"type":'date'})) 
class ClassesForm(forms.ModelForm):
    class Meta:
        model=Classes
        fields=['className','Teacher','days','room','capacity']
    start_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":'time'})) 
    end_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":'time'})) 
class AttendenceForms(forms.ModelForm):
    class Meta:
        model=Attendence
        fields=['Teacher','student','isPresent','courseOrClass','status']
    date=forms.DateField(widget=forms.DateInput(attrs={"type":'date'})) 
class subjectForms(forms.ModelForm):
    class Meta:
        model=SubjectsModel
        fields=['name','description','level','status','Teacher']
class WhyCooseUsForm(forms.ModelForm):
    class Meta:
        model=WhychooseUsModel
        fields=['reason']
class ContactInfoForm(forms.ModelForm):
    class Meta:
        model=CantactInfoModel
        fields=['AcademyAddress','phone_Number','Email','OpeningHours']
class AdmissionForm(forms.ModelForm):
    class Meta:
        model=AddmissionModel
        fields=['Student_Name','gender','PrevSchool','PrevClass','Address','Parent_Guardian_Name','Relation_with_student','phone_number','Email','Course','Class']
    DateOfBirth=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
class EnrollForms(forms.ModelForm):
    class Meta:
        model=Enrollment
        fields=['student','course','classs','subjects','gender','PrevSchool','PrevClass','Address','Parent_Guardian_Name','Relation_with_student','phone_number','Email']
        widgets={
            'course':forms.CheckboxSelectMultiple(),
            'subjects':forms.CheckboxSelectMultiple(),
        }
    DateOfBirth=forms.DateField(widget=forms.DateInput(attrs={"type":'date'})) 