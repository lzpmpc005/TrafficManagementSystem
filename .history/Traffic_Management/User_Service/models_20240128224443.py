from django.db import models

class Plate(models.Model):
    numberPlate = models.CharField(primary_key=True)
    region = models.CharField(max_length=100)
    postal_area = models.CharField(max_length=100)
    age_identifier = models.JSONField()
    random_letters = models.CharField(max_length=3)

    def __str__(self):
        return self.numberPlate.numberPlate

class Driver(models.Model):
    driverID = models.AutoField(primary_key=True)
    driverName = models.CharField(max_length=100)
    driverEmail = models.EmailField(max_length=254)
    driverPhone = models.PositiveIntegerField()

    def __str__(self):
        return f"Driver ID: {self.driverID}, Driver Name: {self.driverName}"

class Vehicle(models.Model):
    numberPlate = models.OneToOneField(Plate, primary_key=True, on_delete=models.CASCADE)
    ownerID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicleType = models.CharField(max_length=50)

    def __str__(self):
        return self.numberPlate
    

class JunctionsLog(models.Model):
    logID = models.AutoField(primary_key=True)
    numberPlate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    location = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Log ID: {self.logID}, Plate: {self.numberPlate}"
