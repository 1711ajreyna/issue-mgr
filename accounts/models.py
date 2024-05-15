from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    
    #def save(self, **kwargs):
        #if not self.role_id:
            #default_role_id = 1
            #self.role_id = default_role_id

        #if not self.team_id:
            #default_team_id = 1
            #self.team_id = default_team_id

        #super().save(**kwargs)