from django.db import models

class Cases(models.Model):
    District = models.CharField(max_length=30)
    Town = models.CharField(max_length=50)
    Date = models.DateTimeField()
    Count = models.IntegerField()
    
    class Meta:
        db_table = 'goa_covid_sheet'
        managed = False
        
    #def __str__(self):
    #    return '{self.District} :: {self.Town} :: {self.Date} :: {self.Count}'

