from django.contrib import admin

from .models import Topic, Entry
"""Adminstration site"""
admin.site.register(Topic)
admin.site.register(Entry)
