const texts = [
    "Empower your coding with AI.",
    "Revolutionize your code reviews.",
    "Optimize your development process.",
    // Add more predefined texts here
];

let currentIndex = 0;

function typeText(text, index, callback) {
    if (index < text.length) {
        document.getElementById('randomTexts').innerHTML = text.substring(0, index + 1) + '<span aria-hidden="true"></span>';
        setTimeout(function() {
            typeText(text, index + 1, callback);
        }, 100); // Speed of typing
    } else if (callback) {
        setTimeout(callback, 2000); // Wait a bit before starting to delete
    }
}

function changeText() {
    const text = texts[currentIndex];
    typeText(text, 0, function() {
        // Wait a bit before changing to the next text
        setTimeout(function() {
            currentIndex = (currentIndex + 1) % texts.length;
            changeText();
        }, 2000); // Time before changing to the next text
    });
}

changeText();

document.getElementById('login').addEventListener('click', function() {
    window.location.href = "{% url 'lf' %}"; // Redirects to the actual login page
});

document.getElementById('Signup').addEventListener('click', function() {
    window.location.href = "{% url 'signup' %}"; // Redirects to the signup page
});

