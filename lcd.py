class LcdStringGenerator:

    def generate(self, number=None):
        lcd_string = ""
        number_to_representation = {
            None: "...\n...\n...",
            0: "._.\n|.|\n|_|",
            1: "...\n..|\n..|",
            2: "._.\n._|\n|_.",
            3: "._.\n._|\n._|",
            4: "...\n|_|\n..|"
        }

        for k, v in number_to_representation.items():
            if number == k:
                lcd_string += v

        return lcd_string

