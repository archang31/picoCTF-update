#!/usr/bin/env bash

base=..
find $base/ansible $base/infra* $base/pico* $base/problems $base/scripts $base/ansible -type f -print0 | xargs -0 chmod 0644
#find $base/ansible $base/infra* $base/pico* $base/problems $base/scripts -type f -exec sh -c 'file {} | grep "text$" && dos2unix {}' \;
find $base/ansible $base/infra* $base/pico* $base/problems -type d -print0 | xargs -0 chmod 0755
chmod +x $base/scripts/*
chmod +x $base/infra*/terraform/.terraform/plugins/linux_amd64/terraform*
