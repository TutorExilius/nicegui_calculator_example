from nicegui import ui

# Calculator Logic ---
class Calculator:
    def __init__(self):
        self.output = "0"
        self.operators = []
        self.operands = []

    def calculate(self):
        self.parse_input()

        while len(self.operands) > 1:
            operand_1 = int(self.operands.pop(0))
            operand_2 = int(self.operands.pop(0))
            operator = self.operators.pop(0)

            if operator == "+":
                result = operand_1 + operand_2
            elif operator == "-":
                result = operand_1 - operand_2
            elif operator == "*":
                result = operand_1 * operand_2
            elif operator == "/":
                result = operand_1 / operand_2

            self.operands.insert(0, str(result))

        self.output = self.operands[0]
        self.operands.clear()

    def parse_input(self):
        output_entries = list(self.output)

        while output_entries:
            char = output_entries.pop(0)

            if char in ["+", "-", "*", "/"]:
                self.operators.append(char)
            else:
                result = self.collect_whole_number(output_entries)

                if result is not None:
                    number_input = char + result
                else:
                    number_input = char

                self.operands.append(number_input)

    def collect_whole_number(self, output_entries):
        one_number = ""

        while output_entries:
            char = output_entries.pop(0)

            if char.isdigit():
                one_number = one_number + char
            else:
                output_entries.insert(0, char)
                return one_number

    def clear(self):
        self.output = "0"
        self.operators.clear()
        self.operands.clear()

    def append_input(self, event):
        if self.output == "0":
            self.output = event.sender.text
        else:
            self.output = self.output + event.sender.text
# ---


# Create a calculator object based on Calculator class above
calculator = Calculator()


# Build our UI ----
# Labels: 'Result' and '0' (initial value)
with ui.row():
    ui.label("Result:")
    ui.label().bind_text(calculator, "output")

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
