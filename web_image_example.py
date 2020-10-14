import requests
import json
import time
import uuid




API_KEY = "== YOUR API KEY =="
CLIENT_ID = "== YOUR CLIENT KEY =="
INVOICE_URL = "== YOUR INVOICE URL =="



GEMINA_API_URL = "https://api.gemina.co.il/v1"
UPLOAD_URL = "/uploads/web"
BUSINESS_DOCUMENTS_URL = "/business_documents"

INVOICE_ID = f"ex_id_{uuid.uuid4()}"



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



def main():

    ### Step I:  Upload Image to the Gemina API ###

    status_code = upload_web_image(INVOICE_URL)
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


if __name__ == "__main__":
    main()
