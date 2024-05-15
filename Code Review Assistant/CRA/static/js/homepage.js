document.addEventListener('DOMContentLoaded', function() {
    const userBtn = document.querySelector('.user-options button');
    const userMenu = document.querySelector('.user-menu');

    // Toggle display of the user menu
    userBtn.addEventListener('click', function() {
        userMenu.style.display = userMenu.style.display === 'block' ? 'none' : 'block';
    });

    // Close the user menu when clicking elsewhere on the page
    document.addEventListener('click', function(event) {
        if (!userBtn.contains(event.target) && !userMenu.contains(event.target)) {
            userMenu.style.display = 'none';
        }
    });
});