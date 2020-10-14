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
Response Text: {"external_id": "ex_id_1f4b81a1-1ca1-4830-9a4d-a5dbb1b6c7a7", "created": "2020-10-14T07:16:41.991518", "timestamp": 1602659801.991518}

Response Status Code: 404
Response Text: {"external_id": "ex_id_1f4b81a1-1ca1-4830-9a4d-a5dbb1b6c7a7", "message": "Unable to find a Prediction for the specified external_id.", "success": false}

Can't find image. Let's give it 5 seconds to create before we try again...
Response Status Code: 202
Response Text: {"external_id": "ex_id_1f4b81a1-1ca1-4830-9a4d-a5dbb1b6c7a7", "created": "2020-10-14T07:16:42.439719", "timestamp": 1602659802.439719}

Image is still being processed. Sleeping for 1 second before the next attempt.
Response Status Code: 200
Response Text: {"net_amount": {"confidence": "high", "value": 1343.59}, "total_amount": {"confidence": "high", "value": 1572.0}, "vat_amount": {"confidence": "high", "value": 228.41}, "supplier_name": {"confidence": "high", "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2~\u05de"}, "timestamp": 1602659803.36772, "business_number": {"confidence": "high", "value": 514713288}, "created": "2020-10-14T07:16:43.367720", "issue_date": {"confidence": "high", "value": "31/08/2020"}, "external_id": "ex_id_1f4b81a1-1ca1-4830-9a4d-a5dbb1b6c7a7", "document_number": {"confidence": "high", "value": 7890}, "document_type": {"confidence": "high", "value": "invoice"}}

Successfully retrieved Prediction for Invoice Image ex_id_1f4b81a1-1ca1-4830-9a4d-a5dbb1b6c7a7:
{
    "business_number": {
        "confidence": "high",
        "value": 514713288
    },
    "created": "2020-10-14T07:16:43.367720",
    "document_number": {
        "confidence": "high",
        "value": 7890
    },
    "document_type": {
        "confidence": "high",
        "value": "invoice"
    },
    "external_id": "ex_id_1f4b81a1-1ca1-4830-9a4d-a5dbb1b6c7a7",
    "issue_date": {
        "confidence": "high",
        "value": "31/08/2020"
    },
    "net_amount": {
        "confidence": "high",
        "value": 1343.59
    },
    "supplier_name": {
        "confidence": "high",
        "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2~\u05de"
    },
    "timestamp": 1602659803.36772,
    "total_amount": {
        "confidence": "high",
        "value": 1572.0
    },
    "vat_amount": {
        "confidence": "high",
        "value": 228.41
    }
}
```



------



The full example code is available here:

[Image Upload](https://github.com/tommyil/gemina-examples/blob/master/image_example.py)

[Web Image Upload](https://github.com/tommyil/gemina-examples/blob/master/web_image_example.py)



For more details, please refer to the [API documentation](https://api.gemina.co.il/swagger/).

You can also contact us [here](mailto:info@gemina.co.il).

