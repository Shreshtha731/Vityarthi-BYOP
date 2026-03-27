from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CareerPath(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skill, related_name='careers')

    def __str__(self):
        return self.title

class ProjectIdea(models.Model):
    title = models.CharField(max_length=200)
    problem_statement = models.TextField()
    associated_career = models.ForeignKey(CareerPath, on_delete=models.CASCADE)
    recommended_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title