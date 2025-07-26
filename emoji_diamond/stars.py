import random
import math
import time


class Shape:
    
    #constructor
    def __init__(self, rows=4):
        self.info = f"\nthis is an emoji diamond with {rows*2-1} rows"
        self.rows = rows
    
    
    #method
    def diamond(self):
        rows = 4

  

        emojis = [
    "⭐️", "🔷", "🌟", "🔴", "💛", "🖤", "🟨", "🟥", "🧿", "🟩",
    "🤍", "🔥", "💎", "❄️", "💚", "🐍", "🦋", "🌈", "🍭", "🎀",
    "💙", "💜", "❤️", "💗", "💖", "💘", "💝", "💓", "💞", "💟",
    "💐", "🌸", "🌺", "🌻", "🌼", "🌷", "🪷", "🪻", "🌹", "🌙",
    "🌞", "🌤️", "🌈", "⚡", "🌠", "🌌", "☀️", "🧡", "🕯️", "🪔",
    "🧁", "🍦", "🍨", "🍩", "🍪", "🍰", "🎂", "🧃", "🧋", "🥤",
    "🍹", "🍸", "🍷", "🥂", "🍺", "🍻", "🍾", "🎈", "🎉", "🎊",
    "🎇", "🎆", "🪅", "🎎", "🎐", "🎏", "🎀", "🪄", "💫", "🌀",
    "🛸", "🚀", "🛶", "🚁", "🦄", "🐉", "🐲", "🐬", "🐳", "🐠",
    "🦚", "🦜", "🦩", "🦋", "🪻", "🌼", "🌺", "🍉", "🍓", "🍒",
    "🍇", "🍍", "🥭", "🍌", "🍋", "🍊", "🍏", "🍎", "🍈", "🧀",
    "🥯", "🥐", "🥞", "🧇", "🍯", "🥓", "🍔", "🍟", "🌮", "🌯",
    "🍕", "🍖", "🍗", "🥗", "🥙", "🧆", "🍤", "🍣", "🍱", "🥡",
    "🍜", "🍚", "🍙", "🍛", "🍲", "🫕", "🫔", "🥠", "🧨", "🎮",
    "🎲", "🎰", "🧿", "💿", "📀", "📸", "📷", "📹", "🎥", "🎞️",
    "📺", "📻", "🎙️", "🎚️", "🎛️", "🎵", "🎶", "🎼", "🎤", "🎧",
    "🧠", "🫀", "🫁", "👁️", "👑", "💍", "👒", "🎩", "🎓", "🧢",
    "🪖", "🥻", "🧥", "🧤", "🧣", "👗", "👚", "👕", "👖", "🩳",
    "👠", "👡", "👢", "🥿", "🩴", "🩱", "👙", "🩲", "🧦", "🧸",
    "🪆", "🪡", "🧵", "🧶", "🪢", "🧳", "💼", "👜", "👝", "👛",
    "💎", "🔮", "🪞", "🪟", "🕹️", "🖼️", "🎨", "🧩", "🪄", "✨",
    "🌟", "💥", "💢", "💦", "💨", "🫧", "🕊️", "🦜", "🪸", "🪷"
]
        factor = math.floor(random.random()*(len(emojis)-1))
        random_inner = emojis[factor]
         
        for i in range(1,(self.rows+1)): 
          print("  " * (self.rows-i) + f"{random_inner}"*(2*i-1)+ " "* (self.rows-i))
    
        for i in range((self.rows-1), 0, -1):
           print("  " * (self.rows-i) + f"{random_inner}"*(2*i-1)+  " " * (self.rows-i))
          
    def Author(self):
        
            time.sleep(0.1)
            print("𝗣" , end="", flush=True)
            time.sleep(0.11)
            print("𝗼" ,  end=""  , flush=True)
            time.sleep(0.12)
            print("𝘄" ,  end="" , flush=True)
            time.sleep(0.13)
            print("𝗲"  ,  end="", flush=True)
            time.sleep(0.14)
            print("𝗿" ,  end="" , flush=True)
            time.sleep(0.15)
            print("𝗲" ,  end="" , flush=True)
            time.sleep(0.16)
            print("𝗱" , end="" , flush=True)
            time.sleep(0.17)
            print(" " ,  end="",flush=True)
            time.sleep(0.18)
            print("𝗯" ,  end="",flush=True)
            time.sleep(0.19)
            print("𝘆" ,  end="",flush=True)
            time.sleep(0.2)
            print(" " ,  end="",flush=True )
            time.sleep(0.21)
            print("𝗢",  end="",flush=True)    
            time.sleep(0.22)
            print("𝗹" ,  end="",flush=True)
            time.sleep(0.23)
            print("𝗶" ,  end="",flush=True)
            time.sleep(0.24)
            print("𝗴" ,  end="",flush=True)
            time.sleep(0.25)
            print("𝗼" ,  end="",flush=True)
            time.sleep(0.26)
            print("𝗧" , end="",flush=True)
            time.sleep(0.27)
            print("𝗲" ,  end="",flush=True)
            time.sleep(0.28)
            print("𝗰" ,  end="",flush=True)
            time.sleep(0.29)
            print("𝗵" ,  end="",flush=True)
            time.sleep(0.31)
            print(" 🇬🇭" ,end="")

