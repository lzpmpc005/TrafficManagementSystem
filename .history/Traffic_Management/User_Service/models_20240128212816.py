from django.db import models

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(max_length=20)

    def __str__(self):
        return f"Driver ID: {self.id}, Driver Name: {self.name}"

class Vehicle(models.Model):
    numberPlate = models.CharField(max_length=20, primary_key=True)
    ownerID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicleType = models.CharField(max_length=50)

    def __str__(self):
        return self.numberPlate
    
class Plate(models.Model):
    numberPlate = models.OneToOneField(Vehicle, primary_key=True, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    postal_area = models.CharField(max_length=100)
    age_identifier = models.JSONField()
    random_letters = models.CharField(max_length=3)

    def __str__(self):
        return self.numberPlate.numberPlate

class JunctionsLog(models.Model):
    logID = models.AutoField(primary_key=True)
    numberPlate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    location = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Log ID: {self.logID}, Plate: {self.numberPlate}"
