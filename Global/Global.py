import discord
import requests
import validators

class Global:

    def analisysURL(self,urlAnalisys, token): 

        url = "https://www.virustotal.com/api/v3/urls"

        payload = {"url": urlAnalisys}
        headers = {
                "accept": "application/json",
                "x-apikey": token,
                "content-type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=payload, headers=headers)
        response = response.json()

        result = self.resultAnalisys(response['data']['id'],token)

        return result 


    def resultAnalisys(self,id, token):
        url = f"https://www.virustotal.com/api/v3/analyses/{id}"

        headers = {
            "accept": "application/json",
            "x-apikey": token
        }

        response = requests.get(url, headers=headers)
        response = response.json()

        return response['data']['attributes']['stats']

