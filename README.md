# 💎 emoji_diamond

A fun and educational Python package that draws randomized emoji diamond patterns!
Built for everyone — including mobile-first coders using Termux or Pydroid 3.



# 🔧 Installation

Install directly from PyPI:

```
pip install emoji-diamond
```



## ✅ Mobile Setup


**In Pydroid 3:**

1. Open the app.


2. Tap the ☰ menu → Pip.


3. Run:

```
pip install emoji-diamond
```


**In Termux:**

Make sure Python is installed, then run:

```
pip install emoji-diamond

OR

pip install emoji-diamond==0.1
```

# 🧠 How It Works


## To draw a diamond:

1. Import the class


2. Pass a number into the class


3. Call .diamond() to draw


4. Use .author() and .info() to get extra information




## ✨ Usage Example

```python


from emoji_diamond.stars import Shape
# Step 1: Import


pattern = Shape(4)
# Step 2: Create the object with 4 as input


pattern.diamond()
# Step 3: Draw the diamond


pattern.author()
# Step 4 (optional): Show author info


pattern.info()
# Step 5 (optional): Show diamond info
```


# 🔄 Random Emoji Feature

Each diamond is drawn using random emojis selected from a built-in list of over 200 emojis. 🤙🏽😍🇬🇭

That means:

Every time you run .diamond(), the diamond will look a little different

The emoji used is randomly chosen and may vary from stars to hearts, animals, food, shapes, and more!


You don’t have to configure anything , just enjoy the surprise!

Example:

```
      🐍
    🐍🐍🐍
  🐍🐍🐍🐍🐍
    🐍🐍🐍
      🐍
```

Then next time it might be:

```
      ❤️ 
    ❤️❤️❤️
  ❤️❤️❤️❤️❤️
    ❤️❤️❤️
      ❤️
```



# 🧾 What Each Part Does


## 🔹 Shape(number)

This is the class constructor. You pass in a single number that represents how many rows the diamond should have from the middle to the top.

The total rows of the diamond are calculated automatically using:

```
total_rows = number * 2 - 1


So:

Shape(3) → 5 rows

Shape(4) → 7 rows

Shape(5) → 9 rows
And so on...
```


## 🔹 .diamond()

This is the main method that draws the diamond shape using a random emoji.

It prints directly in the console or terminal.

```
pattern = Shape(3)
pattern.diamond()
```


## 🔹 .Author()

Returns the author and branding:

**Powered by Oligotech 🇬🇭**


## 🔹 .info()

Returns helpful info based on your input:

This diamond has 3 rows from the middle upwards.



## 💻 Example Output (All in One)

```
from emoji_diamond.stars import Shape

pattern = Shape(3)
pattern.diamond()
pattern.info()
pattern.Author()


*Output:*

     🐙
   🐙🐙🐙
 🐙🐙🐙🐙🐙
   🐙🐙🐙
     🐙

This diamond has 3 rows from the middle upwards.

**Powered by Oligotech 🇬🇭**
```


# 🌍 Author

Made in Ghana 🇬🇭 by [Oligotech](https://t.me/OligoTech)
For support, bug reports, or ideas: visit the GitHub repository or message on social media.


# 📱 Built for Mobile Developers

This package works beautifully even on phones, with tools like:

✅ Termux

✅ Pydroid 3

✅ QPython

✅ Juno

✅ Google Colab (for visual test outputs)


# 📄 License

MIT License — free for use, distribution, and modification.


# 📌 Summary

Feature	Usage

Import class	from emoji_diamond.stars import Shape
Create shape	pattern = Shape(4)
Draw diamond	pattern.diamond()
Random emoji	Built-in feature (200+ emojis)
Show author	pattern.Author()
Get info	pattern.info()
