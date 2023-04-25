from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id}) {self.name}"

class Detail(models.Model):
    master = models.ForeignKey(Master, related_name='details', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.master.name}: {self.description}'

