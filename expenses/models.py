from django.db import models 

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title