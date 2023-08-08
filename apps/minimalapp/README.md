# Tips

### Methods :

GET is used for requesting data from the server, and the data is sent as query parameters in the URL.

POST is used for submitting data to the server, and the data is sent in the request body.

## Command lines

Go to the directory where app.py is :

- flask run : run the app
- flask route : list of all possible routes in the website

## Make a minimal app

Create pages that greets with a given name, uses a template for the layout

① @app.route("/", methods=["GET","POST"], endpoint=endpoint_name)
You create all the different routes to the different windows of the website.
In it, you create the function for what you want in your page.

② Render_template : In a new folder "templates", html pages are created to work on the visuals of the webpage (color, size, location...)

③ "url_for" prints out the different routes given the value of an endpoint and needed variables

④ "current_app" represents the current application context, even if you don't have direct access to the app

⑤ "request" represents the incoming HTTP request made by a client

- Attributes:
  request.method: The HTTP method used for the request (e.g., "GET", "POST").
  request.url: The full URL of the request.
  request.headers: A dictionary containing the HTTP headers of the request.
  request.args: A dictionary containing the query parameters from the URL.
  request.form: A dictionary containing data from the request's form data (for "POST" requests).
  request.cookies: A dictionary containing cookies sent by the client.
- Methods:
  request.get(key): Get a value from the query parameters or form data.
  request.args.get(key): Get a value from the query parameters.
  request.form.get(key): Get a value from the form data.
  request.cookies.get(key): Get a value from the cookies.

## Make a form and send it by email

We want a page to answer the form (username, email, content of inquiry).
A PRG (POST/REDIRECT/GET) pattern is used.

- Show the "Contact form" page (GET)
- Send the info by email (POST)
- Redirect to "Contact complete" (REDIRECT)
- Show the "Contact complete" page (GET)

| Endpoint         | Methods   | Rule              |
| ---------------- | --------- | ----------------- |
| contact          | GET       | /contact          |
| contact_complete | GET, POST | /contact/complete |

① Request and redirect
Create "contact" and "contact_complete" endpoint, and define what to return depending on the method.

② Read the completed forms

③ Flash message and secret_key : used to give immediate feedback
"pip install email-validator" to validate the input email adresses
Check if all the fields are correctly filed. If so, the inquiry is sent by email, if not, we go back to "contact" screen to start again.
The error message appear when you click on submit button

④ Logger to keep tab of what happens
"pip install flask-debugtoolbar" to install the debugger

⑤ Send emails
"pip install flask-mail" simplifies sending emails
To send emails from a gmail account, fiest you  need to configure things
go to settings -> security -> 2-step validation -> apps passwords 
Select "others" as app and generate a password
Then, add mail config in app.py and also in .env
Finally, create a function that sends an email following a template, that must be created as well (contact_mail.txt, contact_mail.html)

⑥ Cookies, sessions and responses
