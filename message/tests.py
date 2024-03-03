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
#         cursor: pointer; /* Change cursor to pointer on hover */
#       }
#       .card:hover {
#         transform: translateY(-5px);
#       }
#       .card a {
#         text-decoration: none; /* Remove underline for anchor tags inside cards */
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
#       <a class="navbar-brand" href="/">FAQ</a>
#       <a class="navbar-brand" href="/">About</a>
#       <!-- Add other navigation links here -->
#     </nav>

#     <!-- Introduction -->
#     <div class="container mt-5">
#       <h2>{{ homepage_design.introduction_header }}</h2>
#       <p>{{ homepage_design.introduction_body }}</p>
#       <!-- Edit icon -->
#       <a href="{% url 'edit_homepage_design' %}"><i class="fas fa-edit"></i></a>
#     </div>

#     <!-- Content -->
#     <div class="container">
#       <h2 class="text-center mb-4">Available Numbers</h2>
#       <div class="row">
#         {% for number in numbers %}
#         <div class="col-md-4 mb-4">
#           <a href="{% url 'chat_window' number.number %}" class="card-link">
#             <div class="card">
#               <div class="card-body">
#                 <h5 class="card-title">{{ number.number }}</h5>
#                 <p class="card-text">clich to see texts</p>
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
