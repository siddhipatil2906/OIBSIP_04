# Emoji Chat App

A simple desktop chat application built with Python and Tkinter. It features a WhatsApp-inspired dark UI, a scrollable chat area, quick-access emoji buttons, and a message input field.

---

## Features

- 💬 **Chat Interface** — Displays messages in a scrollable chat window
- 😊 **Emoji Buttons** — One-click insertion of popular emojis into the message box
- 🟢 **Send Button** — Sends typed messages and appends them to the chat
- 🎨 **Dark Theme UI** — WhatsApp-inspired styling with dark background (`#121212`) and green accents
- 📜 **Auto-Scroll** — Chat automatically scrolls to the latest message

---

## Supported Emojis

| Button | Emoji |
|--------|-------|
| 😊     | Smile |
| 😂     | Laugh |
| ❤️     | Heart |
| 🔥     | Fire  |
| 👍     | Thumbs Up |

---

## Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)

> No additional packages need to be installed.

---

## Usage

```bash
python CHAT_notepad.py
```

1. Type your message in the input box at the bottom
2. Optionally click an emoji button to add an emoji to your message
3. Click **Send** or press the Send button to post the message
4. Your message appears in the chat window as `You: <message>`

---

## UI Layout

```
┌──────────────────────────┐
│    💬 Emoji Chat App     │  ← Dark green header
├──────────────────────────┤
│                          │
│  You: Hello! 😊          │  ← Chat area (light beige)
│  You: How are you? 🔥    │
│                          │
├──────────────────────────┤
│  😊  😂  ❤️  🔥  👍      │  ← Emoji buttons (dark bg)
├──────────────────────────┤
│ [Type here...] [ Send ]  │  ← Input + green Send button
└──────────────────────────┘
```

---

## Notes

- This is a **single-user** chat app — messages are only shown from your side (`You:`).
- There is no networking or backend; it is not a real multi-user chat application.
- To extend it into a real chat app, you could integrate Python's `socket` library for networking.

---

## License

This project is open source and free to use.
