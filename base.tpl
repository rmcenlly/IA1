<!doctype html>
<html lang="en">
  <head>
    <link rel="icon" href="/img/favicon.ico">
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title>{{title or 'No title'}}</title>
    <style>
      body {
        background-color: #1a1a1a;
        color: #FFFFFF;
      }
      .btn{
        color:#FFFFFF;
        background-color:#349cd9;
        border-color: #FFFFFF;
      }
      .btn:hover{
        color:#FFFFFF;
        background-color:#a1c6e1;
        border-color:#FFFFFF;
      }
      .btn-danger {
        background-color: #ad0000;   
      }
      .btn-danger:hover {
        background-color: #000000;  
        color: #ad0000; 
      }
    </style>
  </head>
  
  <body>
  <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #012c81;">
  <a class="navbar-brand" href="/">ASAS Athletics</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item {{'active' if page == 'Home' else '' }}">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item {{'active' if page == 'Students' else '' }}">
        <a class="nav-link" href="/students">Students</a>
      </li>
      <li class = "nav-item {{'active' if page == 'Events' else ''}}">
        <a class = "nav-link" href="/events">Events</a>
      </li>
      <li class = "nav-item {{'active' if page == 'Entries' else ''}}">
        <a class = "nav-link" href="/entries">Entries</a>
      </li>
      <li class = "nav-item {{'active' if page == 'Houses' else ''}}">
        <a class = "nav-link" href="/houses">Houses</a>
      </li>
    </ul>
  </div>
</nav>

<div class="container mt-5">
  <h1>{{page}}</h1>
    {{!base}}
</div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>