# ensembl_variant_lookup/routes.py

from flask import render_template

from ensembl_variant_lookup import app

@app.route('/')
def index():
    return render_template('index.html')
