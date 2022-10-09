import requests

url = "https://api.brawlstars.com/v1/"

 
class Client:

    def __init__(self, token):
        self.token = "Bearer " + token
        self.headers = {'User-Agent': 'Brawlstars | Python', 'Authorization': self.token}

    def get_player(self, tag):
        tag = tag.strip("#").upper()
        return self.Player(self, tag)

    def get_club(self, tag):
        tag = tag.strip("#").upper()
        return self.Club(self, tag)
    
    def get_events_rotation(self):
        data = requests.get(url=(url + "events/rotation"), headers=self.client.headers)
        return data.json()

    class Player:
        
        def __init__(self, client, tag):
            self.client = client
            self.tag = tag

        def get_info(self):
            data = requests.get(url=(url + "players/%23" + self.tag), headers=self.client.headers)
            return data.json()
        
        def get_battlelog(self):
            data = requests.get(url=(url + "players/%23" + self.tag + "/battlelog"), headers=self.client.headers)
            return data.json()

    class Club:

        def __init__(self, client, tag):
            self.client = client
            self.tag = tag

        def get_info(self):
            data = requests.get(url=(url + "clubs/%23" + self.tag), headers=self.client.headers)
            return data.json()

        def get_members(self):
            data = requests.get(url=(url + "clubs/%23" + self.tag + "/members"), headers=self.client.headers)
            return data.json()

