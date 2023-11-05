'''''
import requests
import csv

# Define the API endpoint
api_endpoint = "http://localhost:4000/flights?date=2023-10-21"

# Make a request to the API endpoint
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:

    # Parse the API response into a JSON object
    data = response.json()

    # Get the first 10 data entries
    first_10_data_entries = data[:10]

    # Open a CSV file for writing
    with open("data.csv", "w", newline="") as csvfile:

        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(first_10_data_entries[0].keys())

        # Write each row of data to the CSV file
        for row in first_10_data_entries:
            writer.writerow(row.values())

# If the request was not successful, print an error message
else:
    print("Error: Could not fetch data from API")
'''
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data that you want to display on the frontend
sample_data = {
    'name': 'John Doe',
    'age': 30,
    'location': 'New York',
}

# Define an endpoint to get the data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
