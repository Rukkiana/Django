from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank = True, null = True)
    created_by = models.ForeignKey(User,related_name = 'created_task',on_delete = models.SET_NULL,null=True,blank = True)
    assign_to = models.ForeignKey(User,related_name = 'assign_task',on_delete = models.SET_NULL,null=True,blank = True)

    # class Meta:
    #     permissions = [("can_edit_task", "Can edit task"),
    #                    ("can_delete_task", "Can delete task")]
  



    def __str__(self):
        return self.title

