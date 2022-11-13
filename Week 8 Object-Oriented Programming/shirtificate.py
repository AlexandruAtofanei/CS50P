from fpdf import FPDF

class Pdf:
    # Initialize the name variable and the print_shirt function:
    def __init__(self, name):
        self.name = name
        self.print_shirt()

    # Get the input from the user through a @classmethod:
    @classmethod
    def get(cls):
        name = input("What is your name? ").strip()
        return cls(name)

    # Define a function that creates a pdf with the image(shirt) and text:
    def print_shirt(self):
        # Set font and add text to the top message in the page:
        pdf = FPDF(orientation="P", format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", "B", size = 45)
        pdf.set_text_color(0)
        pdf.cell(w = 0, h = 50, txt = "CS50 Shirtificate", border = 0, align = "C", new_x = "LMARGIN")
        # Add shirtificate.png to page:
        pdf.image(name = "shirtificate.png", x = 15, y = 70, w = 180)
        # Set font and add the input and text on to the shirt
        pdf.set_font("helvetica", "B", size = 25)
        pdf.set_text_color(255)
        pdf.cell(w = 0 , h = 240, txt = f"{self.name} took CS50", border = 0, align = "C")
        # Create pdf
        pdf.output("shirtificate.pdf")

def main():

    Pdf.get()

if __name__ == "__main__":
    main()
