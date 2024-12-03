from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date


def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет!")

#def talk_to_me(update, context):
#   text = update.message.text
#   print(text)
#   update.message.reply_text(text)

def planets(update, context):
    import ephem
    print("Вызвана функция planets")

    import datetime
    today = date.today() 
#    planet = update.message.text
#   planet = ephem.Mars('2024/11/29')
#   update.message.reply_text("Планета {planet}")
#   print(planet)
#   const = ephem.constellation(planet)
#   print(const)
#   update.message.reply_text(const)
    try:
#      planet = ephem.Mars('2024/11/29')
      planet = update.message.text
      planet_name = planet.split()
      print(planet_name)
      name = planet_name[1]

      Mars = ephem.Mars(today)
#      Earth = ephem.Earth("2024/11/30")
      Uranus = ephem.Uranus(today)
      Jupiter = ephem.Jupiter(today)
      Neptune = ephem.Neptune(today)
      Venus = ephem.Venus(today)
      Pluto = ephem.Pluto(today)
      Mercury = ephem.Mercury(today)
      if name == "Mars":
          const = ephem.constellation(Mars)
      elif name == "Jupiter":
          const = ephem.constellation(Jupiter)
      elif name == "Uranus":
          const = ephem.constellation(Uranus)
      elif name == "Neptune":
          const = ephem.constellation(Neptune)
      elif name == "Venus":
          const = ephem.constellation(Venus)
      elif name == "Pluto":
          const = ephem.constellation(Pluto)
      elif name == "Mercury":
          const = ephem.constellation(Mercury)
      else:
#     const = ephem.constellation(Earth)
          print("Не знаю такую планету")
      print(const)
      update.message.reply_text(const)
    except Exception as e:
      print(e)


def main():

    mybot = Updater("7834567751:AAGfqPXRFL3-GDBOH0IcORp7DSIzyJ_W-Jw", use_context = True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
#   dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, planets))
    mybot.start_polling()
    mybot.idle()

main()

input()