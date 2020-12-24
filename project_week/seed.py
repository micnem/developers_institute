import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1_game.settings')
django.setup()

from trading_post.models import Driver, Team, Card


drivers_list = [{"position":1,"points":347,"driver_id":21838,"driver_name":"Lewis Hamilton","team_id":29331,"team_name":"Mercedes","nationality":"Great Britain","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":2,"points":223,"driver_id":92948,"driver_name":"Valtteri Bottas","team_id":29331,"team_name":"Mercedes","nationality":"Finland","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":3,"points":214,"driver_id":87445,"driver_name":"Max Verstappen","team_id":16549,"team_name":"Red Bull","nationality":"Belgium","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":4,"points":125,"driver_id":26087,"driver_name":"Sergio Perez","team_id":32644,"team_name":"Racing Point","nationality":"Mexico","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":5,"points":119,"driver_id":58339,"driver_name":"Daniel Ricciardo","team_id":15591,"team_name":"Renault","nationality":"Australia","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":6,"points":105,"driver_id":87222,"driver_name":"Carlos Sainz","team_id":28251,"team_name":"McLaren","nationality":"Spain","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":7,"points":105,"driver_id":357903,"driver_name":"Alex Albon","team_id":16549,"team_name":"Red Bull","nationality":"Thailand","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":8,"points":98,"driver_id":328938,"driver_name":"Charles Leclerc","team_id":91587,"team_name":"Ferrari","nationality":"Monaco","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":9,"points":97,"driver_id":539806,"driver_name":"Lando Norris","team_id":28251,"team_name":"McLaren","nationality":"Great Britain","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":10,"points":75,"driver_id":991967,"driver_name":"Pierre Gasly","team_id":99735,"team_name":"AlphaTauri","nationality":"France","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":11,"points":75,"driver_id":754025,"driver_name":"Lance Stroll","team_id":32644,"team_name":"Racing Point","nationality":"Canada","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":12,"points":62,"driver_id":102533,"driver_name":"Esteban Ocon","team_id":15591,"team_name":"Renault","nationality":"France","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":13,"points":33,"driver_id":31997,"driver_name":"Sebastian Vettel","team_id":91587,"team_name":"Ferrari","nationality":"Germany","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":14,"points":32,"driver_id":15286,"driver_name":"Daniil Kvyat","team_id":99735,"team_name":"AlphaTauri","nationality":"Russia","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":15,"points":10,"driver_id":86250,"driver_name":"Nico Hulkenberg","team_id":32644,"team_name":"Racing Point","nationality":"Germany","is_reserve":1,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":16,"points":4,"driver_id":64723,"driver_name":"Kimi Raikkonen","team_id":35780,"team_name":"Alfa Romeo Racing","nationality":"Finland","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":17,"points":4,"driver_id":351420,"driver_name":"Antonio Giovinazzi","team_id":35780,"team_name":"Alfa Romeo Racing","nationality":"Italy","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":18,"points":3,"driver_id":764647,"driver_name":"George Russell","team_id":81807,"team_name":"Williams","nationality":"United Kingdom","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":19,"points":2,"driver_id":69101,"driver_name":"Romain Grosjean","team_id":71781,"team_name":"Haas","nationality":"France","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":20,"points":1,"driver_id":12420,"driver_name":"Kevin Magnussen","team_id":71781,"team_name":"Haas","nationality":"Denmark","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":21,"points":0,"driver_id":547297,"driver_name":"Nicholas Latifi","team_id":81807,"team_name":"Williams","nationality":"Canada","is_reserve":0,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":22,"points":0,"driver_id":777590,"driver_name":"Jack Aitken","team_id":81807,"team_name":"Williams","nationality":"Great Britain","is_reserve":1,"updated":"2020-12-21T03:00:02+00:00","season":2020},{"position":23,"points":0,"driver_id":841446,"driver_name":"Pietro Fittipaldi","team_id":71781,"team_name":"Haas","nationality":"Brazil","is_reserve":1,"updated":"2020-12-21T03:00:02+00:00","season":2020}]


def seed_drivers(drivers_list):
    for driver in drivers_list:

        team, created = Team.objects.get_or_create(name=driver['team_name'])

        Driver.objects.get_or_create(name=driver['driver_name'], nationality=driver['nationality'], team=team, position=driver['position'], points=driver['points'])
    return


def add_ids(drivers_list):
    for driver in drivers_list:

        team, created = Team.objects.get_or_create(name=driver['team_name'])

        current_driver, created = Driver.objects.get_or_create(name=driver['driver_name'], nationality=driver['nationality'], team=team)

        team.f1_id = driver["team_id"]
        current_driver.f1_id = driver["driver_id"]

        team.save()
        current_driver.save()


