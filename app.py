from flask import Flask, render_template, make_response, url_for
import pdfkit

app = Flask(__name__)


@app.route('/')
def pdf_template():
    # Prepare data for the template
    title = "Control Union Report"
    message = {
        "greeting": "Hi Jane",
        "content_1": "Your web redesign is finished and we're tracking results through this web analytics report. Early signs are good and everything seems to be on pace.",
        "content_2": "We're also going to be launching a few new landing pages next month. These will be used for SEO and PPC purposes."
    }
    images = {
        "image1": "https://storage.googleapis.com/corpeng-pulse-assets/uploads/2022/11/2image5-1536x783.jpg",
        "image2": "https://storage.googleapis.com/corpeng-pulse-assets/uploads/2022/11/2image2-1536x719.jpg"
    }
    stats = {
        "sessions": "10,487",
        "avg_session_duration": "00:00:26",
        "new_sessions": "13.09%",
        "bounce_rate": "35.00%",
        "goal_completions": "3,145",
        "pages_per_session": "3.49"
    }

    # Render the template with the data
    rendered = render_template('index.html', title=title, message=message, images=images, stats=stats)

    # Define CSS file(s)
    css = ['static/css/index.css']

    # Generate PDF from the rendered template
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
    try:
        pdf = pdfkit.from_string(rendered, False, options=options, css=css, configuration=config)
    except Exception as e:
        return str(e)  # Return the error message as a string (for debugging)

    # Prepare the response
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=control_union_report.pdf'

    return response


@app.route('/download_pdf')
def download_pdf():
    return pdf_template()


@app.route('/preview')
def preview():
    title = "Control Union Report"
    message = {
        "greeting": "Hi Jane",
        "content_1": "Your web redesign is finished and we're tracking results through this web analytics report. Early signs are good and everything seems to be on pace.",
        #"content_2": "We're also going to be launching a few new landing pages next month. These will be used for SEO and PPC purposes."
    }
    images = {
        "image1": "https://storage.googleapis.com/corpeng-pulse-assets/uploads/2022/11/2image5-1536x783.jpg",
        "image2": "https://storage.googleapis.com/corpeng-pulse-assets/uploads/2022/11/2image2-1536x719.jpg"
    }
    stats = {
        "sessions": "10,487",
        "avg_session_duration": "00:00:26",
        "new_sessions": "13.09%",
        "bounce_rate": "35.00%",
        "goal_completions": "3,145",
        "pages_per_session": "3.49"
    }

    # Render the template with the data
    return render_template('index.html', title=title, message=message, images=images, stats=stats)


if __name__ == '__main__':
    app.run(debug=True)