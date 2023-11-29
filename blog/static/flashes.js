var flashbox = document.getElementById("flashbox");
var flashes = document.getElementsByClassName("flashes");
var flashcross = document.getElementById("flashcross");

if (flashes.length == 0) {
    flashbox.style.display = "none";
}

flashcross.addEventListener("click", () => {
    flashbox.style.display = "none";
})