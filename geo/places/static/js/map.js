// Leaflet map initialization
var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to create a marker and popup for each place
function createMarkerAndPopup(place) {
    var marker = L.marker([place.latitude, place.longitude]).addTo(map);
    marker.bindPopup(`<b>${place.name}</b><br>${place.description}`).openPopup();
}

// Function to update the places list and markers on the map
function updatePlacesAndMap(places) {
    var placesList = document.getElementById('places-list');
    placesList.innerHTML = '';

    places.forEach(function (place) {
        // Create a new list item for each place
        var listItem = document.createElement('li');
        listItem.innerHTML = `<b>${place.name}</b><br>${place.description}`;
        placesList.appendChild(listItem);

        // Create a marker and popup for each place on the map
        createMarkerAndPopup(place);
    });
}

// Function to handle form submission and AJAX call
document.getElementById('search-form').addEventListener('submit', function (event) {
    event.preventDefault();

    var query = document.getElementById('search-input').value.trim();
    if (query.length === 0) {
        alert('Please enter a search query.');
        return;
    }

    // Make an AJAX call to the API endpoint to search for places
    fetch(`/api/places/search/?query=${query}`)
        .then(response => response.json())
        .then(data => {
            updatePlacesAndMap(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

// Load all places and display markers on the map initially
fetch('/api/places/')
    .then(response => response.json())
    .then(data => {
        // Update the places list and markers on the map with all places
        updatePlacesAndMap(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
