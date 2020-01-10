"""
Microsoft Reactor Flask + Cognitive Services Demo

See repo:
https://github.com/microsoft/Reactors/blob/master/AI_1/
"""

import os
import base64
import json

from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests

from image import Image

# Load system variables with dotenv
load_dotenv()

# Load keys

# Create vision_client

# Create face_client

# Create the application
app = Flask(__name__)  # NOQA


@app.route("/", methods=["GET"])
def index():
    """
    Homepage controller
    """

    return render_template("index.html")


@app.route("/translate", methods=["GET", "POST"])
def translate():
    """
    Takes an image in for OCR and returns a translation
    If a GET request, returns the html form
    """
    # Load image or placeholder
    image = get_image()

    # Set the default for language translation
    target_language = "en"
    if request.form and "target_language" in request.form:
        target_language = request.form["target_language"]

    # If it"s a GET, just return the form
    if request.method == "GET":
        return render_template("translate.html",
                               image_uri=image.uri,
                               target_language=target_language)

    # Create a placeholder for messages
    messages = []

    # TODO: Add code to retrieve text from picture

    # TODO: Add code to translate text

    return render_template("translate.html", image_uri=image.uri,
                           target_language=target_language, messages=messages)


@app.route("/train", methods=["GET", "POST"])
def train():
    """
    Adds new faces to train the model more
    """

    # Load image or placeholder
    image = get_image()

    # If it"s a GET, just return the form
    if request.method == "GET":
        return render_template("train.html", image_uri=image.uri)

    # Retrieve name from form
    name = ""
    if "name" in request.form:
        name = request.form["name"]

    # Placeholder for messages
    messages = []

    # TODO: Add code to create or update person

    if not messages:
        messages.append("I don't recognize anyone")

    return render_template("train.html", messages=messages, image_uri=image.uri)  # NOQA


@app.route("/detect", methods=["GET", "POST"])
def detect():
    """
    Use model as currently trained to detect faces
    """

    # Load image or placeholder
    image = get_image()

    # If it"s a GET, just return the form
    if request.method == "GET":
        return render_template("detect.html", image_uri=image.uri)

    # Placeholder for message
    messages = []

    # TODO: Add code to detect people in picture

    return render_template("detect.html", messages=messages, image_uri=image.uri)  # NOQA


def get_image():
    """
    Helper function to extract an Image from the current request

    See Image class for details on this works.
    """

    # Helper class
    if request.files:
        return Image(request.files["file"])
    return Image()
