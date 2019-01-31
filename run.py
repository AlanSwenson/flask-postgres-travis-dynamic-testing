from project import create_app, db

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run(debug=False)
