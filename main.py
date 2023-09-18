import discord
import openai
from langchain.document_loaders.chatgpt import ChatGPTLoader
from langchain.retrievers import ChatGPTPluginRetriever
from discord.ext import commands
import langchain
import os
from langchain.llms import OpenAI, OpenAIChat
from langchain.schema import AIMessage, HumanMessage, SystemMessage # it is recommended to not remove imports!
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from discord.ext import commands
from langchain.chains import LLMChain
# it is recommended to not remove imports!
bot = discord.Bot()
# it is recommended to not remove imports!
os.environ['OPENAI_API_KEY'] = 'addyourownopenaikeyhereforpyskagptandchatgptcommandstowork!'
# it is recommended to not remove imports!

# very needed comment


# moderation commands
# moderation commands
# moderation commands
# moderation commands
# moderation commands
# moderation commands
# moderation commands

# purge messages
# purge messages
# purge messages
# purge messages
# purge messages
# purge messages
@bot.command()
async def purge(ctx, amount: int):
    # Check if the user has permission to manage messages
    if ctx.author.guild_permissions.manage_messages:
        try:
            deleted_messages = await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message
            await ctx.send(f"{len(deleted_messages) - 1} messages were deleted by {ctx.author.mention}.", delete_after=5)
        except discord.Forbidden:
            await ctx.send("Operation cannot be completed : No **Manage Messages** permissions!")
    else:
        await ctx.send("**You don't have permission to use this command!**")
# ban
# ban
# ban
# ban
# ban
# ban
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: commands.UserConverter, *, reason="No reason provided"):
    try:
        await ctx.guild.ban(user, reason=reason)
        # Sends a DM to the banned user
        await user.send(f"You have been banned from {ctx.guild.name} for the following reason: {reason}")
        # Send a confirmation message in the server
        await ctx.send(f"{user.mention} has been banned for the reason: {reason}")
    except commands.MissingPermissions:
        await ctx.send("You don't have permission to ban users.")
    except commands.BadArgument:
        await ctx.send("Invalid user provided.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
# kick
# kick
# kick
# kick
# kick
# kick
# kick
# kick
# kick
# kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: commands.UserConverter, reason="No reason provided"):
    try:
        await ctx.guild.kick(user, reason=reason)
        # Sends a DM to the kicked user
        await user.send(f"You have been kicked from {ctx.guild.name} for the following reason: {reason}")
        # Sends a confirmation message in the server
        await ctx.send(f"{user.mention} has been kicked for the reason: {reason}")
    except commands.MissingPermissions:
        await ctx.send("You don't have permission to kick users.")
    except commands.BadArgument:
        await ctx.send("Invalid user provided.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun
# non-moderation/for fun

# ai commands!!!
# ai commands!!!
# ai commands!!!

# pyskagpt (acts like a dumb cat, you can always change this :  "You are Pyska. You are Aiek's cat. Respond concisely and only use LolCat english." to your peference!
@bot.command()
async def pyskagpt(ctx, message):
    llm = OpenAIChat()

    # Prompt
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are Pyska. You are Aiek's cat. Respond concisely and only use LolCat english."
            ),
            # The `variable_name` here is what must align with memory
            # MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human}")
        ]
    )

    # Notice that we `return_messages=True` to fit into the MessagesPlaceholder
    # Notice that `"chat_history"` aligns with the MessagesPlaceholder name
    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        # memory=memory
    )

    # Notice that we just pass in the `question` variables - `chat_history` gets populated by memory
    result = conversation({"human": f"{message}"})['text']
    await ctx.send(discord.utils.escape_mentions(f"`Command used: /pyskagpt`\n**User Input**:\n{message}\n**Result: ** {result}\n"))

# chatgpt (acts like normal chatgpt, except it is named pyskagpt!)
# chatgpt (acts like normal chatgpt, except it is named pyskagpt!)
# chatgpt (acts like normal chatgpt, except it is named pyskagpt!)

@bot.command()
async def chatgpt(ctx, message):
    llm = OpenAIChat()

    # Prompt
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "Your name is PyskaGPT, based on ChatGPT from OpenAi."
            ),
            # The `variable_name` here is what must align with memory
            # MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human}")
        ]
    )

    # Notice that we `return_messages=True` to fit into the MessagesPlaceholder
    # Notice that `"chat_history"` aligns with the MessagesPlaceholder name
    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        # memory=memory
    )

    # Notice that we just pass in the `question` variables - `chat_history` gets populated by memory
    result = conversation({"human": f"{message}"})['text']
    await ctx.send(discord.utils.escape_mentions(f"`Command used: /chatgpt`\n**User Input**:\n{message}\n**Result: ** {result}\n"))

# unimportant commands, you can remove these or make your own!
# unimportant commands, you can remove these or make your own!
# unimportant commands, you can remove these or make your own!
# unimportant commands, you can remove these or make your own!

@bot.command()
async def pyskapicture(ctx):
    await ctx.respond("**here is your pyska pic**")
    await ctx.send("https://media.discordapp.net/attachments/1119200715848548392/1151765221862543360/pisica.png")


