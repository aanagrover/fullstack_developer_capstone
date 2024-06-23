# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

# class CarModel(models.Model):
#     car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  
# Many-to-One relationship
#     name = models.CharField(max_length=100)
#     CAR_TYPES = [
#         ('SEDAN', 'Sedan'),
#         ('SUV', 'SUV'),
#         ('WAGON', 'Wagon'),
#         # Add more choices as required
#     ]
#     type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
#     year = models.IntegerField(default=2023,
#         validators=[
#             MaxValueValidator(2023),
#             MinValueValidator(2015)
#         ])
#     # Other fields as needed

#     def __str__(self):
#         return self.name  # Return the name as the string representation

# --- Refering other code for carModel
class CarModel(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=2)
    type = models.CharField(max_length=10)
    year = models.DateField(null=True)
    carmakes = models.ManyToManyField(CarMake)

    def __str__(self):
        return self.name


class CarDealer:
    def __init__(self, address, city, full_name, id,
                 lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase,
    review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # Dealership
        self.dealership = dealership
        # Dealer name
        self.name = name
        # Dealer purchase
        self.purchase = purchase
        # Dealer review
        self.review = review
        # purchase_date
        self.purchase_date = purchase_date
        # car_make
        self.car_make = car_make
        # car_model
        self.car_model = car_model
        # car_year
        self.car_year = car_year
        # sentiment
        self.sentiment = sentiment
        # id
        self.id = id

    def __str__(self):
        return "Dealer name: " + self.full_name
