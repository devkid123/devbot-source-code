import discord
import datetime
client = discord.Client()
keywords = ['?devbotabout', 'hi devbot', '?devbothelp']
key_2 = ['how are you devbot?', 'hru devbot?']
key_3 = ['devbot who is devkid?']
key_4 = ["?devkidbirthday"]
key_5 = ['devbot what is life?']
key_6 = ['devbot which year was devkid born?']
key_7 = ['devbot do you have iq?']
key_8 = ['devbot how do you know devkid so much?']
key_9 = ['devbot what is the top 5 best programming languages?']
key_10 = ['devbot how did devkid learn how to code?']
key_11 = ['devbot what programming language does devkid use?']
key_12 = ['?devbot spam']
key_13 = ['devbot how to code in python for beginners level?']
key_14 = ['devbot how to code in python for intermediate level?']
key_15 = ['?devbotcommands']
key_16 = ['devbot what is the time now?']
key_17 = ['devbot did you poop?']
key_18 = ['@devbot']
key_19 = ['i hate devbot']
key_20 = ['jk i dont hate you @devbot', 'jk i dont hate you devbot', 'devbot i was jking']
key_21 = ['@devbot :D', 'devbot :D']
key_22 = ['devbot what is the server ip?', "devbot what is devkid's server ip?"]

tday = datetime.date.today()

bday = datetime.date(2021, 12, 14)


@client.event
async def on_message(message):
     for a in range(len(keywords)):
        if keywords[a] in message.content:
            for j in range(1):
                await message.channel.send("hi there!, im devbot a bot which answers questions(but not every question),check the pinned message or type '?devbotcommand (add a s at the end to work)' to get started!")

     for b in range(len(key_2)):
        if key_2[b] in message.content:
            for j in range(1):
                await message.channel.send('im good :), thanks for asking!')
                
     for c in range(len(key_3)):
         if key_3[c] in message.content:
             for j in range(1):
                 await message.channel.send('devkid is a 11 year old who codes small games and is the owner of dev bot(me),devkid also is a small yter and if you want to you can sub to him: https://www.youtube.com/channel/UC51gai-7PFhvps79o0L-K9A')

     for d in range(len(key_4)):
          if key_4[d] in message.content:
               for j in range(1):
                    till_bday = bday - tday
                    if tday == bday:
                         await message.channel.send("today is devkid's birthday!, happy birthday to devkid! :))")
                    else:
                         await message.channel.send(str(till_bday.days) + ' days left for devkids birthday!')
                    
     for e in range(len(key_5)):
          if key_5[e] in message.content:
               for j in range(1):
                    await message.channel.send("oh, thats a complitcated question...")
                    
     for f in range(len(key_6)):
          if key_6[f] in message.content:
               for j in range(1):
                    await message.channel.send("devkid was born on the year 2009!")
                    
     for g in range(len(key_7)):
          if key_7[g] in message.content:
               for j in range(1):
                    await message.channel.send("in terms of knowlegde or iq,we have none")

     for h in range(len(key_8)):
          if key_8[h] in message.content:
               for j in range(1):
                    await message.channel.send("im just a bot who replays to a specific command/question XD")
                    
     for i in range(len(key_9)):
          if key_9[i] in message.content:
               for j in range(1):
                    await message.channel.send("the best programming languages are javascript, python, c/c++, java, c#")

     for j in range(len(key_10)):
          if key_10[j] in message.content:
               for w in range(1):
                    await message.channel.send("devkid learned how to code from tutorials in yt vids")

     for k in range(len(key_11)):
          if key_11[k] in message.content:
               for j in range(1):
                    await message.channel.send("devkid uses python to code games, and even code me!")

     for l in range(len(key_12)):
          if key_12[l] in message.content:
               for j in range(7):
                    await message.channel.send('spamming')

     for m in range(len(key_13)):
          if key_13[m] in message.content:
               for j in range(1):
                    await message.channel.send('check this playlist out!:https://www.youtube.com/watch?v=OFrLs22MDAw&list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm ')

     for n in range(len(key_14)):
          if key_14[n] in message.content:
               for j in range(1):
                    await message.channel.send('check this playlist out!:https://www.youtube.com/watch?v=0VdzZQdaZ28&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv')

     for o in range(len(key_15)):
          if key_15[o] in message.content:
               for j in range(1):
                    await message.channel.send('bot commands that you can use!: ?devbothelp')

     for p in range(len(key_16)):
          if key_16[p] in message.content:
               for j in range(1):
                    await message.channel.send('todays day is ' + str(tday))

     for q in range(len(key_17)):
          if key_17[q] in message.content:
               for j in range(1):
                    await message.channel.send("im just a bot lol, so i didn't")

     for r in range(len(key_18)):
          if key_18[r] in message.content:
               for j in range(1):
                    await message.channel.send('hi there!, is there anything i can help you with?')

     for s in range(len(key_19)):
          if key_19[r] in message.content:
               for j in range(1):
                    await message.channel.send(':C')

     for t in range(len(key_20)):
          if key_20[t] in message.content:
               for j in range(1):
                    await message.channel.send(':D')

     for u in range(len(key_21)):
          if key_21[u] in message.content:
               for j in range(1):
                    await message.channel.send(':DD')

     for v in range(len(key_22)):
          if key_22[v] in message.content:
               for j in range(1):
                    await message.channel.send('the server ip is devkidserver.aternos.me, join now!(the server is not 24/7)')
     



client.run('ODU5MzIwMTkzMDQ1MjMzNjc0.YNq-Sw.fhs_JiZbblJeXKdtwdn5CH5C1Cs')

