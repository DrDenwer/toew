from telethon import *
import random
import logging
from .. import loader, utils
import asyncio

logger = logging.getLogger(__name__)



class YourMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"name": "inf"}



   
    async def ttcmd(self,event):
        await event.delete()
        
        
        
        a=0
        while a<19:  
           await event.respond("🏙 Город")
           await asyncio.sleep(1)  
           await event.respond("🏪 Магазин") 
           await asyncio.sleep(1)  
           await event.respond("/smoke_grnd")

           await asyncio.sleep(11100)  

           await event.respond("🏙 Город")
           await asyncio.sleep(1)  
           await event.respond("🏪 Магазин") 
           await asyncio.sleep(1)  
           await event.respond("/smoke_grnd") 

           await asyncio.sleep(11100)  

           await event.respond("🏙 Город")
           await asyncio.sleep(1)  
           await event.respond("🏪 Магазин") 
           await asyncio.sleep(1)  
           await event.respond("/smoke_grnd") 

           await asyncio.sleep(11100)  

           await event.respond("🏙 Город")
           await asyncio.sleep(1)  
           await event.respond("🏪 Магазин") 
           await asyncio.sleep(1)  
           await event.respond("/smoke_grnd")
           await asyncio.sleep(2)  
           await event.respond("/alikexpress")

           await asyncio.sleep(11100)  
           a+=1
 