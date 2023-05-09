import os
from discord_webhook import DiscordWebhook, DiscordEmbed

Webhook1 = os.environ['webhookS1']
Webhook2 = os.environ['webhook2S2']

webhook_urls = [Webhook1, Webhook2]

webhooks = DiscordWebhook.create_batch(urls=webhook_urls)

embed_title = input('Enter a Title: ')
embed_color = int(input('Enter a color code: '))
thumb_image_url = input('Enter Thumbnail image URL: ')
image_url = input('Enter Image URL: ')
description = input('Please enter a description: ')
set_curl = input('Do you want to set a clickable URL? (0 = yes, 1 = no) ')
if set_curl == '0':
    set_curl = True
    curl = input('What URL do you want? ')
else:
    if set_curl == '1':
        set_curl = False

for webhook in webhooks:
    embed = DiscordEmbed(title=embed_title, color=embed_color)
    embed.set_image(url=image_url)
    embed.set_thumbnail(url=thumb_image_url)
    embed.set_description(description)
    if set_curl:
        embed.set_url(url=curl)
    webhook.add_embed(embed)

response1 = webhooks[0].execute()
response2 = webhooks[1].execute()
