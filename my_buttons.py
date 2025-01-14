from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

# 🗒Bas menyu🗒
main_menu=ReplyKeyboardMarkup(resize_keyboard=True)
menu=KeyboardButton(text='🍲Tagamlar🍲')
ishimlikler=KeyboardButton(text='🥤Ishimlikler🥤')
biz=KeyboardButton(text='Biz haqqimizda!')
contact=KeyboardButton(text='📱Contacts📱')
main_menu.add(menu,ishimlikler)
main_menu.add(biz)
main_menu.add(contact)


# 🍲Tagamlar🍲 menyu
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
awqat_menu=InlineKeyboardMarkup(inline_keyboard=True)
lavash=InlineKeyboardButton(text='🌯Lavash🌯',
                            callback_data='lav')
burger=InlineKeyboardButton(text='🍔Burger🍔',
                            callback_data='bur')
pizza=InlineKeyboardButton(text='🍕pizza🍕',
                           callback_data='joni')
sushi=InlineKeyboardButton(text='🍣sushi🍣',
                           callback_data='suh')
awqat_menu.add(lavash,burger)
awqat_menu.add(pizza,sushi)


# 🍕pizza🍕 menyu
pizzas=InlineKeyboardMarkup(inline_keyboard=True)
o=InlineKeyboardButton(text='🍕Pepperoni',
                       callback_data='p')
t=InlineKeyboardButton(text='🍕Margarita',
                       callback_data='m')
th=InlineKeyboardButton(text="🍕To'rt xil pishloq",
                        callback_data='pi')
f=InlineKeyboardButton(text="🍕Tort mavsum",
                       callback_data='mi')
pizzas.add(o,t)
pizzas.add(th,f)



# 🍣sushi🍣 menyu
sushis=InlineKeyboardMarkup(inline_keyboard=True)
so=InlineKeyboardButton(text='🍣Chirashizushi',
                       callback_data='sp')
st=InlineKeyboardButton(text='🍣Inarizushi',
                       callback_data='sm')
sth=InlineKeyboardButton(text="🍣Makizushi",
                        callback_data='spi')
sushis.add(so,st)
sushis.add(sth)


# 🌯Lavash🌯 menyu
lavashs=InlineKeyboardMarkup()
tandirli=InlineKeyboardButton(text='🌯Tandir lavash',
                              callback_data='tlav')

tovuqlavash=InlineKeyboardButton(text='🌯Tovuq lavash',
                                 callback_data='talav')

kattalavash=InlineKeyboardButton(text='🌯Original katta lavash',
                                 callback_data='olavash')
kichiklavash=InlineKeyboardButton(text='🌯Original kichik lavash',
                                  callback_data='kichiklav')

lavashs.add(tandirli,tovuqlavash)
lavashs.add(kattalavash,kichiklavash)


# 🍔Burger🍔 menyu
burgers=InlineKeyboardMarkup()
chess=InlineKeyboardButton(text='Cheese Burger',
                           callback_data='ss')
gam=InlineKeyboardButton(text='Gamburger',
                         callback_data='gam')
big=InlineKeyboardButton(text='Big burger',
                         callback_data='big')
free=InlineKeyboardButton(text='Free Burger',
                          callback_data='free')
burgers.add(chess,big)
burgers.add(gam,free)



drinks=InlineKeyboardMarkup()

pepsi=InlineKeyboardButton(text='🥤Pepsi🥤',
                           callback_data='pepsi')
cola=InlineKeyboardButton(text='🥤Coca Cola🥤',
                          callback_data='coca')
tea=InlineKeyboardButton(text='🫖Chay🫖',
                         callback_data='chay')
coffee=InlineKeyboardButton(text='☕️Kofe☕️',
                            callback_data='kofe')
gas_water=InlineKeyboardButton(text='🥛Ayran🥛',
                               callback_data='sut')
moxito=InlineKeyboardButton(text='🍹Moxito🍹',
                            callback_data='moxito')
coctail=InlineKeyboardButton(text='🍸Koktayl🍸',
                             callback_data='tayl')
drinks.add(pepsi,cola,gas_water)
drinks.add(coffee,tea,moxito)
drinks.add(coctail)