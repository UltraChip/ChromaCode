# ChromaCode
Repository for the ChromaCode system

# What the hell is this?
ChromaCodes are kind of like QR codes – it’s an image comprised of a grid of squares, and data is encoded in to those squares. Where ChromaCodes differ, however, is that the data is encoded in to the color of the square, instead of just a binary black & white grid.

# Ok but… why?
Originally I was trying to create a “better” QR code with a higher data density. Theoretically ChromaCodes should be denser since each individual square encodes up to 3 bytes of data (as opposed to a QR code where each square only encodes a single bit). In reality though I was never able to make the system reliable enough to actually be useful. However, I still think the codes look kind of cool so I decided to package up the source code and share ChromaCodes with the world as a novelty.

# Why are the first three squares always so brightly colored? 
This is a leftover artifact from back when I was trying to make a QR-code competitor. Those first three squares are “calibration squares” - they are always perfectly red, perfectly green, and perfectly blue and don’t actually encode any message data. The idea was that if a user was trying to use a smartphone camera or something to read a printed ChromaCode, the software could use those three squares as a reference point to compensate for different lighting and photo quality and what not. 

# Can you go in to more technical detail on how this all works?
To a computer, every color is a mixture of the three primary colors Red, Green, and Blue (RGB). To represent this mixture the computer stores how “intense” each primary color is as a single byte – a Red byte, a Green byte, and a Blue byte. For example, a pure purple will have its Red and Blue bytes maxed out to 255* while its Green byte will be at 0. Therefore, the color purple’s RGB value is 255,0,255 (or, if you’re viewing it in hexadecimal, #FF00FF).
Text is also viewed as numerical byte values – each byte represents a single character, and the number in that byte determines what the character is, according to a standardized table. There’s a few different character-mapping tables out there, but ChromaCode uses one of the more traditional ones: ASCII. For example, let’s take the three letters “abc”. According to the ASCII table, those letters have the numerical values of 97, 98, and 99. 
What the ChromaCode encoder does is take your input text, break it up in to three-character groups, and then use those groups as RGB values to color the squares on the grid. The decoder does the opposite process: it looks at the RGB values of each square, converts those values to ASCII character groups, then concatenates all the groups together in to the original text. 

# How do I make my own ChromaCodes?
The encoder and decoder scripts are released as open source so feel free to download and run them yourself if you’d like to play around with your own ChromaCodes. To make the scripts run you’ll need to have Python3 installed along with the PyGame library. 

# Why is your source code so terrible?
I’m an amateur coder at best, and one of the reasons I wrote ChromaCode in the first place (aside from the whole QR-killer thing) was to get a better handle on how Python works. The code is fully open source so if you know a way to improve it feel free to help!
