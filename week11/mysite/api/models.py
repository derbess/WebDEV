from django.db import models

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}: {}'.format(self.id,self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField()
    due_on = models.DateField()
    status = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name,self.created_at,self.due_on,self.status,self.task_list)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at,
            'due_on': self.due_on
            # 'task_list': self.task_list.to_json()
        }
