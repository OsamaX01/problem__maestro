from django.db import models

from users.models import CustomUser

# Create your models here.
class Problem(models.Model):
    instructor =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="my_problems", limit_choices_to={'role': 'instructor'})
    name = models.CharField(max_length=32)
    statement = models.TextField()
    input_section = models.TextField()
    output_section = models.TextField()
    correct_answer = models.TextField(default=None)

    def __str__(self):
        return f"{self.name} problem"

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE,  related_name="testcases")
    number = models.IntegerField()
    data = models.TextField()
    is_visable = models.BooleanField()
    answer = models.TextField(default='default answer')

    def __str__(self):
        return f"{self.problem.name} Test case {self.number}"
    
    def save(self, *args, **kwargs):
        if not self.number:
            # Get the maximum number of test cases for this problem
            max_number = TestCase.objects.filter(problem=self.problem).aggregate(models.Max('number'))['number__max']
            if max_number is not None:
                self.number = max_number + 1
            else:
                self.number = 1
        super().save(*args, **kwargs)
