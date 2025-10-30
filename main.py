@staticmethod
    def add_spaces(num_str):
        if "." in num_str:
            integer, fractional = num_str.split(".")
        else:
            integer, fractional = num_str, ""
        integer = integer.replace(" ", "")
        integer_formatted = ""
        for i, digit in enumerate(reversed(integer)):
            if i != 0 and i % 3 == 0:
                integer_formatted = " " + integer_formatted
            integer_formatted = digit + integer_formatted
        if fractional:
            return integer_formatted + "." + fractional
        return integer_formatted

    def update_display(self):
        text = self.format_number(self.expression)
        self.display.text = text

    def on_click(self, char):
        # Пасхалка: 3914+×=
        if self.expression.endswith("3914+×") and char == "=":
            self.expression = "Шалунишка"
            self.error_state = True
            self.update_display()
            return

        if char == "C":
            self.expression = ""
            self.error_state = False
            self.update_display()
        elif char == "У":
            if not self.error_state:
                self.expression = self.expression[:-1]
                self.update_display()
        elif char == "=":
            if not self.error_state and self.expression.strip() != "":
                safe_expr = self.expression.replace("÷", "/").replace("×", "*").replace(",", ".")
                result = SafeCalculator.calculate(safe_expr)
                if result is None:
                    self.expression = "Ошибка"
                    self.error_state = True
                else:
                    self.expression = result
                self.update_display()
        elif char == "+/-":
            if not self.error_state and any(c.isdigit() for c in self.expression):
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.update_display()
        else:
            if not self.error_state:
                if char in "÷×-+%" and not any(c.isdigit() for c in self.expression):
                    return
                if len(self.expression) < 23 and (char.isdigit() or char in ".,÷×-+%"):
                    if char == ",":
                        char = "."
                    self.expression += char
                    self.update_display()


if name == "main":
    ModernSamsungCalculator().run()