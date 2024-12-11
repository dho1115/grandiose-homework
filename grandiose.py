def FindSynonym(word="operate"):
   from requests import get;
   from dotenv import load_dotenv;
   from json import loads;
   from os import getenv;
   from random import choice

   load_dotenv();
   url = "https://thesaurus-by-api-ninjas.p.rapidapi.com/v1/thesaurus"

   params = dict(word=word);

   headers = {
      "x-rapidapi-key": getenv("myapikey"), #please subscribe to the RAPID URL. Once inside, find the url above to get your own API key.
      "x-rapidapi-host": getenv("myapihost") #also subscribe to get the host.
   }

   response = get(url, params, headers=headers);

   return choice(response.json()["synonyms"]);

result = lambda randomWord, synonym: f"My laptop is so much {synonym} I'm surprised yours can {randomWord}!!!" #This will replace def result(randomWorld, synonym) below.



