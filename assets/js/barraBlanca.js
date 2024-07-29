function loadbarraBlanca() {
    fetch('barraBlanca.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('barraBlanca-container').innerHTML = data;
        });
}

document.addEventListener('DOMContentLoaded', loadbarraBlanca);