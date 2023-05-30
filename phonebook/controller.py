import view
import model
import text_for_user


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_file()
                view.print_message(text_for_user.load_successful)
            case 2:
                model.save_file()
                view.print_message(text_for_user.save_successful)
            case 3:
                pb = model.get_book()
                view.print_contacts(pb, text_for_user.book_empty)
            case 4:
                contact = view.input_contact()
                name = model.add_contact(contact)
                view.print_message(text_for_user.new_contact_successful(name))
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
