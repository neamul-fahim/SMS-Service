function copyNumberToClipboard() {
    var numberElement = document.getElementById("provider-phone");
    var numberText = numberElement.innerText;
    
    navigator.clipboard.writeText(numberText)
        .then(function() {
            console.log('Text copied to clipboard successfully: ' + numberText);
        })
        .catch(function(error) {
            console.error('Error copying text to clipboard: ', error);
        });
}

$(document).ready(function() {
    // Function to fetch messages
    function fetchMessages() {
        // Get the number from the hidden input field
        var number = document.getElementById("message-number").value;

        // Make AJAX request to fetch messages
        $.ajax({
            url: `/message/${number}/`,
            type: 'GET',
            success: function(response) {
                var messages = response.messages;

                // Reverse messages array to display recent messages first
                messages.reverse();

                // Clear existing messages in the table body
                $('#message-table tbody').empty();

                // Iterate over messages and populate the table
                $.each(messages, function(index, message) {
                    var newRow = `<tr>
                                    <td>${message.from_number}</td>
                                    <td>${message.message_body}</td>
                                    <td>${message.timestamp}</td>
                                  </tr>`;
                    $('#message-table tbody').append(newRow);
                });
            },
            error: function(xhr, status, error) {
                console.error('Error fetching messages:', error);
            }
        });
    }

    // Call fetchMessages function initially
    fetchMessages();

    // Set interval to fetch messages every 3 seconds
    setInterval(fetchMessages, 3000);
});

// Replace with your actual selector for the message container (table-container in this case)
const container = document.querySelector('.table-container');
const messageTable = document.getElementById('message-table');

function formatTimestamp(timestamp) {
  const date = new Date(timestamp);
  return date.toLocaleString();
}

function scrollToBottom() {
  container.scrollTop = container.scrollHeight;
}

function updateMessages() {
    const container = document.querySelector('.table-container');
    const messageTable = document.getElementById('message-table');
    const scrollOffset = container.scrollTop; // Capture scroll offset before update
  
    // Replace with your actual logic for fetching messages (e.g., using fetch API)
    fetch(chatWindowUrl)
      .then(response => response.json())
      .then(data => {
        const messagesContainer = document.getElementById('messages');
        messagesContainer.innerHTML = ''; // Clear existing messages
  
        data.messages.forEach(message => {
          const formattedTimestamp = formatTimestamp(message.timestamp);
          const messageHtml = `
            <tr class="message">
              <td>${message.from_number}</td>
              <td>${message.message_body}</td>
              <td>${formattedTimestamp}</td>
            </tr>`;
          messagesContainer.insertAdjacentHTML('beforeend', messageHtml);
        });
  
        // Restore scroll position after DOM update
        container.scrollTop = scrollOffset;
      })
      .catch(error => console.error("Error fetching messages:", error));
  }
  