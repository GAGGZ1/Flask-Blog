from flaskblog import create_app

app = create_app()

# if __name__ == '__main__':
#     app.run(debug=False,host='0.0.0.0')

if __name__ == '__main__':
    app.run(debug=True)