from app.controllers.spellcheck_controller import SpellcheckController
from app.models.spellcheck_model import SpellcheckModel
from app.views.spellcheck_view import SpellcheckView


def main():
    view = SpellcheckView()
    user_input = view.get_user_input()

    model = SpellcheckModel(None, None, None, None)
    controller = SpellcheckController(view, model)
    errors = controller.validate_inputs(user_input[0], user_input[1], user_input[2], user_input[3])
    #if no error go ahear, otherwise pass them on onto the view
    print(user_input)


if __name__ == "__main__":
    main()