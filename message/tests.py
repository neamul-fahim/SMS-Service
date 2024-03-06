# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>24/7 free sms</title>
#     <link
#       rel="stylesheet"
#       href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
#     />
#     <link
#       rel="stylesheet"
#       href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
#     />

#     <link rel="stylesheet" href="static/message/css/home.css" />
#   </head>
#   <body>
#     {% load static %}
#     <nav class="navbar navbar-expand-lg navbar-light bg-light">
#       <div class="container">
#         <a class="navbar-brand" href="#">Your Logo Here</a>
#         <button
#           class="navbar-toggler"
#           type="button"
#           data-toggle="collapse"
#           data-target="#navbarNav"
#           aria-controls="navbarNav"
#           aria-expanded="false"
#           aria-label="Toggle navigation"
#         >
#           <span class="navbar-toggler-icon"></span>
#         </button>
#         <div class="collapse navbar-collapse" id="navbarNav">
#           <ul class="navbar-nav ml-auto">
#             <li class="nav-item">
#               <a class="nav-link" href="#">FAQ</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="#">About Us</a>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </nav>
#     <div class="container mt-5">
#       <div class="row">
#         <div class="col-md-12">
#           <h2 class="sms-header">#1 SMS Receiver App</h2>
#           <div class="teal-line"></div>
#           <p class="online">
#             Receive SMS<span class="teal"> Online 24/7</span>
#           </p>
#           <p class="introduction">
#             AnonymSMS is a totally free online service whereby you can receive
#             SMS messages online, without the need of inputting your own
#             mobile/cell number. Better yet, these temporary numbers are all
#             based on real SIM numbers, and means you will be able to view any
#             and all information received by this number online.
#           </p>
#         </div>
#       </div>
#     </div>

#     <div class="container">
#       <div class="card_latest_number">
#         <div class="card_latest_number_image">
#           <img
#             src="static/message/media/us_flag1.svg"
#             alt="United States Flag"
#             class="image"
#           />
#         </div>
#         <div class="card_content_latest_number">
#           <p class="title is-5 mt-40">
#             Latest added number
#             <span class="primary-text">{{latest_number.number}} </span
#             >{{latest_number.country}}
#           </p>
#           <p class="description">
#             This is the latest added number on our service
#           </p>
#           <div class="pt-10 pb-10">
#             <a
#               href="https://247freesms.com/number/+13159300250"
#               class="button btn-align btn-more is-link color-primary"
#               style="text-decoration: none; color: #fff"
#             >
#               Check it out
#             </a>
#           </div>
#         </div>
#       </div>
#     </div>

#     <div class="centered-container">
#       <h2>Available Numbers</h2>
#     </div>

#     <div class="container">
#       <div class="row">
#         {% for number in numbers %}
#         <div class="col-md-4 mb-4">
#           <div class="card">
#             <div class="card-body">
#               <!-- 1st Row -->
#               <div class="row">
#                 <div class="col-6">
#                   <img
#                     src="{{ number.country_flag_image.url }}"
#                     class="img-fluid"
#                     alt="Number Image"
#                   />
#                 </div>
#                 <div class="col-6">
#                   <h5>{{ number.country }}</h5>
#                 </div>
#               </div>
#               <!-- 2nd Row -->
#               <div class="row mt-3">
#                 <div class="col-6">
#                   <h5>{{ number.number }}</h5>
#                 </div>
#                 <div class="col-6">
#                   <button class="btn btn-secondary">
#                     <i class="fa fa-copy"></i>
#                   </button>
#                 </div>
#               </div>
#               <!-- 3rd Row -->
#               <div class="row mt-3">
#                 <div class="col-6">
#                   <i class="fa fa-folder-open"></i>
#                   <span>Received</span>
#                   <span>{{ number.message_count }}</span>
#                   <span>SMS</span>
#                 </div>
#               </div>
#               <!-- 4th Row -->
#               <div class="row mt-3">
#                 <div class="col-6">
#                   <i class="fa fa-clock"></i>
#                   <span>Last SMS Received</span>
#                   <span>{{ number.last_message_time_passed }}</span>
#                 </div>
#               </div>
#               <!-- 5th Row -->
#               <div class="row mt-3">
#                 <div class="col-6">
#                   <i class="fa fa-plus"></i>
#                   <span>Added</span>
#                   <span>{{ number.time_passed }}</span>
#                 </div>
#               </div>
#               <!-- 6th Row -->
#               <div class="row mt-3">
#                 <div class="col-12">
#                   <button class="btn btn-primary btn-block">Receive SMS</button>
#                 </div>
#               </div>
#             </div>
#           </div>
#         </div>
#         {% endfor %}
#       </div>
#     </div>

#     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
#     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
#   </body>
# </html>
