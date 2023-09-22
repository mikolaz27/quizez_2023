#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    if sys.argv[1].lower() == "test":
        print("NOTE: Running black formatter.")
        print(os.popen("black --config .black.toml .").read())
        print(os.popen("isort .").read())

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


# IaaS - infrastructure as a service  |
# PaaS - platform as a service, RDS   |
# SaaS - software as a service, 1


# КВт/год - ?
#
# 1 1 1 1 -> 1$
# 2 1 1 1 -> 2$
# 2 1 1 2 -> 4$
#
# # 1m\Xo|m/'n{7Y8o5%WJL5m@lXg}\YO5]RC^&hHwO=Os|#d
#
# """Free tier: In your first year includes 750 hours of t2.micro
# (or t3.micro in the Regions in which t2.micro is unavailable)
# instance usage on free tier AMIs per month, 30 GiB of EBS storage,
# 2 million IOs, 1 GB of snapshots, and 100 GB of bandwidth to the internet."""