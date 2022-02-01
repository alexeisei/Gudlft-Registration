from locust import HttpUser, task, between
from server import loadClubs, loadCompetitions

class HelloWorldUser(HttpUser):
    
    wait_time = between(1, 2)
    competitions = loadCompetitions()[0]['name']
    club = loadClubs()[0]["name"]
    email = loadClubs()[0]["email"] 
    
    
    @task
    def index(self):
    
    
    @task
    def connexion(self):
        
   
    
    @task
    def purchase_places(self):
        


    @task
    def get_place(self):
        

    
    @task
    def logout(self):

