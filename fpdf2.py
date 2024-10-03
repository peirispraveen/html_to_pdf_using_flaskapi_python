from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('static/img/MySignature.jpg', 10, 8, 25)
        # Set font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Web Analytics Report', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

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

# Set font for the message section
pdf.set_font('helvetica', '', 12)

# Adding the message
greeting = "Hi Jane,"
content_1 = "Your web redesign is finished and we're tracking results through this web analytics report. Early signs are good and everything seems to be on pace."
content_2 = "We're also going to be launching a few new landing pages next month. These will be used for SEO and PPC purposes."

pdf.cell(0, 10, greeting, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
pdf.cell(0, 10, content_1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
pdf.cell(0, 10, content_2, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)

# Adding images (placeholders)
pdf.set_fill_color(0, 0, 0)  # Red background for placeholders
pdf.cell(95, 60, '', 0, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=True)  # Left image
pdf.cell(95, 60, '', 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)  # Right image

# Adding statistics
stat_values = [10487, "00:00:26", "13.09%", "35.00%", 3145, 3.49]
stat_keys = ["Sessions", "Avg. Session Duration", "% New Sessions", "Bounce Rate", "Goal Completions", "Pages/Session"]

for i in range(6):
    pdf.cell(31, 20, f"{stat_values[i]}", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
    pdf.cell(31, 20, f"{stat_keys[i]}", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')

# Output PDF
pdf.output('pdf_report.pdf')
