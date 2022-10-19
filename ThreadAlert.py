# ThreadAlert by daishin
# Ver.0.0 2022/10/19
# The bot that post a message to specific channel when a new thread is made in the guild
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = '*****'			# Bot token on discord developer portal
CHANNEL_ID = *****		# Channel id where the bot talk to

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_thread_create(thread):
	channel = client.get_channel(CHANNEL_ID) 
	msg = "Thread <#" + str(thread.id) + "> is appeared in <#" + str(thread.parent_id) + ">."
	await channel.send(msg)

client.run(TOKEN)
