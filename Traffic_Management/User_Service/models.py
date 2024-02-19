from django.db import models

class Plate(models.Model):
    numberPlate = models.CharField(primary_key=True, max_length=20)
    region = models.CharField(max_length=100)
    postal_area = models.CharField(max_length=100)
    age_identifier = models.JSONField()
    random_letters = models.CharField(max_length=3)

    def __str__(self):
        return self.numberPlate

class Driver(models.Model):
    driverID = models.AutoField(primary_key=True)
    driverName = models.CharField(max_length=100)
    driverEmail = models.EmailField(max_length=254)
    driverPhone = models.BigIntegerField()

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
    numberPlate = models.CharField(max_length=20)
    dateTime = models.DateTimeField()
    period = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    speed = models.IntegerField(default=0)
    hitSuspicion = models.BooleanField(default=False)
    redlightSuspicion = models.BooleanField(default=False)
    beltStatus = models.BooleanField(default=False)
    phoneStatus = models.BooleanField(default=False)
    registerStatus = models.BooleanField(default=False)

    def __str__(self):
        return f"Log ID: {self.logID}, Plate: {self.numberPlate}"

class Violation(models.Model):
    logID = models.AutoField(primary_key=True)
    violationType = models.CharField(max_length=255)
    fineAmount = models.IntegerField(default=0)

    def __str__(self):
        return f"Log ID: {self.logID}, Violation Type: {self.violationType}, Fine Amount: {self.fineAmount}"


class ViolationLog(models.Model):
    logID = models.AutoField(primary_key=True)
    numberPlate = models.CharField(max_length=255)
    dateTime = models.DateTimeField()
    location = models.CharField(max_length=255)
    violationType = models.ForeignKey(Violation, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return f"Log ID: {self.logID}, Plate: {self.numberPlate}, Date Time: {self.dateTime}, Location: {self.location}, Violation Type: {self.violationType}"

class FineLog(models.Model):
    logID = models.AutoField(primary_key=True)
    numberPlate = models.CharField(max_length=255)
    driverID = models.BigIntegerField()
    driverName = models.CharField(max_length=255)
    dateTime = models.DateTimeField()
    location = models.CharField(max_length=255)
    violationType = models.ForeignKey(Violation, on_delete=models.SET_DEFAULT, default=None)
    fineAmount = models.IntegerField(default=0)
    closedStatus = models.BooleanField()
    
    def __str__(self):
        return f"Log ID: {self.logID}, Plate: {self.numberPlate}, Driver ID: {self.driverID}, Driver Name: {self.driverName}, Date Time: {self.dateTime}, Location: {self.location}, Violation Type: {self.violationType}, Fine Amount: {self.fineAmount}, Closed Status: {self.closedStatus}"
    
class EmailLog(models.Model):
    logID = models.AutoField(primary_key=True)
    driverEmail = models.EmailField(max_length=255)
    fineLogID = models.ForeignKey(FineLog, on_delete=models.SET_DEFAULT, default=None)
    dateTime = models.CharField(max_length=255)
    sentStatus = models.BooleanField()
    
    def __str__(self):
        return f"Log ID: {self.logID}, Driver Email: {self.driverEmail}, Fine Log ID: {self.fineLogID}, Date Time: {self.dateTime}, Sent Status: {self.sentStatus}"
    
class Junction(models.Model):
    junctionID = models.AutoField(primary_key=True)
    junctionName = models.CharField(max_length=255)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)

    def __str__(self):
        return f"Junction ID: {self.junctionID}, Junction Name: {self.junctionName}"