def FindSynonym(word="operate"):
   from requests import get;
   from dotenv import load_dotenv;
   from json import loads;
   from os import getenv;
   from random import choice

   load_dotenv();
   url = "https://thesaurus-by-api-ninjas.p.rapidapi.com/v1/thesaurus"

   querystring = dict(word=word);

   headers = {
      "x-rapidapi-key": getenv("myapikey"), #please subscribe to the url above to get your own API key.
      "x-rapidapi-host": getenv("myapihost") #also subscribe to get the host.
   }

   response = get(url, headers=headers, params=querystring)

   return choice(response.json()["synonyms"]);

def result(fn, synonym):
   return f"My laptop is so much {synonym} I'm surprised yours can {fn}!!!"