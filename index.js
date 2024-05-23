document.getElementById('subscribe-button').addEventListener('click', function() {
    const emailInput = document.getElementById('email');
    const message = document.getElementById('message');
    const subscribeContainer = document.getElementById('subscribe-container');
    const emailPattern = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;

    if (emailPattern.test(emailInput.value)) {
        subscribeContainer.style.display = 'none'; // Hide the subscribe container
        message.textContent = 'You are subscribed!!'; // Display the success message
        message.style.color = 'black'; // Set the color of the message to black
    } else {
        message.style.color = '#fcba03'; // Set the color of the message to red
        message.textContent = 'Please enter a valid email address (xyz@gmail.com)'; // Display error message
    }
});


document.getElementById('reserve-button').addEventListener('click', function() {
    alert('Reservation functionality is not yet implemented.');
});
