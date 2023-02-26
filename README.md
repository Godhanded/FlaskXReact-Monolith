# A Python Flask and React Monolithic WebApp


## My Boiler plate code to use React@18 directly with Flask templates and flask-jinja2

***note: styles not set up yet***

## Python Server setup

* Edit database uri in [config.py file](config.py)

* run ```
    pip install -r requirements.txt
        ```

* main entry point is [app.py](app.py) data is sent to template using data kwarg in render_template,


## React Template setup

* in top level run ```
                        yarn   
                    ```
* ```npm install -g sass```


## starting up the webApp

> run in first terminal
* ``` yarn build``` 
to precompile react into [flask static files](./static/bundle.js)

> run in second terminal
* ```FLASK_DEBUG=true flask run```

App will be hosted on port 5000 of your localhost