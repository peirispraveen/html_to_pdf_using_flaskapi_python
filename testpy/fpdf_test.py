from fpdf import FPDF, XPos, YPos


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('static/img/MySignature.jpg', 10, 8, 25)
        # Set font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Company Name', border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # Set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')


# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# Get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add Page
pdf.add_page()

# Specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)

for i in range(1, 10):
    pdf.cell(0, 10, f'This is line {i} :D', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Output PDF
pdf.output('pdfout/pdf_2.pdf')
