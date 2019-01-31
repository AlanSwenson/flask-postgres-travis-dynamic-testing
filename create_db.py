# This must be contained in a function so we can call it with Zappa
def db_init():
    from project import create_app, db

    app = create_app()
    app.app_context().push()

    from project.models.model1 import Model1

    # if you have more models just add them here
    # from project.models.model2 import Model2
    # from project.models.lots_of_models import Model3, Model4, Model5

    db.create_all()


if __name__ == "__main__":
    db_init()
