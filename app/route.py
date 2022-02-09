from flask import render_template, redirect, url_for, request, send_from_directory, flash, jsonify
from flask import send_from_directory
import json
import datetime



# 頁面類
def index():
    return render_template('index.html')


def page_not_found(e):
    return render_template('404.html'), 404