from chessdotcom import get_player_stats, get_player_profile
import discord
from discord.ext import commands
from datetime import datetime
import openai

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

TOKEN = "MTA3MzQ0OTU2NjA3MTk0NzM3NA.GTmkLi.RjUtqbGqiRyV6jbX_3b52Isk2NKrH9ZWBqULzI"

@bot.event
async def on_ready():
    print("bot has connected to Discord")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
@bot.command()
async def chess(ctx, name):
    player_profile_json = get_player_profile(name)
    profile = player_profile_json.json
    username = profile["player"]["username"]
    avatar = profile["player"]["avatar"]
    followers = profile["player"]["followers"]
    status = profile["player"]["status"]
    last_online = profile["player"]["last_online"]
    joined = profile["player"]["joined"]
    league = profile["player"]["league"]

    player_stats = get_player_stats(name)
    stats_json = player_stats.json

    rapid = stats_json["stats"]["chess_rapid"]
    rapid_rating = rapid["last"]["rating"]
    rapid_date = rapid["last"]["date"]
    rapid_best_rating = rapid["best"]["rating"]
    rapid_best_date = rapid["best"]["date"]
    rapid_record_win = rapid["record"]["win"]
    rapid_record_loss = rapid["record"]["loss"]
    rapid_record_tie = rapid["record"]["draw"]

    bullet = stats_json["stats"]["chess_bullet"]
    bullet_rating = bullet["last"]
    bullet_rating = bullet["last"]["rating"]
    bullet_date = bullet["last"]["date"]
    bullet_best_rating = bullet["best"]["rating"]
    bullet_best_date = bullet["best"]["date"]
    bullet_record_win = bullet["record"]["win"]
    bullet_record_loss = bullet["record"]["loss"]
    bullet_record_tie = bullet["record"]["draw"]

    blitz = stats_json["stats"]["chess_blitz"]
    blitz_rating = blitz["last"]
    blitz_rating = blitz["last"]["rating"]
    blitz_date = blitz["last"]["date"]
    blitz_best_rating = blitz["best"]["rating"]
    blitz_best_date = blitz["best"]["date"]
    blitz_record_win = blitz["record"]["win"]
    blitz_record_loss = blitz["record"]["loss"]
    blitz_record_tie = blitz["record"]["draw"]
    
    embed = discord.Embed(title=username,
                          description ="Chess.com Stats",
                          color=000000,
                          url= f"https://www.chess.com/member/{username}")
    embed.set_author(name=username, icon_url=avatar)
    embed.add_field(
        name= "🥽 Profile",
        value = f"🧑 Followers : {followers} \n  💎 Status : {status} \n 🏆 League: {league} \n 🟢 Last Online : {datetime.fromtimestamp(last_online).strftime('%b %d, %Y')} \n 📝 Member since : {datetime.fromtimestamp(joined).strftime('%b %d, %Y')} \n -------------------------------------------------",
        inline= False
    )
    
    embed.add_field(
        name="🕒 Rapid Stats",
        value = f"Current Rating : {rapid_rating} \n Rapid Best Rating : {rapid_best_rating} \n Record : W-{rapid_record_win} L-{rapid_record_loss} T-{rapid_record_tie}",
        inline= False
    )
    embed.add_field(
        name= "🎯 Bullet Stats",
        value = f"Current Rating : {bullet_rating} \n Bullet Best Rating : {bullet_best_rating} \n Record : W-{bullet_record_win} L-{bullet_record_loss} T-{bullet_record_tie}",
        inline= False
    )
    embed.add_field(
        name= "👑 Blitz Stats",
        value= f"Current Rating : {blitz_rating} \n Blitz Best Rating : {blitz_best_rating} \n Record : W-{blitz_record_win} L-{blitz_record_loss} T-{blitz_record_tie}",
        inline= False
    )
    embed.set_thumbnail(url=avatar)
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fblog.hdwallsource.com%2Fwp-content%2Fuploads%2F2016%2F02%2Fchess-23573-24226-hd-wallpapers.jpg&f=1&nofb=1&ipt=e64b49a3253132d6f7a487e905509a4c3637b7fe2339fab65097427487cad5bd&ipo=images")
    embed.set_footer(
        text="Made with www.Chess.com",
        icon_url= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fyt3.ggpht.com%2Fa-%2FAAuE7mDlUeqCOCJKsBtlgDdFKEKVznbChlVy51qS1w%3Ds900-mo-c-c0xffffffff-rj-k-no&f=1&nofb=1&ipt=63b365d925987bd3690849e690ff5bca622694e31e74b38d786439b38eb77741&ipo=images"
    )
    await ctx.send(embed=embed)
    
    
@bot.command()
async def openai(ctx, prompt):
    TOKEN = "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"
    openai.api_key = TOKEN
    

    image = openai.Image.create(
    prompt = prompt,
    n=1,
    size="512x512"
    )

    print(image)
    await ctx.send("done!")

bot.run(TOKEN)





