function updateDateTime() {
  const dateElement = document.getElementById("Date");
  const currentDate = new Date();
  const dateTimeString = currentDate.toLocaleString(); 
  dateElement.textContent = "Date: " + dateTimeString;
}

function fetchIP() {
  return fetch("https://api.ipify.org?format=json")
    .then(response => response.json())
    .then(data => {
      const IP = data.ip;
      const ipElement = document.getElementById("IP");
      ipElement.textContent = "Your IP: " + IP;
      return IP; // Return the IP address to be used in the next promise chain
    })
    .catch(error => {
      console.error('Error:', error);
      const ipElement = document.getElementById("IP");
      ipElement.textContent = "Unable to retrieve IP.";
      throw error; // Throw the error to be caught in the next promise chain
    });
}

function fetchGeolocation(ip) {
  return fetch(`https://ipapi.co/${ip}/json/`)
    .then(response => response.json())
    .then(data => {
      const city = data.city;
      const region = data.region;
      const country = data.country_name;

      const geolocationElement = document.getElementById("Location");
      geolocationElement.textContent = `Your Location: ${city}, ${region}, ${country}`;
    })
    .catch(error => {
      console.error('Error:', error);
      const geolocationElement = document.getElementById("Location");
      geolocationElement.textContent = "Unable to retrieve geolocation.";
      throw error; // Throw the error to be caught in the next promise chain
    });
}

function toggleMode() {
  const body = document.querySelector('body');
  body.classList.toggle('dark-mode');
  body.classList.toggle('light-mode');
}

fetchIP()
  .then(fetchGeolocation)
  .catch(error => {
    console.error('Error:', error);
  });

updateDateTime();
setInterval(updateDateTime, 1000);