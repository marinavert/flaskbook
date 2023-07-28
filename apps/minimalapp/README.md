# Tips

## app.py file

### @app.route("/", methods=["GET","POST"], endpoint=endpoint_name)

You create all the different routes to the different windows of the website.
In it, you create the function for what you want in your page.

#### Methods :

GET is used for requesting data from the server, and the data is sent as query parameters in the URL. POST is used for submitting data to the server, and the data is sent in the request body.

## Render_template

In a new folder "templates", html pages are created to work on the visuals of the webpage (color, size, location...)
