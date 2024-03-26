from tkinter import *
import random
from tkinter.ttk import Combobox
import re


def select_option(event):
    for widget in root.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()
    selected = combobox.get()
    options[selected]()


def password_generation():
    all_symbols = list('qwertyuiopasdfghjklzxcvbnm')
    check_toggles = [False, False, False]

    frame = Frame(root)
    frame.pack()

    var_digits = BooleanVar()
    checkbox_digits = Checkbutton(frame, text='digits', variable=var_digits,
                                  command=lambda: on_checkbox_toggle(all_symbols, check_toggles, var_digits, 0))
    checkbox_digits.pack(pady=(10, 1), padx=(0, 43))

    var_upper = BooleanVar()
    checkbox_upper = Checkbutton(frame, text='upper letters', variable=var_upper,
                                 command=lambda: on_checkbox_toggle(all_symbols, check_toggles, var_upper, 1))
    checkbox_upper.pack(pady=(1, 1), padx=(0, 5))

    var_spec = BooleanVar()
    checkbox_spec = Checkbutton(frame, text='spec symbols', variable=var_spec,
                                command=lambda: on_checkbox_toggle(all_symbols, check_toggles, var_spec, 2))
    checkbox_spec.pack(pady=(1, 10))

    Label(frame, text='Input symbols count').pack()

    entry = Entry(frame, justify='center', width=40, border='4')
    entry.insert(0, '8')
    entry.pack(pady=10)

    button = Button(frame, width=10, text='generate',
                    command=lambda: gen_passwords(all_symbols, label, text_widget, entry))
    button.pack(pady=(10, 20))

    label = Label(frame, text='Your generated passwords:\n\n')
    label.pack()

    text_widget = Text(frame, width=35, height=11)
    text_widget.pack()


