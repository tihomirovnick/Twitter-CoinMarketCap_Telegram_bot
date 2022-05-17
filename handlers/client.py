from aiogram import types, Dispatcher
from create import dp, bot
from handlers import config
from requests import Session
import json
import tweepy
import asyncio
from data_base import sqlite_db

global ID
global IDR
ID = 511151694
IDR = 956247373


# Start
async def cm_start(message: types.Message):
    await sqlite_db.sql_add_command()

    await bot.send_message(message.from_user.id, 'Бот запущен, скоро появятся новые твиты от Hotbit_news.')

    while True:
        client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        query = "#newlistings from:Hotbit_news"
        response = client.search_recent_tweets(query=query, max_results=10)

        # Add to database
        tweets = []
        for tweet in response.data:
            tweets.append(str(tweet.id))
            break
        element = str(tweets[0])
        await sqlite_db.sql_edit_command(str(element))

        db_back = await sqlite_db.sql_read()

        # Main cycle
        while True:
            client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
            query = "#newlistings from:Hotbit_news"
            response = client.search_recent_tweets(query=query, max_results=10)
            latest_id = response.meta['newest_id']

            if str(db_back) != str(latest_id):
                for tweet in response.data:
                    text = str(tweet.text)
                    parse = text.strip('[]').split('\n')
                    break

                parse_check = []
                for pars in parse:
                    if pars.startswith('$'):
                        pars_splited = pars.strip('[]').split(' ')
                        pars_element = pars_splited[0]
                        if '$' in pars_element:
                            pars_element = pars_element.replace('$', '')
                            parse_check.append(pars_element)
                        break

                symb = str(parse_check[0])

                if (str(parse[3])).startswith('Deposit') == True:

                    # Coinmarketcap
                    try:
                        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
                        parameters = {'symbol': symb}
                        headers = {'Accepts': 'application/json',
                                   'X-CMC_PRO_API_KEY': 'bdb009e3-3886-4fbf-8d13-47ebf57d62aa', }

                        session = Session()
                        session.headers.update(headers)
                        response = session.get(url, params=parameters)

                        week = json.loads(response.text)['data'][symb]['quote']['USD']['percent_change_7d']
                        if week >= 0:
                            week = f"🔋Week {int(week)}%"
                        else:
                            week = f"🛢Week {int(week)}%"
                        month = json.loads(response.text)['data'][symb]['quote']['USD']['percent_change_30d']
                        if month >= 0:
                            month = f"🔋Month {int(month)}%"
                        else:
                            month = f"🛢Month {int(month)}%"
                        name = json.loads(response.text)['data'][symb]['slug']

                        # Final message
                        await bot.send_message(ID,
                                               f"{'<b>'}{parse[3]}{'</b>'}\n{'<b>'}{parse[4]}{'</b>'}\n{'<b>'}{parse[6]}{'</b>'}\n\n{month} {week}\n" + f'<a href="https://coinmarketcap.com/currencies/{str(name)}/">CMC</a>',
                                               parse_mode='HTML', disable_web_page_preview=True)
                        await bot.send_message(IDR,
                                               f"{'<b>'}{parse[3]}{'</b>'}\n{'<b>'}{parse[4]}{'</b>'}\n{'<b>'}{parse[6]}{'</b>'}\n\n{month} {week}\n" + f'<a href="https://coinmarketcap.com/currencies/{str(name)}/">CMC</a>',
                                               parse_mode='HTML', disable_web_page_preview=True)
                        await asyncio.sleep(60)
                        await sqlite_db.sql_edit_command(str(latest_id))
                        break
                    except:
                        await asyncio.sleep(60)
                        await sqlite_db.sql_edit_command(str(latest_id))
                        break


                elif (str(parse[5])).startswith('$') == True:
                    try:
                        # Coinmarketcap
                        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
                        parameters = {'symbol': symb}
                        headers = {'Accepts': 'application/json',
                                   'X-CMC_PRO_API_KEY': 'bdb009e3-3886-4fbf-8d13-47ebf57d62aa', }

                        session = Session()
                        session.headers.update(headers)
                        response = session.get(url, params=parameters)

                        week = json.loads(response.text)['data'][symb]['quote']['USD']['percent_change_7d']
                        if week >= 0:
                            week = (f"🔋Week {int(week)}%")
                        else:
                            week = (f"🛢Week {int(week)}%")

                        month = json.loads(response.text)['data'][symb]['quote']['USD']['percent_change_30d']
                        if month >= 0:
                            month = (f"🔋Month {int(month)}%")
                        else:
                            month = (f"🛢Month {int(month)}%")

                        name = json.loads(response.text)['data'][symb]['slug']

                        # Final message
                        await bot.send_message(ID,
                                               f"\n{'<b>'}{parse[5]}{'</b>'}\n\n{month} {week}\n" + f'<a href="https://coinmarketcap.com/currencies/{str(name)}/">CMC</a>',
                                               parse_mode='HTML', disable_web_page_preview=True)
                        await bot.send_message(IDR,
                                               f"\n{'<b>'}{parse[5]}{'</b>'}\n\n{month} {week}\n" + f'<a href="https://coinmarketcap.com/currencies/{str(name)}/">CMC</a>',
                                               parse_mode='HTML', disable_web_page_preview=True)
                        await asyncio.sleep(60)
                        await sqlite_db.sql_edit_command(str(latest_id))
                        break
                    except:
                        await asyncio.sleep(60)
                        await sqlite_db.sql_edit_command(str(latest_id))
                        break

                else:
                    try:
                        # Coinmarketcap
                        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
                        parameters = {'symbol': symb}
                        headers = {'Accepts': 'application/json',
                                   'X-CMC_PRO_API_KEY': 'bdb009e3-3886-4fbf-8d13-47ebf57d62aa', }

                        session = Session()
                        session.headers.update(headers)
                        response = session.get(url, params=parameters)

                        week = json.loads(response.text)['data'][symb]['quote']['USD']['percent_change_7d']
                        if week >= 0:
                            week = (f"🔋Week {int(week)}%")
                        else:
                            week = (f"🛢Week {int(week)}%")

                        month = json.loads(response.text)['data'][symb]['quote']['USD']['percent_change_30d']
                        if month >= 0:
                            month = (f"🔋Month {int(month)}%")
                        else:
                            month = (f"🛢Month {int(month)}%")

                        name = json.loads(response.text)['data'][symb]['slug']

                        await bot.send_message(ID,
                                               f"{tweet.text}\n\n{month} {week}\n" + f'<a href="https://coinmarketcap.com/currencies/{str(name)}/">CMC</a>',
                                               parse_mode='HTML', disable_web_page_preview=True)
                        await bot.send_message(IDR,
                                               f"{tweet.text}\n\n{month} {week}\n" + f'<a href="https://coinmarketcap.com/currencies/{str(name)}/">CMC</a>',
                                               parse_mode='HTML', disable_web_page_preview=True)
                        await asyncio.sleep(60)
                        await sqlite_db.sql_edit_command(str(latest_id))
                        break
                    except:
                        await asyncio.sleep(60)
                        await sqlite_db.sql_edit_command(str(latest_id))
                        break
                await asyncio.sleep(60)
            await asyncio.sleep(60)
        await asyncio.sleep(60)


# Handlers
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state=None)
