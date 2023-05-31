# 313 Sprite Sheets

Objectives
* Use a sprite sheet to collect images for animation
* Incorporate an image object in a canvas
* Update the image using tkCanvas.itemconfig
* Use the tkObject.after() method to schedule functions

Introduction
Sprites are computer graphics that can be moved and manipulated on screen.  Today we will look at incorporating sprites that are taken from a sprite sheet.  A sprite sheet is a collection of images that generally represent one character. By rapidly changing between images, we can give the impression of animation, much like using a flip book.

Watch this video about sprites and sprite sheets:
https://www.youtube.com/watch?v=F4lptpFSB_I

The process of animation follows a plan like this:
1. Load several images into memory as a list
2. Display one of those images as the canvas object images
3. Set a timeout or interval, after which we run a function to change the image
4. We track the state of the image, and decide which is the next image to display based on what the current image is.
5. In the function, we set another interval to change the image again.

We will use the tkObject.after() method to set the timeout or interval time and function to run.

Task 1
Changing Sprites
Create a canvas where you can move a skeleton (taken from skt.png) using the arrow keys.  You can use the code in the example1.py file to help you choose which images to use for your sprite.
Have the skeleton change to face the direction in which it is moving. You will not be using tk.after() for this, but instead include the image change with tk.itemconfig in your key bindings.

Task 2
Animating Sprites
Repeat Task 1, but this time, include an animated sprite.  This will incorporate some of the code in your example1 file with the code from task1.
