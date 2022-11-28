import argparse

import config
import csv
import os
from tools.tools import build_template, send_email_with_html_and_text


def run(**kwargs):
    CSV_DIR = 'storage'

    template_name = kwargs.get('template_name')
    csv_path = os.path.join(CSV_DIR, kwargs.get('source_csv'))

    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for params_dict in csv_reader:
            print(f'Read: {params_dict}')

            html, text = build_template(template_name, params_dict)

            cc = params_dict.get('cc', None)
            bcc = params_dict.get('bcc', None)

            send_email_with_html_and_text(params_dict['email_subject'], params_dict['to'], html, text, cc, bcc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')

    parser.add_argument(
        '--template_name', type=str,
        help='The name of the template located in send_email/templates/introductory_lesson',
        required=True
    )

    parser.add_argument(
        '--source_csv', type=str,
        help='The name of the csv located in send_email/storage',
        required=True
    )

    parser.add_argument(
        '--send_emails', action='store_true',
        help='Send emails through real SMTP, otherwise send through Mailtrap. ',
    )

    args = parser.parse_args()

    print("=== Received args: ")
    print(args.__dict__)

    run(**args.__dict__)
