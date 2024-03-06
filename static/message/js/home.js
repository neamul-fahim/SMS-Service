document.querySelectorAll('.copy-button').forEach(button => {
    button.addEventListener('click', function() {
        const targetId = this.getAttribute('data-target');
        console.log(targetId)
        const numberElement = document.getElementById(targetId);
        console.log(numberElement)

        const phoneNumber = numberElement.textContent.trim();

        // Use Clipboard API to copy to clipboard
        navigator.clipboard.writeText(phoneNumber)
            .then(() => {
                console.log('Phone number copied to clipboard!');
            })
            .catch(err => {
                console.error('Failed to copy phone number:', err);
            });
    });
});
