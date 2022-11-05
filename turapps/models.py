from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email} {self.fam} {self.name} {self.otc} {self.phone}'

class Coords(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'

class Level(models.Model):
    winter = models.CharField(max_length=255)
    summer = models.CharField(max_length=255)
    autumn = models.CharField(max_length=255)
    spring = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

class Images(models.Model):
    data = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.data} {self.title}'


class pereval_added(models.Model):
    new = 'Добавлено'# добавлено на проверку;
    pending = 'Рассматривается'# — если модератор взял в работу;
    accepted = 'Принято'# — модерация прошла успешно;
    rejected = 'Отклонено' # — модерация прошла, информация не принята.
    VERIFICATION_STATUS = [
        (new, 'Добавлено'),
        (pending, 'Рассматривается'),
        (accepted, 'Принято'),
        (rejected, 'Отклонено'),
    ]
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField()
    status = models.CharField(max_length=255,choices=VERIFICATION_STATUS, default=new)
    user = models.ForeignKey(Users,related_name='per_user', on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords,related_name='per_coords', on_delete=models.CASCADE)
    level = models.ForeignKey(Level,related_name='per_level', on_delete=models.CASCADE)
    images = models.ManyToManyField(Images, through='PerevalImages')


    # В этой модели будут связаны id места на перевале и id сделанных на нём снимков
class PerevalImages(models.Model):
    pereval = models.ForeignKey(pereval_added, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pereval} {self.images}'
