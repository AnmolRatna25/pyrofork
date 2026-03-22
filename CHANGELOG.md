# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Added `style` and `icon_custom_emoji_id` support to `KeyboardButton`.
- Available `ButtonStyle` colors: `PRIMARY` (blue), `DANGER` (red), `SUCCESS` (green).

### Example Usage

```python
from pyrogram import Client, enums
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup

app = Client("my_account")


@app.on_message()
async def send_styled_keyboard(client, message):
	keyboard = ReplyKeyboardMarkup(
		[
			[
				KeyboardButton(
					text="Confirm",
					style=enums.ButtonStyle.SUCCESS,
					icon_custom_emoji_id=5368324170671202286,
				)
			]
		],
		resize_keyboard=True,
	)

	await message.reply("Choose an option:", reply_markup=keyboard)


app.run()
```

### Recommended Private Message Filter Pattern

Prefer filtering command-like messages directly in the decorator:

```python
@Client.on_message(filters.private & filters.text & filters.incoming & filters.regex(r"^(?!/)"))
async def pm_search(client, message):
	...
```

Instead of handling command exclusion inside the function body:

```python
@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_search(client, message):
	if str(message.text).startswith('/'):
		return
	...
```

Why this is better:
- The handler is triggered only for intended messages, so fewer unnecessary calls happen.
- Filtering at decorator level keeps handler logic cleaner and easier to read.
- It reduces repeated guard checks across multiple handlers.
- It avoids accidental processing when early-return checks are missed during refactors.

### on_callback_query Group Example

Use `group` when you want deterministic handler execution order for callback queries.
Lower group numbers run first, which helps you split logic into clear stages:
- `group=0`: high-priority handlers (admin actions, security checks, strict filters)
- `group=1+`: fallback or general handlers

This pattern avoids overlapping handler logic, reduces accidental double-processing,
and makes large bots easier to maintain as callback flows grow.

```python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_callback_query(filters.regex("^admin:"), group=0)
async def handle_admin_callbacks(client, callback_query):
	await callback_query.answer("Admin callback handled")


@app.on_callback_query(group=1)
async def handle_other_callbacks(client, callback_query):
	await callback_query.answer("Fallback callback handler")


app.run()
```

### InlineKeyboardButton Example

Use inline keyboard buttons when you want callback-based interactions directly under a message.

```python
from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client("my_account")


@app.on_message()
async def send_inline_keyboard(client, message):
	keyboard = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Open Docs",
					url="https://pyroratna.ratna.pw",
					style=enums.ButtonStyle.PRIMARY,
					icon_custom_emoji_id=5368324170671202286,
				),
				InlineKeyboardButton(
					"Delete",
					callback_data="delete",
					style=enums.ButtonStyle.DANGER,
					icon_custom_emoji_id=5368324170671202286,
				),
			]
		]
	)

	await message.reply("Choose an action:", reply_markup=keyboard)


@app.on_callback_query()
async def handle_inline_callbacks(client, callback_query):
	if callback_query.data == "delete":
		await callback_query.answer("Delete action confirmed")


app.run()
```
