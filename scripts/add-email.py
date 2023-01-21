#!/usr/bin/env python3

"""
./add-email.py

Initialized the optional email configuration settings.
"""

import api
import argparse
import os
import sys

def main(args):

    settings = api.config.get_settings()
    for key, value in vars(args).items():
        if key == 'email_filter':
            if value is not None:
                settings["email_filter"] = value.split(' ')
        else:
            settings["email"][key] = value
    print(settings)
    api.config.change_settings(settings)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Configuration Email Settings")
    parser.add_argument("--enable_email", required=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument("--email_verification", default=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument("--parent_verification_email", default=False, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument("--smtp_url", required=True)
    parser.add_argument("--smtp_port", default=587, type=int)
    parser.add_argument("--email_username", required=True)
    parser.add_argument("--email_password", required=True)
    parser.add_argument("--from_addr", required=True)
    parser.add_argument("--from_name", required=True)
    parser.add_argument("--max_verification_emails", default=3, type=int)
    parser.add_argument("--smtp_security", default="TLS")
    parser.add_argument("--email_filter", nargs='+', default=None)
    args = parser.parse_args()

    # set default picoCTF settings
    if 'APP_SETTINGS_FILE' not in os.environ:
        os.environ['APP_SETTINGS_FILE'] = '/picoCTF-web-config/deploy_settings.py'
    with api.create_app().app_context():
        main(args)
