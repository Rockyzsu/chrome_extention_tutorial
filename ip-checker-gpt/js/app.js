window.addEventListener("load", () => {
  fetch("https://api.ipify.org/?format=json")
    .then(response => response.json())
    .then(data => {
      const ipAddress = data.ip;
      document.getElementById("ipAddress").textContent = ipAddress;
    })
    .catch(error => {
      console.error(error);
      document.getElementById("ipAddress").textContent = "Error fetching IP address";
    });
});