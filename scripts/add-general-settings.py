#!/usr/bin/env python3

"""
./add-general-settings.py

Initialized the general configuration settings.
"""

import api
import argparse
import os
import sys

def main(args):
    settings = api.config.get_settings()
    for key, value in vars(args).items():
        if value is not None:
            settings[key] = value
    api.config.change_settings(settings)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Configuration General Settings")
    parser.add_argument("--enable_feedback", default=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument("--competition_name")
    parser.add_argument("--competition_url")
    parser.add_argument("--max_team_size", type=int)
    parser.add_argument("--max_batch_registrations", type=int)
    parser.add_argument("--enable_rate_limiting",  default=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument("--group_limit", type=int)
    args = parser.parse_args()

    # set default picoCTF settings
    if 'APP_SETTINGS_FILE' not in os.environ:
        os.environ['APP_SETTINGS_FILE'] = '/picoCTF-web-config/deploy_settings.py'
    with api.create_app().app_context():
        main(args)
