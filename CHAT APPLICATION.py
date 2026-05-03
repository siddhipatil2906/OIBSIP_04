from tkinter import *

def send():
    msg = entry.get()
    if msg != "":
        chat.config(state=NORMAL)
        chat.insert(END, "You: " + msg + "\n\n")
        chat.config(state=DISABLED)
        entry.delete(0, END)
        chat.see(END)

def add_emoji(emoji):
    entry.insert(END, emoji)

root = Tk()
root.title("CHATNOVA")
root.geometry("420x600")
root.config(bg="#121212")

# Header
title = Label(root, text="💬 CHATNOVA", font=("Arial",18,"bold"),
bg="#075E54", fg="white", pady=10)
title.pack(fill=X)

# Chat Area
chat = Text(root, font=("Segoe UI Emoji",12),
bg="#ECE5DD", fg="black")
chat.pack(padx=10, pady=10, fill=BOTH, expand=True)
chat.config(state=DISABLED)

# Emoji Buttons Frame
emoji_frame = Frame(root, bg="#121212")
emoji_frame.pack()

Button(emoji_frame, text="😊", font=("Arial",14),
command=lambda:add_emoji("😊")).pack(side=LEFT, padx=5)

Button(emoji_frame, text="😂", font=("Arial",14),
command=lambda:add_emoji("😂")).pack(side=LEFT, padx=5)

Button(emoji_frame, text="❤️", font=("Arial",14),
command=lambda:add_emoji("❤️")).pack(side=LEFT, padx=5)

Button(emoji_frame, text="🔥", font=("Arial",14),
command=lambda:add_emoji("🔥")).pack(side=LEFT, padx=5)

Button(emoji_frame, text="👍", font=("Arial",14),
command=lambda:add_emoji("👍")).pack(side=LEFT, padx=5)

# Bottom Input Area
bottom = Frame(root, bg="#121212")
bottom.pack(fill=X, pady=10)

entry = Entry(bottom, font=("Segoe UI Emoji",12), width=25)
entry.pack(side=LEFT, padx=10)

btn = Button(bottom, text="Send",
font=("Arial",12,"bold"),
bg="#25D366", fg="white",
command=send)
btn.pack(side=LEFT)

root.mainloop()
