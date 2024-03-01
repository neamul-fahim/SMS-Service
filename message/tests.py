# <!DOCTYPE html>
# <html>
#   <head>
#     <title>Number Details</title>
#     <!-- Include jQuery library -->
#     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
#     <style>
#       body {
#         font-family: Arial, sans-serif;
#         margin: 0;
#         padding: 0;
#         background-color: #f0f0f0;
#       }

#       /* Scroll bar style */
#       ::-webkit-scrollbar {
#         width: 8px;
#       }

#       ::-webkit-scrollbar-track {
#         background: #f1f1f1;
#       }

#       ::-webkit-scrollbar-thumb {
#         background: #888;
#         border-radius: 4px;
#       }

#       ::-webkit-scrollbar-thumb:hover {
#         background: #555;
#       }

#       .chat-header {
#         text-align: center;
#         margin-bottom: 20px;
#       }

#       .chat-container {
#         max-width: 1000px;
#         margin: 20px auto;
#         padding: 20px;
#         background-color: #fff;
#         border-radius: 10px;
#         box-shadow: 0 0 10px rgba(255, 165, 0, 1);
#       }

#       .chat-messages-container {
#         max-height: 400px; /* Adjust as needed */
#         overflow-y: auto;
#         padding-right: 16px; /* Add space for the scrollbar */
#       }

#       .chat-messages {
#         list-style: none;
#         padding: 0;
#         margin: 0;
#       }

#       .message {
#         background-color: #f2f2f2;
#         border-radius: 15px;
#         padding: 10px;
#         margin-bottom: 10px;
#         position: relative;
#       }

#       .message .content {
#         font-size: 16px;
#         color: #333;
#         line-height: 1.4;
#         padding: 5px;
#         margin-top: 5px;
#       }

#       .message .timestamp {
#         font-size: 12px;
#         color: #666;
#         position: absolute;
#         bottom: 5px;
#         right: 5px;
#       }

#       .message .from-number {
#         font-size: 14px;
#         color: #333;
#         margin-bottom: 5px;
#       }

#       .freeze-btn {
#         margin-bottom: 10px;
#       }
#     </style>
#   </head>
#   <body>
#     <div class="chat-header">
#       <h2>Chat with {{ number }}</h2>
#     </div>
#     <div class="chat-container">
#       <button class="freeze-btn" onclick="toggleAutoReload()">
#         Freeze Auto-Reload
#       </button>
#       <div class="chat-messages-container">
#         <ul class="chat-messages" id="messages">
#           <!-- Messages will be dynamically added here -->
#         </ul>
#       </div>
#     </div>

#     <script>
#       var chatWindowUrl = "{% url 'message' number %}";
#       var autoReloadIntervalId;

#       function formatTimestamp(timestamp) {
#         var date = new Date(timestamp);
#         return date.toLocaleString();
#       }

#       function scrollToBottom() {
#         var container = $(".chat-messages-container");
#         container.scrollTop(container.prop("scrollHeight"));
#       }

#       function updateMessages() {
#         $.ajax({
#           url: chatWindowUrl,
#           success: function (data) {
#             console.log("Received data:", data);
#             $("#messages").empty();
#             $.each(data.messages, function (index, message) {
#               console.log("Message:", message);
#               var formattedTimestamp = formatTimestamp(message.timestamp);
#               var messageHtml = `
#                           <li class="message">
#                               <div class="from-number">${message.from_number}</div>
#                               <div class="content">${message.message_body}</div>
#                               <div class="timestamp">${formattedTimestamp}</div>
#                           </li>`;
#               $("#messages").append(messageHtml);
#             });
#             scrollToBottom(); // Scroll to bottom after updating messages
#           },
#           error: function (xhr, status, error) {
#             console.error("Error fetching messages:", error);
#           },
#         });
#       }

#       function toggleAutoReload() {
#         if (autoReloadIntervalId) {
#           clearInterval(autoReloadIntervalId);
#           autoReloadIntervalId = null;
#           $(".freeze-btn").text("Resume Auto-Reload");
#         } else {
#           updateMessages(); // Update messages immediately when resuming auto-reload
#           autoReloadIntervalId = setInterval(updateMessages, 5000);
#           $(".freeze-btn").text("Freeze Auto-Reload");
#         }
#       }

#       $(document).ready(function () {
#         autoReloadIntervalId = setInterval(updateMessages, 5000);
#       });
#     </script>
#   </body>
# </html>
