from django.db import models


class Reason(models.Model):

    text = models.TextField()
    order = models.IntegerField()

class Course(models.Model):

    access_conditions = models.TextField()  # accessContidions
    career_opportunities = models.TextField()  # careerOportunities
    competences = models.TextField()  # competences
    direction_contact = models.CharField(max_length=200)  # directionContact
    direction_email = models.EmailField()  # directionEmail
    course_ects = models.IntegerField()  # courseECTS
    course_name = models.CharField(max_length=200)  # courseName
    course_secretariat_contact = models.CharField(max_length=200)  # courseSecretariatContact
    course_secretariat_email = models.EmailField()  # courseSecretariatEmail
    future_studies = models.TextField()  # futureStudies
    infrastructure = models.TextField()  # infrastructure
    objectives = models.TextField()  # objectives
    presentation = models.TextField()  # presentation
    scientific_area = models.CharField(max_length=200)  # scientificArea
    semesters = models.IntegerField()  # semesters
    recipients = models.TextField()  # recipients
    guest_teachers = models.TextField()  # guestTeachers

    def __str__(self):
        return f'{self.course_name}'

class Subject(models.Model):

    name = models.CharField(max_length=40)
    year = models.IntegerField()
    semester = models.CharField(max_length=2)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=20)
    scientific_area = models.ForeignKey('Scientific_area', on_delete = models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='curso/images', null=True, blank=True)
    resume = models.TextField()
    subject = models.ManyToManyField(Subject)


class Flat_plan(models.Model):

    subjects = models.ManyToManyField(Subject)
    years = models.IntegerField()


class Scientific_area(models.Model):

    teachers = models.ManyToManyField(Teacher)
    program = models.TextField()
    objectives = models.TextField()
    description = models.TextField()


class Programming_Language(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):

    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='curso/images', null=True, blank=True)
    video = models.URLField(max_length=200,default='')
    concepts = models.TextField()
    technologies = models.TextField()
    programming_languages = models.ManyToManyField(Programming_Language)
    repository = models.URLField(max_length=200,default='')

    def __str__(self):
        return f'{self.title}'


