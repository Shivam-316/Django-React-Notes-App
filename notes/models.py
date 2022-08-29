from django.db import models
from users.models import Author
import datetime

PRIORITY = [
    (1, 'Low'),
    (50, 'Medium'),
    (100, 'High'),
]

def getTitleDefault():
    return f'Note of {datetime.date.today().strftime("%w %b, %Y")}'

# Create your models here.
class Note(models.Model):
    class NotePriority(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 50, 'Medium'
        HIGH = 100, 'High'
        __empty__ = 'None'

    author = models.ForeignKey(to = Author, on_delete = models.CASCADE, related_name='notes')
    title = models.CharField(max_length=36, blank = True, default = getTitleDefault)
    body = models.TextField(blank=True)
    priority = models.IntegerField(choices = NotePriority.choices, blank=True, null=True)
    created_on = models.DateField(auto_now_add = True)
    updated_on = models.DateField(auto_now = True)

        
    def __str__(self) -> str:
        return self.title