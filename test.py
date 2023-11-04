import requests

def test_api(api_url):
    try:
        # Send a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            print("API request was successful!")
            # You can print the response content for further inspection
            # print(response.text)
        else:
            print(f"API request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'api_url' with the actual URL of the API you want to test
    api_url = "https://github.com/AmericanAirlines/Flight-Engine/blob/main/src/api/flights.ts"
    test_api(api_url)
