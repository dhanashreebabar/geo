# Geo

1.Clone the Repository:
  Clone the repository containing the Django project and navigate to the project directory:
  
    >>git clone <repository_url>
    >> cd geo
    
2.Install Requirements:
  Install the required Python packages specified in the requirements.txt file:

>  >  pip install -r requirements.txt

3.Set Up the PostgreSQL Database:
  Ensure that you have PostgreSQL installed and create a new database for the project. Update the database settings in geo/settings.py to use your 
  PostgreSQL configuration.

4.Migrate the Database:
  Run the database migrations :
  >> python manage.py makemigrations
  >> python manage.py migrate

5.Run the Development Server:
    Start the Django development server:
    >> python manage.py runserver
    
6.Access the API Endpoints:
  The API endpoints are accessible at 
  http://localhost:8000/api/places/  
  http://localhost:8000/api/places/search/
  You can use tools like curl, Postman, or any other HTTP client to test the API.

7.Install Node.js Dependencies:
    In the root directory of the project, install the required Node.js dependencies:
    >>npm install
    >> npm install --save-dev jest jsdom

8.Run the JavaScript Tests:
  Run the JavaScript tests to ensure that the template is rendering correctly and the map integration and dynamic search functionality are working   
  as expected:
  >> npm test

9.Django API Testing:
 for testing the Django API, Run the following command to execute your Django API tests:
>  > python manage.py test

10.Access the Application:
  Finally, access the application by visiting http://localhost:8000/places/ in your web browser. You should see the Places List page with an   
  interactive map, search form, and the list of places.

  



    
