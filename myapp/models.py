import uuid

from django.contrib.auth.models import User
from django.db import models
class BaseModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    uid =models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
    created_at = models.DateField(auto_now=True)
    updated_at  = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class EmployeeTable(BaseModel):
    company_name =models.CharField(max_length=100)
    emp_fname = models.CharField(max_length=200)
    emp_lname = models.CharField(max_length=50)
    emp_DOB = models.DateField()
    emp_phone = models.IntegerField()
    emp_id = models.IntegerField()
    emp_email = models.EmailField()
    aboutUS = models.TextField()
    is_done = models.BooleanField(default=True)


    def __str__(self):
        return self.emp_fname

class TimingCreateTable(BaseModel):
    EmployeeTable = models.ForeignKey(EmployeeTable,on_delete=models.CASCADE)
    timing = models.DateField()
