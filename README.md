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
    json_data = {
        "external_id": INVOICE_ID,
        "client_id": CLIENT_ID,
        "use_llm": True,  # <-- Optional, for LLM Support. For more details: https://github.com/tommyil/gemina-examples/blob/master/llm_integration.md
    }

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
        "use_llm": True,  # <-- Optional, for LLM Support. For more details: https://github.com/tommyil/gemina-examples/blob/master/llm_integration.md
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
Response Text: {"external_id": "ex_id_f53e9784-363f-4810-86d9-e028af95daf0", "timestamp": 1720471040.149028, "created": "2024-07-08T20:37:20.149028"}

Response Status Code: 404
Response Text: {"external_id": "ex_id_f53e9784-363f-4810-86d9-e028af95daf0", "client_id": 261, "type": null, "message": "Unable to find a Prediction for the specified external_id.", "success": false}

Can't find image. Let's give it 5 seconds to create before we try again...
Response Status Code: 200
Response Text: {"supplier_name": {"coordinates": null, "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2\"\u05de", "confidence": "high"}, "assignment_number": {"coordinates": null, "value": null, "confidence": "high"}, "vat_amount": {"coordinates": {"normalized": [[190, 908], [243, 908], [243, 926], [190, 926]], "original": [[253, 1208], [323, 1208], [323, 1232], [253, 1232]], "relative": [[0.15, 0.52], [0.2, 0.52], [0.2, 0.53], [0.15, 0.53]]}, "value": 228.41, "confidence": "high"}, "timestamp": 1720471040.737491, "total_amount": {"coordinates": {"normalized": [[159, 936], [243, 935], [243, 959], [159, 960]], "original": [[212, 1246], [323, 1244], [323, 1276], [212, 1278]], "relative": [[0.13, 0.53], [0.2, 0.53], [0.2, 0.55], [0.13, 0.55]]}, "value": 1572.0, "confidence": "high"}, "payment_method": {"coordinates": null, "value": "cheque", "confidence": "medium"}, "document_type": {"coordinates": null, "value": "invoice", "confidence": "high"}, "issue_date": {"coordinates": {"normalized": [[174, 407], [264, 409], [263, 431], [173, 429]], "original": [[232, 542], [351, 544], [350, 574], [230, 571]], "relative": [[0.14, 0.23], [0.21, 0.23], [0.21, 0.25], [0.14, 0.24]]}, "value": "31/08/2020", "confidence": "high"}, "document_number": {"coordinates": {"normalized": [[415, 284], [500, 285], [499, 329], [414, 328]], "original": [[552, 378], [665, 379], [664, 438], [551, 437]], "relative": [[0.33, 0.16], [0.4, 0.16], [0.4, 0.19], [0.33, 0.19]]}, "value": 7890, "confidence": "high"}, "net_amount": {"coordinates": {"normalized": [[175, 877], [245, 877], [245, 899], [175, 899]], "original": [[233, 1167], [326, 1167], [326, 1196], [233, 1196]], "relative": [[0.14, 0.5], [0.2, 0.5], [0.2, 0.51], [0.14, 0.51]]}, "value": 1343.59, "confidence": "high"}, "external_id": "ex_id_f53e9784-363f-4810-86d9-e028af95daf0", "business_number": {"coordinates": {"normalized": [[182, 198], [303, 200], [303, 224], [182, 222]], "original": [[242, 264], [403, 266], [403, 298], [242, 295]], "relative": [[0.15, 0.11], [0.24, 0.11], [0.24, 0.13], [0.15, 0.13]]}, "value": 514713288, "confidence": "high"}, "currency": {"coordinates": null, "value": "ils", "confidence": "medium"}, "created": "2024-07-08T20:37:20.737491", "primary_document_type": {"coordinates": null, "value": "invoice", "confidence": "high"}, "expense_type": {"coordinates": null, "value": "other", "confidence": "medium"}}

