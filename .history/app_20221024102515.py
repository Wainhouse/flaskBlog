from .website import create_app


# -- Create the Flask APP
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)