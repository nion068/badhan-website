from django.db import models

class Hall(models.Model):
    hall_name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.hall_name

class BloodGroup(models.Model):
    blood_group = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.blood_group

class Department(models.Model):
    dept = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.dept

class Donor(models.Model):
    name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=2)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    room = models.CharField(max_length=10)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)
    last_donation = models.DateField()
    count = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.dept + self.batch + ' ' + self.blood_group
    

    