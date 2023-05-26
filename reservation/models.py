from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=100)
    client_phone = models.CharField(max_length=100)
    client_address = models.CharField(max_length=100)
    client_country = models.CharField(max_length=100)
    client_city = models.CharField(max_length=100)
    client_zip = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'client'
        
    def __str__(self):
        return self.client_name

class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=100)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_status = models.CharField(max_length=100)
    room_image = models.ImageField(upload_to='pics')
    room_description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'room'
        
    def __str__(self):
        return f"Room {self.room_number}"
