# Gemina API - Quick Implementation Guide



It's fast and easy to implement the Gemina Invoice Analysis.



First, define the API key that you were given, as well as the Client Id:

```python
API_KEY = "== YOUR API KEY =="
CLIENT_ID = "== YOUR CLIENT KEY =="
```



Also define the Gemina URL and endpoints:

```python
GEMINA_API_URL = "https://api.gemina.co.il/v1"
UPLOAD_URL = "/uploads"
BUSINESS_DOCUMENTS_URL = "/business_documents"
```



If you use a web image (instead of uploading one), then set the URL of the invoice.
In addition, don't forget to update the upload URL to web.

```python
INVOICE_URL = "== YOUR INVOICE URL =="
UPLOAD_URL = "/uploads/web"
```



Next, start implementing Gemina.

It happens in  2 steps:



------



## Step 1 - Upload Invoice

Here you upload a Business Document (for example: an invoice / credit invoice / receipt, and more) in an image format (we support all the available formats e.g. Jpeg / PNG).

The server will return the status code **201** to signify that the image has been added and that processing has started.

*If you use the same endpoint again*, you will find out that the server returns a *202 code*, to let you know that the same image has already been accepted, and there's no need to upload it again.

It could also return *409 if a prediction already exists for that image*.

Please note that the image file needs to be added to the **requests** files section as "*file*".



```python
def upload_image(image_path):
    url = f"{GEMINA_API_URL}{UPLOAD_URL}"
    headers = {"Authorization": API_KEY}
    json_data = {"external_id": INVOICE_ID}

    with open(image_path, "rb") as image_data:
        files = {
            "file": (image_path, image_data, "application/octet-stream"),
        }

        response = requests.post(url, files=files, headers=headers, data=json_data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        return response.status_code
```



**Alternatively,** you can submit an existing web image here:

```python
def upload_web_image(image_url):
    url = f"{GEMINA_API_URL}{UPLOAD_URL}"
    token = f"Basic {API_KEY}"  # Mind the space between 'Basic' and the API KEY
    headers = {"Authorization": token}
    json_data = {
        "external_id": INVOICE_ID,
        "client_id": CLIENT_ID,
        "url": image_url,
    }

    response = requests.post(url, headers=headers, data=json_data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    return response.status_code
```



Here's how you use the above functions:

```python
### Step I:  Upload Image to the Gemina API ###

status_code = upload_image(INVOICE_PATH)
# Alternatively: status_code = upload_web_image(INVOICE_URL)
if status_code == 201:
    pass
elif status_code == 202:
    print("Image is already being processed. No need to upload again.")
elif status_code == 409:
    print("A prediction already exists for this image. No need to upload again.")
else:
    print("Server returned an error. Operation failed.")
    return
```



------



## Step 2 - Get Prediction

Here you retrieve a prediction for the invoice that you uploaded during the first step.



You have to wait until the document finished processing.

Therefore you need to keep asking the server when the prediction is ready.



When it's not yet ready, the server will return either 404 (not found) or 202 (accepted and in progress).

*When Ready, the server will return **200**, with the prediction payload*.



```python
def get_prediction(image_id):
    url = f"{GEMINA_API_URL}{BUSINESS_DOCUMENTS_URL}/{image_id}"
    headers = {"Authorization": API_KEY}
    status = 202

    while(status == 202 or status == 404):
        response = requests.get(url, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        status = response.status_code
        if status == 202:
            print("Image is still being processed. Sleeping for 1 second before the next attempt.")
            time.sleep(1)
        elif status == 404:
            print("Can't find image. Let's give it 5 seconds to create before we try again...")
            time.sleep(5)

    if status == 200:
        return json.loads(response.text)
    else:
        return None
```



```python
### Step II:  Retrieve Prediction for the Uploaded Image ###

prediction = get_prediction(INVOICE_ID)
if prediction:
    print(f"Successfully retrieved Prediction for Invoice Image {INVOICE_ID}:")
    print(json.dumps(prediction, sort_keys=True, indent=4))
else:
    print(f"Failed to retrieve Prediction for Invoice Image {INVOICE_ID}.")
```



------



## Output

