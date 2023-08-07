# Tips

## app.py file

### @app.route("/", methods=["GET","POST"], endpoint=endpoint_name)

You create all the different routes to the different windows of the website.
In it, you create the function for what you want in your page.

#### Methods :

GET is used for requesting data from the server, and the data is sent as query parameters in the URL. POST is used for submitting data to the server, and the data is sent in the request body.

## Render_template

In a new folder "templates", html pages are created to work on the visuals of the webpage (color, size, location...)

To run the app, go to the directory where app.py is and in command prompt : flask run

"flask route" : gives the list of all possibles routes/links

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
