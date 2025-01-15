from aiogram import types, Dispatcher,Bot,executor

from my_buttons import main_menu
from my_buttons import awqat_menu
from my_buttons import pizzas
from my_buttons import lavashs
from my_buttons import sushis
from my_buttons import burgers
from my_buttons import drinks

api = '7726712436:AAGTPNCsugPl8my5FZI4Y9PviIMDhJHkkcY'  
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text=f'Assalamu aleykum {sms.from_user.first_name}',
                     reply_markup=main_menu)

@dp.message_handler(text='🍲Tagamlar🍲')
async def awqats(sms:types.Message):
    await sms.answer(text='Awqatlar',
                     reply_markup=awqat_menu)

@dp.message_handler(text='🥤Ishimlikler🥤')
async def dr(sms:types.Message):
    await sms.answer(text='Ishimlikler',
                     reply_markup=drinks)

@dp.callback_query_handler()
async def sss(call:types.CallbackQuery):
    data=call.data

    #Pizza menyu
    if data=='joni':
        await call.answer(text='Siz pizza zakaz berdiniz!')
        await call.message.answer(
            text="Siz tomendegi pizzalardan birin sayalasaniz boladi:",
            reply_markup=pizzas)
        
    if data=='p':
        await call.answer(text='Suwret jiberilip atir!')
        image1=open(file='lesson4/Без названия.jfif',mode='rb')
        await call.message.answer_photo(
            photo=image1,
            caption='🍕Pepperoni 50 000 swm')
    
    if data=='m':
        await call.answer(text='Suwret jiberilip atir!')
        image2=open(file='lesson4/Без названия (1).jfif',mode='rb')
        await call.message.answer_photo(
            photo=image2,
            caption='🍕Margarita 60 000 swm')
    
    if data=='pi':
        await call.answer(text='Suwret jiberilip atir!')
        image3=open(file='lesson4/4-cheese-1300x868.jpg',mode='rb')
        await call.message.answer_photo(
            photo=image3,
            caption='🍕Tort xil pishloq 75 000 swm')
        
    if data=='mi':
        await call.answer(text='Suwret jiberilip atir!')
        image4=open(file='lesson4/4-stagioni.jpg',mode='rb')
        await call.message.answer_photo(
            photo=image4,
            caption='🍕Tort mavsum 70 000 swm')
        

    # Lavash menyu
    if data=='lav':
        await call.answer(text='Siz lavash zakaz berdiniz!')
        await call.message.answer(
            text="Siz tomendegi lavashlardan sayalasaniz boladi:",
            reply_markup=lavashs)
        
    if data=='tlav':
        await call.answer(text='Suwret jiberilip atir!')
        imageb1=open(file='lesson4/tandir.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb1,
            caption='🌯Tandir lavash 29 0000 swm')
    
    if data=='talav':
        await call.answer(text='Suwret jiberilip atir!')
        imageb1=open(file='lesson4/tovuq.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb1,
            caption='🌯Tovuq lavash 26 000 swm')
    
    if data=='olavash':
        await call.answer(text='Suwret jiberilip atir!')
        imageb1=open(file='lesson4/katta lav.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb1,
            caption='🌯Original katta lavash 34 0000 swm')
        
    if data=='kichiklav':
        await call.answer(text='Suwret jiberilip atir!')
        imageb1=open(file='lesson4/kichiklav.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb1,
            caption='🌯Original kichik lavash 23000 swm')
    

    # Sushi menyu
    if data=='suh':
        await call.answer(text='Siz sushi zakaz berdiniz!')
        await call.message.answer(
            text="Siz tomendegi sushilerdan sayalasaniz boladi:",
            reply_markup=sushis)
        
    if data=='sp':
        await call.answer(text='Suwret jiberilip atir!')
        images1=open(file='lesson4/Chirashizushi.jfif',mode='rb')
        await call.message.answer_photo(
            photo=images1,
            caption='🍣Chirashizushi 45 000 swm')
        
    if data=='sm':
        await call.answer(text='Suwret jiberilip atir!')
        images2=open(file='lesson4/Inarizushi.jfif',mode='rb')
        await call.message.answer_photo(
            photo=images2,
            caption='🍣Inarizushi 40 000 swm')
        
    if data=='spi':
        await call.answer(text='Suwret jiberilip atir!')
        images3=open(file='lesson4/Makizushi.jfif',mode='rb')
        await call.message.answer_photo(
            photo=images3,
            caption='🍣Makizushi 50 000 swm')


    # Burger menyu
    if data=='bur':
        await call.answer(text='Siz burger zakaz berdiniz!')
        await call.message.answer(
            text="Siz tomendegi burgerlerden sayalasaniz boladi:",
            reply_markup=burgers)
        

    if data=='ss':
        await call.answer(text='Suwret jiberilip atir!')
        imageb1=open(file='lesson4/cheeseburger.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb1,
            caption='🍔Cheese burger 25 000 swm')


    if data=='gam':
        await call.answer(text='Suwret jiberilip atir!')
        imageb2=open(file='lesson4/gamburger.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb2,
            caption='🍔Gamburger 30 000 swm')


    if data=='big':
        await call.answer(text='Suwret jiberilip atir!')
        imageb3=open(file='lesson4/bigburger.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageb3,
            caption='🍔Big burger 35000 swm')


    if data=='pepsi':
        await call.answer(text='Suwret jiberilip atir!')
        imagepepsi=open(file='lesson4/pepsi.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imagepepsi,
            caption='🥤Pepsi 1.5l 13 000 swm')
    if data=='coca':
        await call.answer(text='Suwret jiberilip atir!')
        imagecocacola=open(file='lesson4/coca cola.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imagecocacola,
            caption='🥤Caca Cola 1.5l 12 000 swm')
    if data=='chay':
        await call.answer(text='Suwret jiberilip atir!')
        imagetea=open(file='lesson4/chay.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imagetea,
            caption='🫖Chay 5000 swm')
    if data=='kofe':
        await call.answer(text='Suwret jiberilip atir!')
        imagecofe=open(file='lesson4/coffee.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imagecofe,
            caption='☕️Kofe 7000 swm')
    if data=='sut':
        await call.answer(text='Suwret jiberilip atir!')
        imageayran=open(file='lesson4/ayran.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imageayran,
            caption='🥛Ayran 5000 swm')
    if data=='moxito':
        await call.answer(text='Suwret jiberilip atir!')
        imagemox=open(file='lesson4/moxito.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imagemox,
            caption='🍹Moxito 10 000 swm')
    if data=='tayl':
        await call.answer(text='Suwret jiberilip atir!')
        imagekoktayl=open(file='lesson4/coctail.jfif',mode='rb')
        await call.message.answer_photo(
            photo=imagekoktayl,
            caption='🍸Koktayl 15 000 swm')


# Menyuga qaytiw knopkasi
@dp.message_handler(text='Menuga qaytiw')
async def backs(sms:types.Message):
    await sms.answer(text='Menuga qayttiniz!',
                     reply_markup=main_menu)


# Contacts knopkasi
@dp.message_handler(text='📱Contacts📱')
async def kontakts(sms:types.Message):
    await sms.answer(text=f'Biz biz baylanis ushin:\nAdminstrator Tel:+998932452314')


# Biz haqqimizda knopkasi
@dp.message_handler(text='Biz haqqimizda!')
async def o(sms:types.Message):
    await sms.answer(text="Bizin restoranimiz 2022-jildan baslap is juritip\
 kelmekte.\nBizin restoranimizdin Nokis qalasinda 3 filiali bar.")


if __name__=='__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)
