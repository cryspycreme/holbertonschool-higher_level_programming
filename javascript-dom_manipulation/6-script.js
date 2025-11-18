// send a HTTP GET request to the specified url
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
// convert HTTP response to JS object    
    .then(response => {
        if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
        return response.json();
    })
    .then(data => {
        document.querySelector("#character").textContent = data.name;
        })
    .catch(error => {console.error('Error fetching character:', error);
    })