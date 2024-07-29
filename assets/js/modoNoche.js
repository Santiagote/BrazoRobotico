// Función para alternar el modo oscuro
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    let toggleLink = document.getElementById('toggle-dark-mode');
    let heroSection = document.getElementById('hero-section');

    // Cambiar el fondo del hero-section
    if (document.body.classList.contains('dark-mode')) {
        heroSection.classList.remove('bg-success');
        heroSection.classList.add('bg-dark-mode');
    } else {
        heroSection.classList.remove('bg-dark-mode');
        heroSection.classList.add('bg-success');
    }

    // Cambiar el icono del enlace según el modo
    toggleLink.innerHTML = document.body.classList.contains('dark-mode') ?
        '<i class="fas fa-sun fa-sm fa-fw me-2"></i>' :
        '<i class="fas fa-moon fa-sm fa-fw me-2"></i>';
    
    // Guardar el estado en el almacenamiento local
    localStorage.setItem('dark-mode', document.body.classList.contains('dark-mode'));
}

// Función para cargar el estado del modo oscuro desde el almacenamiento local
function loadDarkMode() {
    // Verificar si el modo oscuro está activado
    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
        let heroSection = document.getElementById('hero-section');
        if (heroSection) {
            heroSection.classList.remove('bg-success');
            heroSection.classList.add('bg-dark-mode');
        }
    } else {
        document.body.classList.remove('dark-mode');
        let heroSection = document.getElementById('hero-section');
        if (heroSection) {
            heroSection.classList.remove('bg-dark-mode');
            heroSection.classList.add('bg-success');
        }
    }
    
    let toggleLink = document.getElementById('toggle-dark-mode');
    if (toggleLink) {
        toggleLink.innerHTML = document.body.classList.contains('dark-mode') ?
            '<i class="fas fa-sun fa-sm fa-fw me-2"></i>' :
            '<i class="fas fa-moon fa-sm fa-fw me-2"></i>';
    }
}

// Ejecutar al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    loadDarkMode();
    
    let toggleLink = document.getElementById('toggle-dark-mode');
    if (toggleLink) {
        toggleLink.addEventListener('click', function(event) {
            event.preventDefault();
            toggleDarkMode();
        });
    }
});
