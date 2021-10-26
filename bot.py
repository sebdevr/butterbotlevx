import logging

from db import Database
from datastructures import ENV
import utils

from typing import Union
import time
import math

import regex as re

import discord.utils
from discord.ext import commands, tasks
from gsheet import *

config = utils.read_config()

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s")

sheet = gsheet()

client = commands.Bot(command_prefix="!" , case_insensitive=True)

@client.event 
async def on_ready():
    print("The Butter Bot is ready!")

@client.command()
async def fuq(ctx):
    embed =  discord.Embed(title = "FUQ - Frequently Unaswered Questions" , description = "Everything you need to know about LevX DAO 0.111" , color = discord.Colour.green())
    embed.add_field(name = "\u200b", value = "**Q1. Who is LevX?\nQ2. What is LEVX DAO 0.111?\nQ3. What are the perks for $LEVX holders?\nQ4. _Wen_ will $LEVX launch?\nQ5. What is OH-GEEZ token?\nQ6. How do I check if I am eligible for a free $OH-GEEZ token?\nQ7. Where can I buy $OH-GEEZ token?\nQ8. Where do I add liquidity to OH-GEEZ/ETH?\nQ9. How will $LEVX be allocated?\nQ10. How will the 30k $LEVX tokens for the first 10k twitter followers be distributed?\nQ11. What will happen after 6 months lock up?\nQ12. What about the unclaimed $OH-GEEZ token?\nQ13. What will happen with the earnings of the miso auction?**" , inline = False )
    embed.add_field(name = "\u200b", value = "``Choose the question you want answered using: !Q1, !Q2 etc.``", inline = False )
    await ctx.send(embed = embed)

