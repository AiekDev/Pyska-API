import discord
import openai
from langchain.document_loaders.chatgpt import ChatGPTLoader
from langchain.retrievers import ChatGPTPluginRetriever
from discord.ext import commands
import langchain
import os
from langchain.llms import OpenAI, OpenAIChat
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain # do not remove any of these unless u know what youre doing

bot = discord.Bot()

os.environ['OPENAI_API_KEY'] = 'add your token fr' # NOTE : This is a base for your own bot, which means some functions have been removed to keep Pyska-API it's thing!

@bot.command()
async def chatgpt(ctx, message):
    llm = OpenAIChat()

    # Prompt
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "Your name is PyskaGPT, based on ChatGPT from OpenAi." # you can always edit this!
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
    await ctx.send(f"`Command used: /chatgpt`\n**User Input**:\n{message}\n**Result: ** {result}\n")


goofy4 = '''**Pyska-API has 5 commands, here is what they all do :**
```/help - Says all the 5 commands that can be used with PyskaAPI
/pyskavideo - sends a video of pyska
/pyskapicture - sends a pyska pic :3 
/chatgpt - PyskaGPT!!
/about - information about the bot
```
''' # only 5 commands have been kept for open source project, why? because youre supposed to be original and know how to edit code, being a skid isnt good for you

@bot.command()
async def pyskapicture(ctx):
    await ctx.respond("**here is your pyska pic**")
    await ctx.send("https://media.discordapp.net/attachments/1119200715848548392/1151765221862543360/pisica.png")


@bot.command()
async def help(ctx):
    await ctx.respond(goofy4)

@bot.command()
async def pyskavideo(ctx):
    await ctx.respond("**heres a video of me**")
    await ctx.send(
        "https://cdn.discordapp.com/attachments/1119200715848548392/1151782214946799676/VID-20230424-WA0000.mp4")


@bot.command()
async def about(ctx):
    await ctx.respond(
        "**Pyska-API (OPEN SOURCE EDITION)** - Open Source Python Discord Bot - (developed by `@aiek.`, contribuitors : `@robom101`)")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='PYSKA-API (OPEN SOURCE EDITION) - /help for commands!'), status=discord.Status.do_not_disturb)


bot.run("yourdiscordtoken")
