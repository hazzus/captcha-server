# Python captcha-server
## What it can do?

This server can provide captcha(generated itself). And check your answer on it.

## How to work with it?
Of course you need to run `server.py`

To get captcha, send GET request on the server.py(in example it was localhost:8080). To answer it, send POST request on the same address with field answer='your_code'. Response will show your result.

Time is limited by 30 seconds. There is no auth(TODO)

## Example
### Usage examples
You can see example of client in /client. `client.py` sends GET request and creates a form HTML-page to send POST.  
This implemntation is quite bad but I only create server and "do not care" about client system.
### Captcha examples
#### 2zpc
![2zpc](captcha%20examples/2zpc.png)
#### jrjzy  
![jrjzy](captcha%20examples/jrjzy.png)  
#### veghsj
![veghsj](captcha%20examples/veghsj.png)

## Captcha class
Actually difficulties were while creating `captcha` class in `captha.py`  
Usage of this class:
* Firstly import captcha:  
`from captcha import captcha`
* Now you can create captcha with this code:  
`cp = captcha()`  
    * Constructor of captcha will create captcha code and image
    * You can get image:  
        `cp.get_image()`  
      Actually calls `clear_image()`  
    * To get code:  
        `cp.get_code()`
    * To clear image:  
        `cp.clear_image()`  
    Actually I need to create destructor and some other features like re-create captcha, but this is `TODO`)