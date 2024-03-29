import discord
import psycopg2
import random
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
try:
    connection = psycopg2.connect(user = os.getenv("DBUSER"),
                                  password = os.getenv("DBPASS"),
                                  host = os.getenv("DBHOST"),
                                  port = os.getenv("DBPORT"),
                                  database = os.getenv("DBNAME"))
    cursor = connection.cursor()
    print(connection)
    postgreSQL_select_Query = 'SELECT * FROM pictures'
    cursor.execute(postgreSQL_select_Query)
    url_list = cursor.fetchall()
except (Exception, psycopg2.Error) as error:
    print(f'Error while fetching data from PostgreSQL', error)
finally:
    #Closing db connection
    if connection:
        cursor.close()
        connection.close()
        print(f'DB connection has been closed')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

message_cooldown = commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.user)

input = str('!shooter')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author != client.user and message.content.lower() == input:
        bucket = message_cooldown.get_bucket(message)
        retry_after = bucket.update_rate_limit()
    else:
        return
    if retry_after:
        return
    else:
        output = url_list[random.randint(0, len(url_list)-1)]  
        cleanedOutput = str(output).replace("'", '').replace(',','').replace('(', '').replace(')', '')
        await message.channel.send(cleanedOutput)

client.run(os.getenv("TOKEN"))
