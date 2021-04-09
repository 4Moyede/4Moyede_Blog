from djongo import models


class Introduce(models.Model):
    objects = models.DjongoManager()

    id = models.ObjectIdField(db_column='_id', primary_key=True)
    profile = models.TextField(default=" ", blank=True, null=True)
    detail = models.TextField(default=" ", blank=True, null=True)


class Projects(models.Model):
    objects = models.DjongoManager()

    id = models.ObjectIdField(db_column='_id', primary_key=True)
    url = models.TextField(default="https://github.com/4Moyede/", blank=True, null=True)
    name = models.TextField(default=" ", blank=True, null=True)
    thumbnail = models.TextField(default="loading.png", blank=True, null=True)
    detail = models.TextField(default=" ", blank=True, null=True)
    techStack = models.TextField(default=" ", blank=True, null=True)

    def __str__(self):
        return self.name


class TechStack(models.Model):
    objects = models.DjongoManager()

    id = models.ObjectIdField(db_column='_id', primary_key=True)
    tech = models.TextField(default=" ", blank=True, null=True)
    skill = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.tech
