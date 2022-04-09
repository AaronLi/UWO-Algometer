from fpdf import FPDF
from datetime import date
import enum
import algometer_data
import pyqtgraph as pg

class MeasurementRegionSide(enum.Enum):
    NONE = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()

def print_pdf(name, age, height, weight, comment, areas_measured):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
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
    for area_index in range(len(areas_measured)):
        pdf.set_font("Arial", style="B")
        pdf.cell(200, 10, txt="{}".format(areas_measured[area_index][1]), ln=(6+area_index*3+1), align="L")
        pdf.set_font("Arial", style="")

        pdf.cell(200, 10, txt="\t{}".format(algometer_data.readings[area_index][0]), ln=(6 + area_index * 3 + 2), align="L")
        ##print graphs
        for i, reading in enumerate(algometer_data.readings[area_index][1]):
            if reading[0] == MeasurementRegionSide.LEFT:
                pdf.cell(200, 10, txt="\tLeft Side: {}".format("hi"), ln=(6 + i * 3 + 2), align="L")

            elif reading[0] == MeasurementRegionSide.RIGHT:
                pdf.cell(200, 10, txt="\tRight Side: {}".format("hi"), ln=(6 + i * 3 + 2), align="L")
        #end graphs


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

