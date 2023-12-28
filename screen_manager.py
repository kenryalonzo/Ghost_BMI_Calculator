from kivy.uix.screenmanager import ScreenManager
from package.Data import Data
from package.User import User
from package.session import Session


class MyScreenManager(ScreenManager):
    def get_gender(self, sex):
        if sex == "Homme":
            return 0
        elif sex == "Femme":
            return 1
        
        
    def check_credentials(self, pseudo:str, password:str):
        print(f"{pseudo} : {password}")
        get_user = Data.get_user(pseudo, password)
        print(get_user)
        if get_user['status']:
            self.current = "index"
            Session.make_session(get_user)
            return
        Session.clear_session()
            
            
    def check_signup(self, username, password:str, password_repeat:str, nameAndSurname, age, sex, taille, poids, travail):
        
        if password != "" and password == password_repeat:
            user = User(username, password, nameAndSurname, int(age), self.get_gender(sex), int(taille)/100, int(poids), travail)
            data = Data(user)
            data.update()
            print("Inscription effectue")
            self.current = "index"
            get_user = Data.get_user(username, password)
            Session.make_session(get_user)
    
    
    def check_update(self, username, password:str, password_repeat:str, nameAndSurname, age, sexe, taille, weight, work):
        
        old_password = Session.get_session()['data']["mot_de_passe"]
        
        if password  == "" and password_repeat == "":
            password = old_password
        elif password == password_repeat and password != "":
            password = password_repeat
        else:
            print("Les deux champs de password doivent correspondre")
            return 
            
        user = User(username,password, nameAndSurname, int(age), self.get_gender(sexe), float(taille)/100, float(weight), work)
        data = Data(user)
        data.update()
        print("mise à jour effectue")
        self.current = "index"
        pass