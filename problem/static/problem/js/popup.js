document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById("resultModal");
    var span = document.querySelector("#resultModal .close");

    modal.style.display = "block";

    span.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});