from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB, PORT, WEBHOOK 
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        self.force_channel = FORCE_SUB
        if FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB)                  
                self.invitelink = link
            except Exception as e:
                print(e)
                print("🅼🅰🅺🅴 🆂🆄🆁🅴 🅱🅾🆃 🅰🅳🅼🅸🅽 🅸🅽 🅵🅾🆁🅲🅴 🆂🆄🅱 🅲🅷🅰🅽🅽🅴🅻")             
                self.force_channel = None
        if WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", PORT).start()     
        print(f'''{me.first_name} 
        

░██████╗███╗░░██╗░█████╗░░██╗░░░░░░░██╗░██████╗  ██████╗░░█████╗░████████╗███████╗
██╔════╝████╗░██║██╔══██╗░██║░░██╗░░██║██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝╚════██║
╚█████╗░██╔██╗██║██║░░██║░╚██╗████╗██╔╝╚█████╗░  ██████╦╝██║░░██║░░░██║░░░░░███╔═╝
░╚═══██╗██║╚████║██║░░██║░░████╔═████║░░╚═══██╗  ██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
██████╔╝██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝  ██████╦╝╚█████╔╝░░░██║░░░███████╗
╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝

''')
      

    async def stop(self, *args):
        await super().stop()      
        print('''
╔══╦═╦══╗╔══╦══╦═╦═╦═╦═╦══╗
║╔╗║║╠╗╔╝║══╬╗╔╣║║╬║╬║╦╩╗╗║
║╔╗║║║║║─╠══║║║║║║╔╣╔╣╩╦╩╝║
╚══╩═╝╚╝─╚══╝╚╝╚═╩╝╚╝╚═╩══╝
              ''')
       

bot=Bot()
bot.run()
