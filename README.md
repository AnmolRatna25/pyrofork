<p align="center">
    <a href="https://github.com/AnmolRatna25/PyroRatnaGram">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="PyroRatnaGram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://github.com/AnmolRatna25">
        Homepage
    </a>
    •
    <a href="https://pyrofork.wulan17.dev">
        Documentation
    </a>
    •
    <a href="https://github.com/AnmolRatna25/PyroRatnaGram/issues">
        Issues
    </a>
    •
    <a href="https://t.me/RATNA_Robot">
        Support Chat
    </a>
    •
    <a href="https://t.me/official_RATNA">
        News/Releases
    </a>
</p>

## PyroRatnaGram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

``` python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from PyroRatnaGram!")


app.run()
```

**PyroRatnaGram** is a modern, elegant and asynchronous [MTProto API](https://pyrofork.wulan17.dev/main/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

If you'd like to support PyroRatnaGram, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/AnmolRatna25).
- Donate via Razorpay:

    <form><script src="https://checkout.razorpay.com/v1/payment-button.js" data-payment_button_id="pl_NU88lK67V6xLEP" async> </script> </form>

### Key Features

- **Ready**: Install PyroRatnaGram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install -U pyroratnagram
```

### Resources

- Check out the docs at https://pyrofork.wulan17.dev to learn more about PyroRatnaGram, get started right
away and discover more in-depth material for building your client applications.
- Join the official group at https://t.me/RATNA_Robot and stay tuned for news, updates and announcements.
