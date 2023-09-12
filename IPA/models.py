from django.db import models

# Create your models here.

class price_prediction(models.Model):
    LotArea = models.FloatField()
    MSZoning = models.CharField(max_length=255)
    BldgType = models.CharField(max_length=255)
    ExterQual = models.CharField(max_length=255)
    OverallQual = models.CharField(max_length=255)
    GarageType = models.CharField(max_length=255)
    CentralAir = models.CharField(max_length=255)
    Heating = models.CharField(max_length=255)
    predicted_price = models.FloatField()
    
def __str__(self):
        return f"Prediction for LotArea: {self.LotArea}, ExterQual: {self.ExterQual}, Predicted Price: {self.predicted_price}"