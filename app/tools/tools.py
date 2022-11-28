from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config


def build_template(template_name: str, template_params: dict):
    from jinja2 import Environment, FileSystemLoader

    template_path = f'templates/{template_name}/'
    environment = Environment(loader=FileSystemLoader(template_path))
    # Debe existir una carpeta llamada template_name y dentro dos archivos template.html y template.txt
    html_template = environment.get_template(f"template.html")
    text_template = environment.get_template(f"template.txt")

    return html_template.render(template_params), text_template.render(template_params)


def send_email_with_html_and_text(subject: str, to: str, html_content: str = None, text_content: str = None,
                                  cc: str = None, bcc: str = None):
    import smtplib

    if html_content is None and text_content is None:
        raise ValueError('Both html_content and text_content are None')

    if html_content is not None and text_content is None:
        raise ValueError('If html_content is set text_content is required')

    email_address = config.MAIL_DEFAULT_FROM

    # create email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    if bcc is not None:
        msg["Bcc"] = bcc
    if cc is not None:
        msg["Cc"] = cc

    # Record the MIME types of both parts - text/plain and text/html.
    msg.attach(MIMEText(text_content, 'plain'))

    if html_content is not None:
        msg.attach(MIMEText(html_content, 'html'))

    with smtplib.SMTP(config.MAIL_SMTP_HOST, config.MAIL_SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(config.MAIL_SMPT_USER, config.MAIL_SMPT_PASSWORD)
        smtp.send_message(msg)

    print(f'=== Done sending email to {msg["To"]}')
