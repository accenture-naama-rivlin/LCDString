class LcdStringGenerator:

    def generate(self, number=None):
        number_to_representation = {
            None: ["...", "...", "..."],
            0: ["._.", "|.|", "|_|"],
            1: ["...", "..|", "..|"],
            2: ["._.", "._|", "|_."],
            3: ["._.", "._|", "._|"],
            4: ["...", "|_|", "..|"],
            5: ["._.", "|_.", "._|"],
            6: ["._.", "|_.", "|_|"],
            7: ["._.", "..|", "..|"],
            8: ["._.", "|_|", "|_|"],
            9: ["._.", "|_|", "..|"]
        }

        number_to_string = str(number)

        display =[]
        for index in range(0, 3):
            for digit in number_to_string:
                display.append(number_to_representation[int(digit)][index] + " ")
            display.append("\n")

        display_return = ",".join(display)
        display_return = display_return.replace(",", "")

        return display_return


