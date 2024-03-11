# cardputer_repl
M5Stack Cardputer Virtual REPL

Copying code.py and the /lib/ folder from this repository to the M5Stack [Cardputer](https://shop.m5stack.com/products/m5stack-cardputer-kit-w-m5stamps3) will present a virtual REPL on the device keyboard when it boots. Using the FN key there are up/down/left/right keys for accessing the command line history and edit functions.  

In order to enable Cardputer keyboard input in python scripts add the following block of code to the import section of your code:
```py
try:
    from cardputer_repl import input
except:
    pass
```
The Virtual REPL will treat a file named virtcode.py in the root directory ('/') the way the native REPL treats a code.py file, that is it will be executed within the Virtual REPL when the Microcontroller is powered up or reset. When the virtcode.py program exits the Virtual REPL will take over control.