@client.command()
async def q1(ctx):
    embed = discord.Embed(title = "Q1. Who is LevX?" , description = "• LevX is our crazy dictator ruling the DAO. He's also the lead dev/product manager of Shoyu NFT." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q2(ctx):
    embed = discord.Embed(title = "Q2. What is LEVX DAO 0.111?" , description = "• With 0.111 OH-GEEZ token, you can join #😵oh-geez channel and be a Morty. It was DAO 0.333 originally but is degenerating over and over again. Out goal is to be a DAO 0.000000000000000000111 in 2077." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q3(ctx):
    embed = discord.Embed(title = "Q3. What are the perks for $LEVX holders?" , description = "• 33% of shoyu 1-year grant (35k sushi) will be distributed to $LEVX holders.\n\n• Personal AMA with the dictator himself @LevxApp.\n\n• Special roles in the discord.\n\n• $LEVX holders will benefits from all the ongoing & upcoming projects (Sharkpunks, MaidCoin, BearFi, Lev-x and more…).\n\n• Revenue generated from all projects merged into 1 token “$LEVX”." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q4(ctx):
    embed = discord.Embed(title = "Q4. When will $LEVX launch?" , description = "• Early November. Refer to https://dictatorship.levxdao.org/#/proposal/QmX4zuW5ETRHH9SGwTeKvwDczFBdkmABtu9mxq45QfDTud and https://dictatorship.levxdao.org/#/proposal/QmXDHXZPDdXPoUznBhMhwnf2E1Gqnejru7FtB6EGJnUbiL for details." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q5(ctx):
    embed = discord.Embed(title = "Q5. What is OH-GEEZ token?" , description = "• It is a worthless token with a maximum supply of 333. Initial 333 members of LevX DAO discord are eligible to claim their free $Oh-Geez token.\n\n• Holding $Oh-Geez token makes you eligible for $LEVX drop. You can trade Oh-geez on sushiswap.\n\n• Holding at least 0.111 $Oh-Geez gives you a special role in discord (#oh-geez).\n\n• If you want to participate in the governance, you will need to add liquidity to the OhGeez-ETH liquidity pool.\n\n• If you hold more than 10% of the total OHGEEZ-ETH-LP you will receive a special discord role and can put proposals." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q6(ctx):
    embed = discord.Embed(title = "Q6. How do I check if I am eligible for a free $OH-GEEZ token?" , description = "• The initial 333 members of the LevX DAO Discord members are eligible to claim 1 OhGeez token.\n\n• More info here: https://blog.levxdao.org/how-to-acquisition-of-ohgeez-tokens-formortys-48e330a7e100\n\n• First, check your address here: https://raw.githubusercontent.com/levx-io/ohgeez/master/oh-geez.json\n\n• If you want to participate in the governance, you will need to add liquidity to the OhGeez-ETH liquidity pool.\n\n• If you are eligible claim here: https://oh-geez-frontend.herokuapp.com/" , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q7(ctx):
    embed = discord.Embed(title = "Q7. Where can I buy $Oh-geez token?" , description = "• You can find the link in discord channel “#Announcement”.\n\nhttps://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x1098269bFc70b26DeA43f18F812D2b9854E874bA" , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q8(ctx):
    embed = discord.Embed(title = "Q8. Where do I add liquidity to OH-GEEZ/ETH?" , description = "• You can find the link in discord channel “#FAQ”\n\nhttps://app.sushi.com/add/ETH/0x1098269bFc70b26DeA43f18F812D2b9854E874bA" , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q9(ctx):
    embed = discord.Embed(title = "Q9. How will $LEVX be allocated?" , description = "• 30k $LEVX will be distributed for the first 10k twitter followers (@Levxapp). Unclaimed amount will be distributed to Oh-Geez LPs. Oh-Geez LPs need to lock up their LPs for 6 months to be eligible.\n\n• 2750 $LEVX tokens will be distributed to $Oh-Geez holders (1:10 ratio,1 OG =10 $LEVX).\n\n• 763 $LEVX for the miso auction." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q10(ctx):
    embed = discord.Embed(title = "Q10. How will the 30k $LEVX tokens for the first 10k twitter followers be distributed?" , description = "• You are eligible for the drop just by being in the first 10k @Levxapp twitter followers.\n\n• Extra tokens can be earned depending on your contribution. 5 classes for extra tokens:\n\n• CLASS 1: Creator of $LEVX (10% 10k).\n\n• CLASS 2: Core Discord contributor. The more you contribute to the discord the better chance you will have to receive extra tokens (20% 6k).\n\n• CLASS 3: Noise maker: Tweeting, liking, sharing. Introducing the DAO to others (9k 30%).\n\n• CLASS 4: Early $LEVX believers. These are people who were amongst the first to join the DAO (20% 6k)\n\n• CLASS 5: Peoples who did the bear minimum. Even if you did nothing, a follow is always helpful, and you will be rewarded for that (20% 6k)." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q11(ctx):
    embed = discord.Embed(title = "Q11. What will happen to OH-GEEZ LP holders after LEVX releases?" , description = "• You will have the choice between:\n\n1. Lock your LPs for 6 months for LEVX reward then, OH-GEEZ token out of LPs will be burnt and ETH will be returned to the holder.\n2. Migrate your Oh-Geez LPs to LEVX LP (This is recommended as LEVX LP will get a minimum 33.3% of @Levxapp revenue sharing)." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q12(ctx):
    embed = discord.Embed(title = "Q12. What about the unclaimed $Oh-Geez token?" , description = "• 257 out of 333 tokens have been claimed. Unclaimed amount will be distributed to OhGeez LPs (currently 6900 $LEVX)." , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def q13(ctx):
    embed = discord.Embed(title = "What will happen with the earnings of the miso auction?" , description = "• 50% of the earned ETH will be swapped to LEVX\n• With another 50% of ETH, they'll all be added as liquidity to LEVX-ETH pool" , color = discord.Colour.green())
    await ctx.send(embed = embed)

@client.command()
async def add1rdr0p(ctx):

        SPREADSHEET_ID = '1G3A9PSxYllxSaNv5ivCAeyvueoZfJXhIfnvTZTgt8SA'
        RANGE_NAME = 'A1'
        FIELDS = 2 

        # Restrict the command to a role
        # Change REQUIREDROLE to a role id or None
        REQUIREDROLE = None
        if REQUIREDROLE is not None and discord.utils.get(ctx.message.author.roles, id=int(REQUIREDROLE)) is None:
            await ctx.message.channel.send('```You don\'t have the required role!```')
            return
    
      
        msg = ctx.message.content[4:]
        result = [x.strip() for x in msg.split(',') if x]
        if re.match(r"^0x[0-9a-fA-F]{40}$", result[0]):
        
            
            DATA = [ctx.message.author.name] + [str(ctx.message.author.id)] + [str(ctx.message.created_at)] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            await ctx.message.channel.send('```Your data has been successfully submitted!```')
        else:
           
            await ctx.message.channel.send('```This is not a valid ETH address.```'.format(FIELDS,FIELDS-1))


@tasks.loop(seconds=60)
async def check_release():

    for guild in client.guilds:
        db = Database(config.get("DATABASE_FILENAME"))
        if punished_users := db.get_currently_punished_users(config["SECOND_OFFENSE_LIMIT"]):
            for punished_user in punished_users:
                user = await guild.fetch_member(punished_user.member_id)
                if releases_granted(punished_user.punishment_count, punished_user.last_ban):
                    db.set_unbanned(punished_user.member_id, guild.id)
                    role = discord.utils.get(guild.roles, name=config.get("PUNISHMENT_ROLE"))
                    await user.remove_roles(role)


@client.command(name="grant-amnesty", pass_context=True)
async def grant_amnesty(context):

    if any([discord.utils.get(context.message.author.roles, name=_role) for _role in config.get("MAINTENANCE_ROLES")]):
        mentioned_users = context.message.mentions
        for user in mentioned_users:
            db = Database(config.get("DATABASE_FILENAME"))
            db.remove_entry(user.id, context.guild.id)

            role = discord.utils.get(user.guild.roles, name=config.get("PUNISHMENT_ROLE"))
            await user.remove_roles(role)
        verb = "were" if len(mentioned_users) > 1 else "was"
        if mentioned_users:
            await context.send(f"{' '.join([_user.name for _user in mentioned_users])} {verb} granted amnesty.")


@client.command(name="punish-wen", pass_context=True)
async def punish_wen(context):

    if any([discord.utils.get(context.message.author.roles, name=_role) for _role in config.get("MAINTENANCE_ROLES")]):
        mentioned_users = context.message.mentions
        for member in mentioned_users:
            timeout = determine_timeout(member.id, context.guild.id)

            role = discord.utils.get(member.guild.roles, name=config.get("PUNISHMENT_ROLE"))
            await member.add_roles(role)
            logging.info(f'Action: Role {config.get("PUNISHMENT_ROLE")} added for user {member}')

            if math.isinf(timeout):
                timeout_text = f"wen = ban. {member.name} muted forever."
            else:
                timeout_text = f"wen = ban. {member.name} muted for {int(timeout / 60)} minutes."
            await context.send(timeout_text)


def releases_granted(punishment_count: int, last_ban: int) -> bool:

    seconds_since_last_ban = int(time.time()) - last_ban

    if punishment_count == config.get("FIRST_OFFENSE_LIMIT"):
        if seconds_since_last_ban >= config.get("FIRST_OFFENSE_PENALTY"):
            return True
    elif config.get("FIRST_OFFENSE_LIMIT") < punishment_count <= config.get("SECOND_OFFENSE_LIMIT"):
        if seconds_since_last_ban >= config.get("SECOND_OFFENSE_PENALTY"):
            return True
    return False


def determine_timeout(member_id: int, guild_id: int) -> Union[int, float]:
    """Queries the connected database to determine the timeout the users deserves based on his timeout history.
    :param member_id: Discord ID of the member. Primary key of the associated timeout table.
    :param guild_id: Discord ID of the current guild.
    :return: How many minutes the user should be muted (through role assignment). Infinity if user shall be muted
    forever.
    """
    db = Database(config.get("DATABASE_FILENAME"))
    timeout = db.get_timeout(member_id, guild_id)

    if timeout is None:
        db.create_timeout_entry(member_id, guild_id)
        return config.get("FIRST_OFFENSE_PENALTY")

    updated_timeout = timeout + 1
    db.update_timeout(member_id, guild_id, updated_timeout)

    if updated_timeout == 1:
        return config.get("FIRST_OFFENSE_PENALTY")
    elif config.get("FIRST_OFFENSE_LIMIT") < updated_timeout <= config.get("SECOND_OFFENSE_LIMIT"):
        return config.get("SECOND_OFFENSE_PENALTY")
    elif updated_timeout > config.get("SECOND_OFFENSE_LIMIT"):
        return math.inf


def contains_banned_text(message: str) -> bool:
    """Uses regular expression patterns to check whether a message contains bannable text.
    :param message: lower cased message content
    :return: Whether the users deservers a ban or not
    """
    patterns = [r"\b(wen)\b",
                r"(^|\s)(when)(?:\s+\w+){1}(\s)*(?:\?)+($|\s)",
                r"(wen|when)\s(token|airdrop)($|\s)"]

    for pattern in patterns:
        if re.search(pattern, message):
            return True
    return False


@client.listen("on_message")
async def on_message(message):
    """Listener which checks every message for rule violations and takes action if necessary
    :param message:
    """
    if message.author == client.user or any([discord.utils.get(message.author.roles, name=_role)
                                          for _role in config.get("MAINTENANCE_ROLES")]):
        return

    message_channel = client.get_channel(message.channel.id)

    if contains_banned_text(message.content.lower()):
        member = message.author

        timeout = determine_timeout(member.id, message.guild.id)

        role = discord.utils.get(member.guild.roles, name=config.get("PUNISHMENT_ROLE"))
        await member.add_roles(role)
        logging.info(f'Action: Role {config.get("PUNISHMENT_ROLE")} added for user {member}')

        if math.isinf(timeout):
            timeout_text = f"wen = ban. - {member.name} muted forever."
        else:
            timeout_text = f"wen = ban. - {member.name} muted for {int(timeout / 60)} minutes."
        await message_channel.send(timeout_text)

check_release.start()

client.run("ODk5NDQ0MzY1MDQxMjIxNjMy.YWy21w.eMvQKe8aRfmyCSatjPUQ3qVAHLk")