import os
import discord
from groq import Groq

# Initialize Groq client
groq_client = Groq(api_key="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")

# Discord bot token
token = "MTIzOTkwMDIwNDUwMTgyNzY3NA.G0dBj4.QKASsWwbKAar7Uw07RK6ms_5qocs3n2UcIYrSk"

# Discord client
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        try:
            if message.author == self.user:
                return  # Ignore messages from the bot itself

            if self.user in message.mentions:
                completion = groq_client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {
                            "role": "user",
                            "content": message.content,
                        }
                    ],
                )
                response = completion.choices[0].message.content
                await message.channel.send(response)

        except Exception as e:
            print(e)

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(token)

