from django.contrib import admin
from IPA.models import price_prediction

# Register your models here.

class IPA_Admin(admin.ModelAdmin):
    list_display= (
        'id','LotArea','MSZoning','BldgType','ExterQual','OverallQual','GarageType','CentralAir','Heating','predicted_price'
    )
    
    list_display_links=(
        'id','LotArea','MSZoning','BldgType','ExterQual','OverallQual','GarageType','CentralAir','Heating','predicted_price'
    )
  

admin.site.register(price_prediction, IPA_Admin)