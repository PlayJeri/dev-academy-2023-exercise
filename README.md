Helsinki city bike App
A Flask application to store and display information about bike stations and rides. App also has admin only endpoint for adding data. And script to
parse csv files and adding the date to database.

Requirements
pip install -r requirements.txt

Clone the repository:

$ git clone https://github.com/PlayJeri/dev-academy-2023-exercise.git

Create an admin user:

create .env file and add username and password there
then run python create_admin.py

Run the application:

python app.py

Endpoints
/: Welcome page of the app that has links to rides and stations endpoints
/stations: Display the list of bike stations
/station: Display more detailed information about a single station
/rides: Display a list with rides and ride info
/login: Endpoint to login for admin access
/create_station: Endpoint for creating new bike stations (requires admin access)

Adding Data
The app allows you to add data to the database by uploading a CSV file containing information about bike stations and rides. The main.py script parses the CSV file and inserts the data into the SQLite database.

Tests
The app includes tests for the endpoints in the tests directory. To run the tests:

run pytest for testing
