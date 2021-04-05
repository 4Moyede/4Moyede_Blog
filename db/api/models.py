from djongo import models


class Introduce(models.Model):
    objects = models.DjongoManager()

    id = models.ObjectIdField(db_column='_id', primary_key=True)
    detail = models.TextField()


class Projects(models.Model):
    objects = models.DjongoManager()

    id = models.ObjectIdField(db_column='_id', primary_key=True)
    url = models.TextField()
    name = models.TextField()
    thumbnail = models.TextField()
    detail = models.TextField()
    techStack = models.TextField()


class TechStack(models.Model):
    objects = models.DjongoManager()

    id = models.ObjectIdField(db_column='_id', primary_key=True)
    tech = models.TextField()
    skill = models.IntegerField()
