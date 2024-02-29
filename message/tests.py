# <!DOCTYPE html>
# <html>
#   <head>
#     <title>Home Page</title>
#     <!-- Bootstrap CSS -->
#     <link
#       rel="stylesheet"
#       href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
#     />
#     <style>
#       /* Custom styles */
#       body {
#         font-family: "Roboto", sans-serif;
#         background-color: #f8f9fa;
#       }
#       .navbar {
#         background-color: #f8f9fa;
#         padding: 0.5rem 1rem;
#         box-shadow: 0 2px 4px rgba(255, 165, 0, 1);
#       }
#       .navbar-brand {
#         font-weight: bold;
#         font-size: 1.25rem;
#         color: #333;
#       }
#       .navbar-nav .nav-link {
#         color: #333;
#         font-size: 1rem;
#         margin-right: 1rem;
#       }
#       .navbar-nav .nav-link:hover {
#         color: #007bff;
#       }
#       .card {
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(255, 165, 0, 1);
#         transition: transform 0.3s ease;
#       }
#       .card:hover {
#         transform: translateY(-5px);
#       }
#       .card-title {
#         color: #333;
#         font-size: 1.2rem;
#         margin-bottom: 10px;
#       }
#       .card-text {
#         color: #666;
#         font-size: 0.9rem;
#       }
#       .container {
#         max-width: 800px;
#         margin-top: 50px;
#       }
#       .footer {
#         margin-top: 50px;
#         text-align: center;
#         color: #666;
#       }
#     </style>
#   </head>
#   <body>
#     <!-- Navigation Bar -->
#     <nav class="navbar navbar-expand-lg navbar-light">
#       <a class="navbar-brand" href="/">Home</a>
#       <!-- Add other navigation links here -->
#     </nav>

#     <!-- Content -->
#     <div class="container">
#       <h2 class="text-center mb-4">List of Numbers</h2>
#       <div class="row">
#         {% for number in numbers %}
#         <div class="col-md-4 mb-4">
#           <a href="{% url 'chat_window' number.number %}">
#             <div class="card">
#               <div class="card-body">
#                 <h5 class="card-title">{{ number.number }}</h5>
#                 <p class="card-text">Timestamp: {{ number.timestamp }}</p>
#               </div>
#             </div>
#           </a>
#         </div>
#         {% endfor %}
#       </div>
#     </div>

#     <!-- Footer -->
#     <div class="footer">
#       <p>&copy; 2024 Your Company. All rights reserved.</p>
#     </div>

#     <!-- Bootstrap JS (optional) -->
#     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
#     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
#   </body>
# </html>
