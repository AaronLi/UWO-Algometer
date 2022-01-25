from fpdf import FPDF

def print_pdf(name, age, height, weight, comment, areas_measured):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200 ,10, txt="Name: {}".format(name), ln=1, align="L")
    pdf.cell(200, 10, txt="Age: {}".format(age), ln=2, align="L")
    pdf.cell(200, 10, txt="Height: {}".format(height), ln=3, align="L")
    pdf.cell(200, 10, txt="Weight: {}".format(weight), ln=4, align="L")
    pdf.cell(200, 10, txt="Comments:\n {}".format(comment), ln=5, align="L")
    pdf.cell(200, 10, txt="----------------------------------------------------------------------------------------------------", ln=6, align="L")
    formatted_name = name.replace(" ", "_")
    pdf.output("{}_Report.pdf".format(formatted_name))


