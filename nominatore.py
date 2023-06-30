import discord

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="Imposta nome, cognome e server del tuo personaggio.",
                   guild_ids=[1118403657784889404])
async def setup(ctx, nome:str, cognome:str):
    
    await ctx.author.edit(nick=f"{nome.capitalize()} {cognome.capitalize()}")
    await ctx.author.add_roles(ctx.guild.get_role(1118622975483183154))
    await ctx.respond("Nome cambiato con successo.")
    
bot.run('MTEyMjQ2MTM0NjkxOTg4Mjg0Mw.G1o-21.ydXTCVC0ekbTRfsavAmm1aueOOqRPT-YHkTL2I')
