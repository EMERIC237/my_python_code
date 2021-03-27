from flask import Flask

app=Flask(_name_)


@app.route('/')


def home():
    

    return"Website content goes here."

if _name_=='_main_':

    app.run(debud=True)
