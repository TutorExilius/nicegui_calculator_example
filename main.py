from nicegui import ui

# Calculator Logic ---
class Calculator:
    def __init__(self):
        self.output = ""

    def calculate(self):
        self.output = eval(self.output)

    def clear(self):
        self.output = ""

    def append_input(self, event):
        self.output = self.output + event.sender.text
# ---


# Create a calculator object based on Calculator class above
calculator = Calculator()


# Build our UI ----
# Labels: 'Result' and '0' (initial value)
with ui.row():
    ui.label().bind_text(calculator, "output").style(
        "text-align: right; padding: 2px 8px; height: 30px; width: 210px; border: 1px solid black;"
    )

# Buttons: '1' , '2', '3' and '+'
with ui.row():
    ui.button("1", on_click=calculator.append_input).style("width: 40px;")
    ui.button("2", on_click=calculator.append_input).style("width: 40px;")
    ui.button("3", on_click=calculator.append_input).style("width: 40px;")
    ui.button("+", on_click=calculator.append_input).style("width: 40px;")

# Buttons: '4' , '5', '6' and '-'
with ui.row():
    ui.button("4", on_click=calculator.append_input).style("width: 40px;")
    ui.button("5", on_click=calculator.append_input).style("width: 40px;")
    ui.button("6", on_click=calculator.append_input).style("width: 40px;")
    ui.button("-", on_click=calculator.append_input).style("width: 40px;")

# Buttons: '7' , '8', '9' and '*'
with ui.row():
    ui.button("7", on_click=calculator.append_input).style("width: 40px;")
    ui.button("8", on_click=calculator.append_input).style("width: 40px;")
    ui.button("9", on_click=calculator.append_input).style("width: 40px;")
    ui.button("*", on_click=calculator.append_input).style("width: 40px;")

# Buttons: '0' , '=', 'CLR' and '/'
with ui.row():
    ui.button("0", on_click=calculator.append_input).style("width: 40px;")
    ui.button("=", on_click=calculator.calculate).style("width: 40px;")
    ui.button("CLR", on_click=calculator.clear).style("width: 40px;")
    ui.button("/", on_click=calculator.append_input).style("width: 40px;")
# ----


# Run NiceGUI App
ui.run()