def change_symbols(check_toggles):
    match check_toggles:
        case [True, False, False]:
            return list('qwertyuiopasdfghjklzxcvbnm1234567890')
        case [False, True, False]:
            return list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        case [False, False, True]:
            return list('qwertyuiopasdfghjklzxcvbnm%*(!&)?@#$~')
        case [True, True, False]:
            return list('qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
        case [True, False, True]:
            return list('qwertyuiopasdfghjklzxcvbnm1234567890%*(!&)?@#$~')
        case [False, True, True]:
            return list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM%*(!&)?@#$~')
        case [True, True, True]:
            return list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM%*(!&)?@#$~1234567890')
        case [False, False, False]:
            return list('qwertyuiopasdfghjklzxcvbnm')


def gen_passwords(all_symbols, label, text_widget, entry):
    try:
        label.config(text='Your generated passwords:\n\n')
        text_widget.delete('1.0', END)
        symbol_count = int(entry.get())
        for _ in range(10):
            password = ''.join(random.choice(all_symbols) for _ in range(symbol_count))
            text_widget.insert(END, f'{password}\n')
    except Exception:
        label.config(text='Input number\n\n')


def on_checkbox_toggle(all_symbols, check_toggles, var, index):
    if var.get():
        check_toggles[index] = True
        all_symbols.clear()
        all_symbols.extend(change_symbols(check_toggles))
    else:
        check_toggles[index] = False
        all_symbols.clear()
        all_symbols.extend(change_symbols(check_toggles))


def word_to_password():
    all_symbols = []
    check_toggles = [False, False, False]

    frame = Frame(root)
    frame.pack()

    var_digits = BooleanVar()
    checkbox_digits = Checkbutton(frame, text='digits', variable=var_digits,
                                  command=lambda: on_checkbox_toggle_word(all_symbols, check_toggles, var_digits, 0))
    checkbox_digits.pack(pady=(10, 1), padx=(0, 43))

    var_upper = BooleanVar()
    checkbox_upper = Checkbutton(frame, text='upper letters', variable=var_upper,
                                 command=lambda: on_checkbox_toggle_word(all_symbols, check_toggles, var_upper, 1))
    checkbox_upper.pack(pady=(1, 1), padx=(0, 5))

    var_spec = BooleanVar()
    checkbox_spec = Checkbutton(frame, text='spec symbols', variable=var_spec,
                                command=lambda: on_checkbox_toggle_word(all_symbols, check_toggles, var_spec, 2))
    checkbox_spec.pack(pady=(1, 10))

    Label(frame, text='Input words').pack()

    entry = Entry(frame, justify='center', width=40, border='4')
    entry.pack(pady=10)

    button = Button(frame, width=10, text='generate',
                    command=lambda: gen_password_word(text_widget, entry, all_symbols, check_toggles))
    button.pack(pady=(10, 20))

    label = Label(frame, text='Your generated passwords:\n\n')
    label.pack()

    text_widget = Text(frame, width=35, height=11)
    text_widget.pack()

    clear_button = Button(frame, width=10, text='clear', command=lambda: clear_text(text_widget))
    clear_button.pack(pady=10)


def gen_password_word(text_widget, entry, all_symbols, check_toggles):
    if check_toggles != [False, False, False] and not entry.get().isspace():
        word = entry.get()
        if ' ' in word:
            word = ''.join(letter for letter in word if letter != ' ')

        password = ''
        for letter in word:
            choose = random.choice([1, 2, 3])
            if check_toggles == [False, True, False]:
                if choose == 1:
                    password += f'{letter.upper()}'
                else:
                    password += f'{letter}'
            elif choose == 1:
                password += f'{letter}{random.choice(all_symbols)}'
            elif choose == 3 and check_toggles[1]:
                password += f'{letter.upper()}'
            else:
                password += f'{letter}'

        text_widget.insert(END, f'{password}\n')


def clear_text(text_widget):
    text_widget.delete('1.0', END)


def on_checkbox_toggle_word(all_symbols, check_toggles, var, index):
    if var.get():
        check_toggles[index] = True
        all_symbols.clear()
        all_symbols.extend(additional_symbols(check_toggles))
    else:
        check_toggles[index] = False
        all_symbols.clear()
        all_symbols.extend(additional_symbols(check_toggles))


def additional_symbols(check_toggles):
    match check_toggles:
        case [True, False, False] | [True, True, False]:
            return list('1234567890')
        case [False, False, True] | [False, True, True]:
            return list('%*(!&)?@#$~')
        case [True, False, True] | [True, True, True]:
            return list('1234567890%*(!&)?@#$~')
        case [False, False, False] | [False, True, False]:
            return list('')


def check_password():
    frame = Frame(root)
    frame.pack()

    Label(frame, text="Let's check your password").pack(pady=10)

    entry = Entry(frame, justify='center', width=40, border='4')
    entry.pack(pady=10)

    button = Button(frame, width=10, height=2, text='Check', command=lambda: checking(entry, label))
    button.pack(pady=10)

    label = Label(frame)
    label.pack()


def checking(entry, label):
    password = entry.get()
    if password:
        pattern = r'(?=.*[a-zA-Z])(?=.*\d)(?=.*[^\w\s])'
        if len(password) < 8:
            label.config(text='Password is not a stong\n\nPassword length must be >= 8')
        elif re.search(pattern, password):
            label.config(text='Your password is strong')
        else:
            label.config(text='Password is not a stong\n\nPassword must contain a-z, A-Z, 0-9 and spec symbol')


root = Tk()
root.title('Password generator')
root.geometry('500x600')

difficulties = ['Password generation', 'Word to password', 'Check password']
selected_option = StringVar()
selected_option.set("Password generation")
combobox = Combobox(root, textvariable=selected_option, values=difficulties)
combobox.pack()
combobox.bind('<<ComboboxSelected>>', select_option)

options = {
    'Password generation': password_generation,
    'Word to password': word_to_password,
    'Check password': check_password
}

password_generation()

print(n)