Successfully retrieved Prediction for Invoice Image ex_id_f53e9784-363f-4810-86d9-e028af95daf0:
{
    "assignment_number": {
        "confidence": "high",
        "coordinates": null,
        "value": null
    },
    "business_number": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    182,
                    198
                ],
                [
                    303,
                    200
                ],
                [
                    303,
                    224
                ],
                [
                    182,
                    222
                ]
            ],
            "original": [
                [
                    242,
                    264
                ],
                [
                    403,
                    266
                ],
                [
                    403,
                    298
                ],
                [
                    242,
                    295
                ]
            ],
            "relative": [
                [
                    0.15,
                    0.11
                ],
                [
                    0.24,
                    0.11
                ],
                [
                    0.24,
                    0.13
                ],
                [
                    0.15,
                    0.13
                ]
            ]
        },
        "value": 514713288
    },
    "created": "2024-07-08T20:37:20.737491",
    "currency": {
        "confidence": "medium",
        "coordinates": null,
        "value": "ils"
    },
    "document_number": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    415,
                    284
                ],
                [
                    500,
                    285
                ],
                [
                    499,
                    329
                ],
                [
                    414,
                    328
                ]
            ],
            "original": [
                [
                    552,
                    378
                ],
                [
                    665,
                    379
                ],
                [
                    664,
                    438
                ],
                [
                    551,
                    437
                ]
            ],
            "relative": [
                [
                    0.33,
                    0.16
                ],
                [
                    0.4,
                    0.16
                ],
                [
                    0.4,
                    0.19
                ],
                [
                    0.33,
                    0.19
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
    "expense_type": {
        "confidence": "medium",
        "coordinates": null,
        "value": "other"
    },
    "external_id": "ex_id_f53e9784-363f-4810-86d9-e028af95daf0",
    "issue_date": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    174,
                    407
                ],
                [
                    264,
                    409
                ],
                [
                    263,
                    431
                ],
                [
                    173,
                    429
                ]
            ],
            "original": [
                [
                    232,
                    542
                ],
                [
                    351,
                    544
                ],
                [
                    350,
                    574
                ],
                [
                    230,
                    571
                ]
            ],
            "relative": [
                [
                    0.14,
                    0.23
                ],
                [
                    0.21,
                    0.23
                ],
                [
                    0.21,
                    0.25
                ],
                [
                    0.14,
                    0.24
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
                    175,
                    877
                ],
                [
                    245,
                    877
                ],
                [
                    245,
                    899
                ],
                [
                    175,
                    899
                ]
            ],
            "original": [
                [
                    233,
                    1167
                ],
                [
                    326,
                    1167
                ],
                [
                    326,
                    1196
                ],
                [
                    233,
                    1196
                ]
            ],
            "relative": [
                [
                    0.14,
                    0.5
                ],
                [
                    0.2,
                    0.5
                ],
                [
                    0.2,
                    0.51
                ],
                [
                    0.14,
                    0.51
                ]
            ]
        },
        "value": 1343.59
    },
    "payment_method": {
        "confidence": "medium",
        "coordinates": null,
        "value": "cheque"
    },
    "primary_document_type": {
        "confidence": "high",
        "coordinates": null,
        "value": "invoice"
    },
    "supplier_name": {
        "confidence": "high",
        "coordinates": null,
        "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2\"\u05de"
    },
    "timestamp": 1720471040.737491,
    "total_amount": {
        "confidence": "high",
        "coordinates": {
            "normalized": [
                [
                    159,
                    936
                ],
                [
                    243,
                    935
                ],
                [
                    243,
                    959
                ],
                [
                    159,
                    960
                ]
            ],
            "original": [
                [
                    212,
                    1246
                ],
                [
                    323,
                    1244
                ],
                [
                    323,
                    1276
                ],
                [
                    212,
                    1278
                ]
            ],
            "relative": [
                [
                    0.13,
                    0.53
                ],
                [
                    0.2,
                    0.53
                ],
                [
                    0.2,
                    0.55
                ],
                [
                    0.13,
                    0.55
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
                    190,
                    908
                ],
                [
                    243,
                    908
                ],
                [
                    243,
                    926
                ],
                [
                    190,
                    926
                ]
            ],
            "original": [
                [
                    253,
                    1208
                ],
                [
                    323,
                    1208
                ],
                [
                    323,
                    1232
                ],
                [
                    253,
                    1232
                ]
            ],
            "relative": [
                [
                    0.15,
                    0.52
                ],
                [
                    0.2,
                    0.52
                ],
                [
                    0.2,
                    0.53
                ],
                [
                    0.15,
                    0.53
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



## More Resources



Response Types - https://github.com/tommyil/gemina-examples/blob/master/response_types.md

Data Loop - https://github.com/tommyil/gemina-examples/blob/master/data_loop.md

LLM Integration - https://github.com/tommyil/gemina-examples/blob/master/llm_integration.md

C# Implementation - https://github.com/tommyil/gemina-examples-cs

Node.js/TypeScript Implementation - https://github.com/tommyil/gemina-examples-ts

Java Implementation - https://github.com/tommyil/gemina-examples-java

PHP Implementation - https://github.com/tommyil/gemina-examples-php



------



The full example code is available here:

[Image Upload](https://github.com/tommyil/gemina-examples/blob/master/image_example.py)

[Web Image Upload](https://github.com/tommyil/gemina-examples/blob/master/web_image_example.py)



For more details, please refer to the [API documentation](https://api.gemina.co.il/swagger/).

You can also contact us [here](mailto:info@gemina.co.il).

