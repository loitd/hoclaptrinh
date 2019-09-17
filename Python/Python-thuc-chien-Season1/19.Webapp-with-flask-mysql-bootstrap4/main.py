from views import app

if __name__ == "__main__":
    # debug = True to forece flask reload when code changed
    app.config.from_object('config.DevelopmentConfig')
    app.run(debug=True)
    