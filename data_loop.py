import datetime
import time

import requests
import json
import uuid




API_KEY = "== YOUR API KEY =="
CLIENT_ID = "== YOUR CLIENT KEY =="



GEMINA_API_URL = "https://api.gemina.co.il/v1"
UPLOAD_URL = "/uploads"
BUSINESS_DOCUMENTS_URL = "/business_documents"

INVOICE_PATH = "invoice.png"
INVOICE_ID = f"ex_id_{uuid.uuid4()}"



def upload_image(image_path):
    url = f"{GEMINA_API_URL}{UPLOAD_URL}"
    token = f"Basic {API_KEY}"  # Mind the space between 'Basic' and the API KEY
    headers = {"Authorization": token}
    json_data = {
        "external_id": INVOICE_ID,
        "client_id": CLIENT_ID,
    }

    with open(image_path, "rb") as image_data:
        files = {
            "file": (image_path, image_data, "application/octet-stream"),
        }

        response = requests.post(url, files=files, headers=headers, data=json_data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        return response.status_code


def get_prediction(image_id):
    url = f"{GEMINA_API_URL}{BUSINESS_DOCUMENTS_URL}/{image_id}"
    token = f"Basic {API_KEY}"  # Mind the space between 'Basic' and the API KEY
    headers = {"Authorization": token}
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


def send_labeled_data(image_id):
    url = f"{GEMINA_API_URL}{BUSINESS_DOCUMENTS_URL}"
    token = f"Basic {API_KEY}"  # Mind the space between 'Basic' and the API KEY
    headers = {"Authorization": token}
    json_data = {
        "external_id": INVOICE_ID,
        "client_id": CLIENT_ID,
        "document_type": "invoice_receipt", # from a closed list
        "total_amount": 117.0, # can be either string or number
        "net_amount": 100.0, # can be either string or number
        "vat_amount": 17.0, # can be either string or number
        "document_number": "IL7890", # Can contain characters as well
        "issue_date": "2021-07-22", # YYYY-MM-DD
        "business_number": "EUR-514713288", # can contain characters as well
        "supplier_name": "Five Straps", # any language
        "expense_type": "fuel", # from a closed list
        "payment_method": "credit_card", # from a closed list
        "currency": "usd", # from a closed list
    }

    response = requests.put(url, headers=headers, json=json_data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def main():

    ### Step I:  Upload Image to the Gemina API ###

    status_code = upload_image(INVOICE_PATH)
    if status_code == 201:
        pass
    elif status_code == 202:
        print("Image is already being processed. No need to upload again.")
    elif status_code == 409:
        print("A prediction already exists for this image. No need to upload again.")
    else:
        print("Server returned an error. Operation failed.")
        return


    ### Step II:  Retrieve Prediction for the Uploaded Image ###

    prediction = get_prediction(INVOICE_ID)
    if prediction:
        print(f"Successfully retrieved Prediction for Invoice Image {INVOICE_ID}:")
        print(json.dumps(prediction, sort_keys=True, indent=4))
    else:
        print(f"Failed to retrieve Prediction for Invoice Image {INVOICE_ID}.")


    ### Step III:  Send Labeled Image Date and Close the Data Loop ###
    ### Perform this operation when users validate the prediction. ###

    labeled_data = send_labeled_data(INVOICE_ID)
    if labeled_data:
        print(f"Successfully updated the labeled data for Invoice Image {INVOICE_ID}:")
        print(json.dumps(labeled_data, sort_keys=True, indent=4))
    else:
        print(f"Failed to update labeled data for Invoice Image {INVOICE_ID}.")


if __name__ == "__main__":
    main()
