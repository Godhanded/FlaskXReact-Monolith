# A Python Flask and React Monolithic WebApp


## My Boiler plate code to use React@18 directly with Flask templates and flask-jinja2



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

* data from the flask server is collected as props and passed to the ```<App/>``` component
* entry point is [index.html](./templates/) >> [index.js](./src/index.js)


## starting up the webApp

> run in first terminal

* ```yarn style```
to convert scss in [styles.scss](./src/styles.scss) to css in [stylesheet.scss](./static/stylesheet.css)

* ``` yarn build``` 
to precompile react into [flask static files](./static/bundle.js)


> run in second terminal
* ```FLASK_DEBUG=true flask run```

App will be hosted on port 5000 of your localhost

## django version coming soon