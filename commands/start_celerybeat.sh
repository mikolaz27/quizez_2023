#!/bin/bash

celery -A config worker -l ${CELERY_LOG_LEVEL} --beat --scheduler django