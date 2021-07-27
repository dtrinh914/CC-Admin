import app

if __name__ == '__main__':
    print("== Running in debug mode ==")
    app.create_app().run(host='localhost', port=3000, debug=True)
else:
    handler = app.create_app('PROD')
