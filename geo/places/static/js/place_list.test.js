const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

test('Place list page renders correctly', () => {
  // Read the contents of the place_list.html file
  const filePath = path.join(process.cwd(), 'geo/places/templates/place_list.html');
  const html = fs.readFileSync(filePath, 'utf8');

  // Create a virtual DOM environment using jsdom
  const dom = new JSDOM(html);
  const document = dom.window.document;

  // Test that the page title is correct
  expect(document.title).toBe('Places List');

  // Test that the search form is present
  const searchForm = document.getElementById('search-form');
  expect(searchForm).toBeTruthy();

  // Test that the map element is present
  const mapElement = document.getElementById('map');
  expect(mapElement).toBeTruthy();

  // Test that the places list is present
  const placesList = document.getElementById('places-list');
  expect(placesList).toBeTruthy();
});

