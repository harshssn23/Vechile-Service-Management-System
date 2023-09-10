'''pip install fpdf- to be run in the command prompt'''
from datetime import date

from fpdf import FPDF

pdf=FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 12)

pdf.cell(200,10,txt = "Vehicle Job Card",ln=1,align = 'C')
pdf.cell(200,10,txt = "Date: "+str(date.today()),ln=2,align = 'R')
pdf.cell(200,10,txt = "Customer Name:",ln=3,align = 'L')
pdf.cell(200,10,txt = "Vehicle Brand:",ln=4,align = 'L')
pdf.cell(200,10,txt = "Vehicle Model:",ln=5,align = 'L')
pdf.cell(200,10,txt = "Registration Number:",ln=6,align = 'L')
pdf.cell(200,10,txt = "Odometer reading:",ln=7,align = 'L')
pdf.cell(200,10,txt = "Fuel level:",ln=8,align = 'L')
pdf.cell(200,10,txt = "Test Drive:",ln=9,align = 'L')
pdf.cell(200,10,txt = "Service work done:",ln=10,align = 'L')
pdf.cell(200,10,txt = "Price:",ln=10,align = 'L')

pdf.output("jobcard.pdf")