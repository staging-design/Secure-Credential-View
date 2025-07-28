window.onload = function () {
    fetch('/api/credentials')
        .then(response => response.json())
        .then(data => {
            document.getElementById("email").textContent = data.email;
            document.getElementById("passcode").textContent = data.passcode;
        })
        .catch(error => {
            console.error("Error fetching credentials:", error);
            document.getElementById("email").textContent = "Error";
            document.getElementById("passcode").textContent = "Error";
        });
}
