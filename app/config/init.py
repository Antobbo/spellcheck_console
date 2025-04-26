from app.controllers.spellcheck_controller import SpellcheckController
from app.models.spellcheck_model import SpellcheckModel
from app.views.spellcheck_view import SpellcheckView


def main():
    view = SpellcheckView()
    user_input = view.get_user_input()

    model = SpellcheckModel(None, None, None, None)
    controller = SpellcheckController(view, model)

    print(user_input)


if __name__ == "__main__":
    main()