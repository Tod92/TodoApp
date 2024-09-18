from django.db import models

TODO = "TODO"
DOING = "DOING"
DONE = "DONE"

STATUS_CHOICES = (
    (TODO, "To do"),
    (DOING, "In progress"),
    (DONE, "Done")
)
# Create your models here.

class Task(models.Model):
    title : str = models.CharField(max_length=100)
    description : str | None = models.CharField(max_length=500, blank=True)
    status : str = models.CharField(max_length=9,
                                    choices=STATUS_CHOICES,
                                    default=TODO)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title