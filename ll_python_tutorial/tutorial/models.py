from django.db import models



class Chapter(models.Model):
    name = models.CharField(max_length=500, default="")
    displayName = models.CharField(max_length=500, default="")
    content = models.TextField(default="")

    def __str__(self):
        return "name: " + self.name + " " + "displayName:" + self.displayName



class Exercise(models.Model):
    title = models.CharField(max_length=500,default="")
    description = models.CharField(default="",max_length=1000)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "title: " + self.title + "\n" + "description: +\n" + self.description+ "\n" +str(self.chapter)





