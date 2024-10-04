# 1. Create a template file as report_template.html
from jinja2 import Environment, FileSystemLoader

# 2. Create a template Environment
env = Environment(loader=FileSystemLoader('templates'))

# 3. Load the template from the Environment
template = env.get_template('CUformat.html')

# 4. Render the template with variables

html = template.render(
        main_title = "KUDUGALAYAYA KARAWILA BADALKUMBURA - TEMPORAL ANALYSIS 2020-2023",

        year1 = "2020",
        year2 = "2021",
        year3 = "2022",
        year4 = "2023",

        sat_img1 = "imgs/Picture1.png",
        sat_img2 = "imgs/Picture1.png",
        sat_img3 = "imgs/Picture1.png",
        sat_img4 = "imgs/Picture1.png",

        def_risk1 = "Deforestation risk is low (farm unit does not overlap forested areas with tree cover loss)",
        def_risk2 = "Deforestation risk is low (farm unit does not overlap forested areas with tree cover loss)",
        def_risk3 = "Deforestation risk is low (farm unit does not overlap forested areas with tree cover loss)",
        def_risk4 = "Deforestation risk is low (farm unit does not overlap forested areas with tree cover loss)",

        enc_risk1 = "Encroachment risk is low (Land is not encroaching with a protected area)",
        enc_risk2 = "Encroachment risk is low (Land is not encroaching with a protected area)",
        enc_risk3 = "Encroachment risk is low (Land is not encroaching with a protected area)",
        enc_risk4 = "Encroachment risk is low (Land is not encroaching with a protected area)",

        total_area = "0.12 ha",
        int_potec = "0.00 ha",

        int_def_area = "0.00 ha",
        eligible_area = "0.12 ha",

        scale_meters = "20M"
)

# 5. Write the template to an HTML file
with open('CU_report_jinja.html', 'w') as f:
    f.write(html)

import pdfkit
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
options = {
        'page-size': 'A4',
        'orientation': 'Landscape',
        'enable-local-file-access': None,  # Allow local file access
        'margin-top': '10mm',
        'margin-right': '10mm',
        'margin-bottom': '10mm',
        'margin-left': '10mm'
}

# 5. Generate PDF using pdfkit and external CSS
try:
        pdfkit.from_file('CU_report_jinja.html', 'CU_report.pdf', css='templates/styles.css', configuration=config)
except Exception as e:
        print(e)
