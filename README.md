# Python captcha-server
## What it can do?

This server can provide captcha(generated itself). And check your answer on it.

## How to work with it?

To get captcha, send GET request on the server.py(in example it was localhost:8080). To answer it, send POST request on the same address with field answer='your_code'. Response will show your result.

Time is limited by 30 seconds. There is no auth(thinking about it)

## Example

You can see example of client in /client. `client.py` sends GET request and creates a form HTML-page to send POST
