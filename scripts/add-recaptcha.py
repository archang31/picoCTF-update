#!/usr/bin/env python3

"""
./add-recaptcha.py

Initialized the optional recaptcha configuration settings.
"""

import api
import argparse
import os
import sys

def main(args):

    settings = api.config.get_settings()
    for key, value in vars(args).items():
        settings['captcha'][key] = value
    print(settings)
    api.config.change_settings(settings)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Configuration reCAPTCHA Settings")
    parser.add_argument("--enable_captcha", required=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument("--captcha_url", required=True)
    parser.add_argument("--reCAPTCHA_public_key", required=True)
    parser.add_argument("--reCAPTCHA_private_key", required=True)
    args = parser.parse_args()

    # set default picoCTF settings
    if 'APP_SETTINGS_FILE' not in os.environ:
        os.environ['APP_SETTINGS_FILE'] = '/picoCTF-web-config/deploy_settings.py'
    with api.create_app().app_context():
        main(args)