```bash
Response Status Code: 201
Response Text: {"created": "2021-05-02T16:53:58.421956", "timestamp": 1619974438.421956, "external_id": "ex_id_59e2c48a-dd58-4fe5-8ca7-9add86d10eee"}

Response Status Code: 202
Response Text: {"created": "2021-05-02T16:53:58.806600", "timestamp": 1619974438.8066, "external_id": "ex_id_59e2c48a-dd58-4fe5-8ca7-9add86d10eee"}

Image is still being processed. Sleeping for 1 second before the next attempt.
Response Status Code: 200
Response Text: {"total_amount": {"coordinates": {"normalized": [[156, 936], [242, 936], [242, 958], [156, 958]], "original": [[208, 1246], [322, 1246], [322, 1275], [208, 1275]]}, "value": 1572.0, "confidence": "high"}, "timestamp": 1619974439.228592, "issue_date": {"coordinates": {"normalized": [[782, 817], [885, 818], [885, 838], [782, 837]], "original": [[1041, 1087], [1178, 1089], [1178, 1115], [1041, 1114]]}, "value": "31/08/2020", "confidence": "high"}, "external_id": "ex_id_59e2c48a-dd58-4fe5-8ca7-9add86d10eee", "business_number": {"coordinates": {"normalized": [[182, 199], [303, 201], [303, 223], [182, 221]], "original": [[242, 265], [403, 268], [403, 297], [242, 294]]}, "value": 514713288, "confidence": "high"}, "net_amount": {"coordinates": {"normalized": [[173, 877], [244, 877], [244, 896], [173, 896]], "original": [[230, 1167], [325, 1167], [325, 1192], [230, 1192]]}, "value": 1343.59, "confidence": "high"}, "document_type": {"coordinates": null, "value": "invoice", "confidence": "high"}, "supplier_name": {"coordinates": null, "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2\"\u05de", "confidence": "high"}, "created": "2021-05-02T16:53:59.228592", "document_number": {"coordinates": {"normalized": [[412, 289], [501, 292], [500, 326], [411, 323]], "original": [[548, 385], [667, 389], [665, 434], [547, 430]]}, "value": 7890, "confidence": "high"}, "vat_amount": {"coordinates": {"normalized": [[189, 906], [241, 907], [241, 925], [189, 924]], "original": [[251, 1206], [321, 1207], [321, 1231], [251, 1230]]}, "value": 228.41, "confidence": "high"}}

Successfully retrieved Prediction for Invoice Image ex_id_59e2c48a-dd58-4fe5-8ca7-9add86d10eee:
{
    "business_number": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    182,
                    199
                ],
                [
                    303,
                    201
                ],
                [
                    303,
                    223
                ],
                [
                    182,
                    221
                ]
            ],
            "original": [
                [
                    242,
                    265
                ],
                [
                    403,
                    268
                ],
                [
                    403,
                    297
                ],
                [
                    242,
                    294
                ]
            ]
        },
        "value": 514713288
    },
    "created": "2021-05-02T16:53:59.228592",
    "document_number": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    412,
                    289
                ],
                [
                    501,
                    292
                ],
                [
                    500,
                    326
                ],
                [
                    411,
                    323
                ]
            ],
            "original": [
                [
                    548,
                    385
                ],
                [
                    667,
                    389
                ],
                [
                    665,
                    434
                ],
                [
                    547,
                    430
                ]
            ]
        },
        "value": 7890
    },
    "document_type": {
        "confidence": "high",
        "coordinates": null,
        "value": "invoice"
    },
    "external_id": "ex_id_59e2c48a-dd58-4fe5-8ca7-9add86d10eee",
    "issue_date": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    782,
                    817
                ],
                [
                    885,
                    818
                ],
                [
                    885,
                    838
                ],
                [
                    782,
                    837
                ]
            ],
            "original": [
                [
                    1041,
                    1087
                ],
                [
                    1178,
                    1089
                ],
                [
                    1178,
                    1115
                ],
                [
                    1041,
                    1114
                ]
            ]
        },
        "value": "31/08/2020"
    },
    "net_amount": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    173,
                    877
                ],
                [
                    244,
                    877
                ],
                [
                    244,
                    896
                ],
                [
                    173,
                    896
                ]
            ],
            "original": [
                [
                    230,
                    1167
                ],
                [
                    325,
                    1167
                ],
                [
                    325,
                    1192
                ],
                [
                    230,
                    1192
                ]
            ]
        },
        "value": 1343.59
    },
    "supplier_name": {
        "confidence": "high",
        "coordinates": null,
        "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2\"\u05de"
    },
    "timestamp": 1619974439.228592,
    "total_amount": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    156,
                    936
                ],
                [
                    242,
                    936
                ],
                [
                    242,
                    958
                ],
                [
                    156,
                    958
                ]
            ],
            "original": [
                [
                    208,
                    1246
                ],
                [
                    322,
                    1246
                ],
                [
                    322,
                    1275
                ],
                [
                    208,
                    1275
                ]
            ]
        },
        "value": 1572.0
    },
    "vat_amount": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    189,
                    906
                ],
                [
                    241,
                    907
                ],
                [
                    241,
                    925
                ],
                [
                    189,
                    924
                ]
            ],
            "original": [
                [
                    251,
                    1206
                ],
                [
                    321,
                    1207
                ],
                [
                    321,
                    1231
                ],
                [
                    251,
                    1230
                ]
            ]
        },
        "value": 228.41
    }
}
```



------



## Other Features



#### Pass the Client Tax Id

To facilitate the algorithm's work and increase accuracy, you can pass the Client's Tax Id to the API with each Json call.

This will help to avoid situations where the Client's Tax Id is mistakenly interpreted as the Supplier's Tax Id (or Business Number).

To do so, add the following line to the data Dictionary (that is, to your Json):

```python
{ "client_business_number": "== Your Client's Business Number =="}
```



Full example:

```python
json_data = {
	"external_id": INVOICE_ID,
    "client_id": CLIENT_ID,
    "url": image_url,
    "client_business_number": "== Your Client's Business Number =="
}
```

The `client_business_number` can be represented either by `string` or `int`.



------





The full example code is available here:

[Image Upload](https://github.com/tommyil/gemina-examples/blob/master/image_example.py)

[Web Image Upload](https://github.com/tommyil/gemina-examples/blob/master/web_image_example.py)



For more details, please refer to the [API documentation](https://api.gemina.co.il/swagger/).

You can also contact us [here](mailto:info@gemina.co.il).

