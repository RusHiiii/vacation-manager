from django.db import models

class Month(models.TextChoices):
    JAN = '1', 'Janvier'
    FEB = '2', 'Février'
    MAR = '3', 'Mars'
    APR = '4', 'Avril'
    MAY = '5', 'Mai'
    JUN = '6', 'Juin'
    JUL = '7', 'Juillet'
    AUG = '8', 'Août'
    SEP = '9', 'Septembre'
    OCT = '10', 'Octobre'
    NOV = '11', 'Novembre'
    DEC = '12', 'Décembre'