@bot.command()
async def givememoney(ctx):
    await ctx.respond("**ok heres my credit card**")
    await ctx.send("https://cdn.discordapp.com/attachments/1109190484859035668/1151843506525044756/credit.png")


@bot.command()
async def whatismyip(ctx):
    await ctx.respond("**80.123.10.104** :scream:")


@bot.command()
async def whatisyourpurpose(ctx):
    await ctx.respond(goofy)


@bot.command()
async def announcement(ctx):
    await ctx.respond(goofy3)


@bot.command()
async def pyskaspeechbubble(ctx):
    await ctx.respond("https://media.discordapp.net/attachments/1109190484859035668/1135866564026040400/attachment.gif")


@bot.command()
async def help(ctx):
    await ctx.respond(goofy4)


@bot.command()
async def lowtiergod(ctx):
    await ctx.respond("https://tenor.com/view/ltg-low-tier-god-yskysn-ltg-thunder-thunder-gif-23523876")


@bot.command()
async def pyskavideo(ctx):
    await ctx.respond("**heres a video of me**")
    await ctx.send(
        "https://cdn.discordapp.com/attachments/1119200715848548392/1151782214946799676/VID-20230424-WA0000.mp4")


@bot.command()
async def kys(ctx):
    await ctx.respond("https://cdn.discordapp.com/attachments/1119173657147740262/1151910571436945469/kys.mp4")


@bot.command()
async def fr(ctx):
    await ctx.respond("**fr**")
    await ctx.send(fr)



@bot.command()
async def about(ctx):
    await ctx.respond(
        "**Pyska-API** - Open Source Python Discord Bot - (developed by `@aiek.`, contribuitors : `@robom101`)")
    await ctx.send("GITHUB LINK : https://github.com/AiekDev/Pyska-API")

# bot status! you can always change this to your liking
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='PYSKA-API - /help for commands!'), status=discord.Status.idle)





# ignore these, you can remove them lol

goofy = '''The Pyska API: Empowering Automation

Introduction:
APIs (Application Programming Interfaces) are transforming our digital world, and the Pyska API is a compelling example. In this discussion, we'll explore its significance, powering your Discord bot's daily cat picture posts.

Efficiency Through Automation:
Pyska automates daily cat picture posts in Discord, saving time. APIs like Pyska enhance efficiency by eliminating manual tasks.

Seamless Communication:
Pyska facilitates communication between software systems, allowing your bot to fetch cat pictures seamlessly, bridging application gaps.

Access to Rich Content:
Pyska enriches your Discord server's content with an abundance of cat pictures. APIs grant applications access to vast data repositories, enhancing user experiences.

Customization and Innovation:
Pyska fosters developer innovation, enabling unique user interactions. Your cat picture bot showcases the creativity empowered by APIs.

Cross-Platform Compatibility:
Pyska ensures a consistent cat picture experience for Discord users, regardless of device or location.

Data Security and Privacy:
Pyska adheres to data protection standards, emphasizing API security and user data privacy.

Economic Impact:
APIs like Pyska contribute to economic growth by fostering innovation in the tech industry.

Global Reach:
Discord users worldwide enjoy your cat pictures, highlighting APIs' role in promoting global connectivity.

Conclusion:
The Pyska API streamlines tasks, enhances communication, and fuels innovation. As technology advances, APIs like Pyska will continue shaping a more efficient and engaging digital landscape.'''

goofy3 = '''Please DO NOT announce to the server when you are going to go masturbate. This has been a reoccurring issue, and I'm not sure why some people have such under developed social skills that they think that a server full of mostly male strangers would need to know that. No one is going to be impressed and give you a high five (especially considering where that hand has been). I don't want to add this to the rules, since it would be embarrassing for new users to see that we have a problem with this, but it is going to be enforced as a rule from now on.

If it occurs, you will be warned, then additional occurrences will be dealt with at the discretion of modstaff. Thanks.'''

goofy4 = '''**Pyska-API has 17 commands, here is what they all do :**

**FOR MODERATION**
```/ban - Requirement : Ban permission/Administrator
/kick - Requirement : Kick permission
/purge (deletes messages) - Requirement : Manage Messages permission

NOTE : For Pyska-API to execute the moderation commands, Administrator permissions are needed, otherwise, these commands won't work!!!```
**FOR FUN**
```/help - Says all the 17 commands that can be used with Pyska-API
/pyskavideo - Sends a video of pyska
/pyskapicture - Sends a pyska pic :3
/lowtiergod - Sends the infamous lowtiergod gif 
/kys - Sends a lowtietgod video (fr fr)
/whatisyourpurpose - sends an essay about the impact of PyskaAPI on our daily life
/announcement - The staff NEED to stop informing other people when they are going to masturbate!
/givememoney - You can have Pyska's credit card now (for free!!)
/pyksagpt - PyskaGPT is an AI that acts like my cat pretty much
/chatgpt - PyskaGPT but acts like ChatGPT
/fr - Spams the phrase "fr" (i mean it)
/pyskaspeechbubble - Sends a speechbubble of Pyska to make fun of the person on top
/about -  Information about the bot
/whatismyip - Sends a fake IP address```
'''

fr = '''FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR FR '''

bot.run("insertyourownbottokenhere")
