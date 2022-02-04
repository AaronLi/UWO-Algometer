from fpdf import FPDF
from datetime import date

import algometer_data


def print_pdf(name, age, height, weight, comment, areas_measured):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    '''
    pdf.set_font("Arial", size=12)
    pdf.cell(200 ,10, txt="Name: {}".format(name), ln=1, align="L")
    pdf.cell(200, 10, txt="Age: {}".format(age), ln=2, align="L")
    pdf.cell(200, 10, txt="Height: {}".format(height), ln=3, align="L")
    pdf.cell(200, 10, txt="Weight: {}".format(weight), ln=4, align="L")
    pdf.cell(200, 10, txt="Comments: {}".format(comment), ln=5, align="L")
    '''
    pdf.set_font("Times", size=12)
    pdf.line(10, 30, 200, 30)
    pdf.cell(100, 10, "Name: {}".format(name), 0, 0)
    sex = algometer_data.patient_sex
    pdf.cell(100, 10, "Sex: {}".format(sex), 0, 1)
    pdf.cell(100, 10, "Age: {}".format(age), 0, 0)
    pdf.cell(100, 10, "Height: {}".format(height), 0, 1)
    pdf.cell(100, 10, "Weight: {}".format(weight), 0, 1)
    pdf.line(10, 60, 200, 60)
    pdf.cell(200, 20, "{}".format(comment), 0, 1)
    pdf.line(10, 80, 200, 80)
    for i in range(len(areas_measured)):
        pdf.set_font("Arial", style="B")
        pdf.cell(200, 10, txt="{}".format(areas_measured[i][1]), ln=(6+i*3+1), align="L")
        pdf.set_font("Arial", style="")
        #testing step
        result = "no data"
        pdf.cell(200, 10, txt="\tRight Side: {}".format(result), ln=(6 + i * 3 + 2), align="L")
        pdf.cell(200, 10, txt="\tLeft Side: {}".format(result), ln=(6 + i * 3 + 3), align="L")
    formatted_name = name.replace(" ", "_")
    pdf.output("{}_Report.pdf".format(formatted_name))




class PDF(FPDF):
    def header(self):
        # Logo
        self.image('western_logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Algometer Measurement Analysis', 0, 0, 'C')
        self.set_font('Arial', '', 12)
        self.ln(5)
        today = date.today()
        day = "{}".format(today)
        self.cell(190, 10, day, 0, 2, 'C')
        # Line break
        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

