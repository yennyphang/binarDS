#!/usr/bin/env python
# coding: utf-8

# In[11]:


import re
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling')
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,config=swagger_config)

@swag_from("docs/hello_world.yml", methods=['GET'])
@app.route('/', methods=['GET'])
def hello_Yenny():
    json_response = {
        'status_code': 200,
        'description': "Menyapa Hello Yenny",
        'data': "Hello World"
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text.yml", methods=['GET'])
@app.route('/text', methods=['GET'])
def text():
    json_response = {
        'status_code': 200,
        'description': "Original Teks",
        'data': "Halo, apa kabar semua?"
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_clean.yml", methods=['GET'])
@app.route('/text-clean', methods=['GET'])
def text_clean():
    json_response = {
        'status_code': 200,
        'description': "Original Teks",
        'data': re.sub(r'[^a-zA-Z0-9]', ' ', "Halo, apa kabar semua?")
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_processing.yml", methods=['POST'])
@app.route('/text-processing_input', methods=['POST'])
def text_processing_input():

    text = request.form.get('text')

      json_response = {
        'status_code': 200,
        'description': "cleaning text user input",
        'raw_data':text
        'clean_data': re.sub(r'[^a-zA-Z0-9]', ' ', text)
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_processing_upload.yml", methods=['POST'])
@app.route('/text-processing_upload', methods=['POST'])
def text_processing_upload():

    file = request.file.get('file')

#     json_response = {
#         'status_code': 200,
#         'description': "cleaning text user input",
#         'raw_data':text
#         'clean_data': re.sub(r'[^a-zA-Z0-9]', ' ', text)
#     }
    df = pd_read_csv(file)
    
    response_data = jsonify(df.to_dict())
    return response_data


if __name__ == '__main__':
    app.run()


# In[ ]:




