// Add event listeners to tab links to handle navigation
document.getElementById("home-tab").addEventListener("click", function() {
    window.location.href = "/";
});

document.getElementById("about-tab").addEventListener("click", function() {
    window.location.href = "/about";
});

document.getElementById("events-tab").addEventListener("click", function() {
    window.location.href = "/services";
});
