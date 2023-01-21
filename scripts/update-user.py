#!/usr/bin/env python3

"""
./update-user.py -u username -p password -e email

Adds a user account to the website.
"""

import api

import argparse
import os
import sys

def main(args):
    # map arguments into parameter names expected by the API
    params = {}
    uid = None
    username = None
    for key, value in vars(args).items():
        if value is not None:
            if key is 'uid':
                uid = value
            elif key in 'username':
                username = value
            else:
                params[key] = value
    if uid is None and username is None:
        print("ERROR: a uid (--uid) or username (--username) is required", file=sys.stderr)
        sys.exit(1)
    if uid:
        exists = api.user.get_user(uid=uid)
    else:
        exists = api.user.get_user(name=username)
    if exists is None:
        print("ERROR: user does not exist", file=sys.stderr)
        sys.exit(1)

    try:
        # if params is not empty
        if bool(params):
            if uid:
                updated_user = api.user.update_user(uid=uid, params=params)
            else:
                updated_user = api.user.update_user(name=username, params=params)
            print("Updating user. Previous (initial) user information was:")
            print(updated_user)
        else:
            print("Not updating any user information.")
        print("Current user information is:")
        if uid:
            current_user = api.user.get_user(uid=uid, include_pw_hash=False)
        else:
            current_user = api.user.get_user(name=username, include_pw_hash=False)
        print(current_user)
    except api.PicoException as e:
        if uid:
            print(f"ERROR: failed to update user uid:{uid}", file=sys.stderr)
        else:
            print(f"ERROR: failed to update username:{username}", file=sys.stderr)
        print(e.message, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Update user account")

    parser.add_argument("-u", "--uid")
    parser.add_argument("-n", "--username")
    parser.add_argument("-e", "--email")
    parser.add_argument("-f", "--firstname")
    parser.add_argument("-l", "--lastname")
    parser.add_argument("-c", "--country")
    parser.add_argument("-a", "--affiliation")
    parser.add_argument("-t", "--usertype")

    args = parser.parse_args()

    # set default picoCTF settings
    if 'APP_SETTINGS_FILE' not in os.environ:
        os.environ['APP_SETTINGS_FILE'] = '/picoCTF-web-config/deploy_settings.py'
    with api.create_app().app_context():
        main(args)
