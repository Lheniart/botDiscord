import discord
from discord.ext import commands
from blagues_api import BlaguesAPI, BlagueType





tokenBlague = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTE1ODM3NDYxMTI3MzEyMTg1MiIsImxpbWl0IjoxMDAsImtleSI6IkxxbmwySElPWGJDcDIzdWxRY3h3TEJLNnAwd0xETnR3R0pyTlQ1SG1LSHFFR2JUNGExIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDQtMzBUMTI6NTI6NDkrMDA6MDAiLCJpYXQiOjE3MTQ0ODE1Njl9.PfYjm2A_4vQtLb0IflUQzkc4nofwtQWD9jaSeQ7dMc0'
blagues = BlaguesAPI(tokenBlague)

welcome_message = "Bienvenue sur notre serveur ! Nous sommes heureux de vous avoir parmi nous."

mot_a_detecter = "voldemort"

#Intents
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True

# guilds = serveurs discords
intents.guilds = True
intents.members = True


# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
    print (f"{bot.user.name} s'est bien connecté !")

@bot.event
async def on_member_join(member):
    # Envoyer le message de bienvenue dans un salon spécifique (vous pouvez personnaliser cela selon vos besoins)
    channel = member.guild.system_channel  # Récupérer le salon de bienvenue par défaut du serveur
    if channel is not None:
        await channel.send(welcome_message)

@bot.command()
async def welcome(ctx):
    # Envoyer le message de bienvenue dans le salon où la commande a été utilisée
    await ctx.send(welcome_message)

# Commande !ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande !touché
@bot.command()
async def touché(ctx):
    await ctx.send("coulé ! 💥")

# Commande !members
@bot.command()
async def members(ctx):
    members_list = ctx.guild.members

    members_info = "Liste des membres :\n"
    
    # Boucler à travers chaque membre
    for member in members_list:

        nickname = member.display_name

        roles = [role.name for role in member.roles]

        members_info += f"{nickname} - {' | '.join(roles)}\n"

    await ctx.send(members_info)

@bot.event
async def on_message(message):
    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")

    await bot.process_commands(message)

# Commande !joke
@bot.command()
async def joke(ctx):
    blague = await blagues.random()
    # Envoyer la blague dans le salon où la commande a été utilisée
    await ctx.send(f"{blague.joke}\n||{blague.answer}||")


# Événement pour détecter lorsque qu'un message est envoyé


#connexion du bot au serveur avec au token
bot.run("MTIzNDgzOTE2MTQ4NDIxODQwOA.G0ecdp.SwBluT0IX7l4Pens2WMsLchQm2E80vFJidBF-k")