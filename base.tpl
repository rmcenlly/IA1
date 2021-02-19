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
      .btn{
        color:#FFFFFF;
        background-color:#008F4C;
        border-color: #FFFFFF;
      }
      .btn:hover{
        color:#FFFFFF;
        background-color:#008F4C;
        text-decoration:underline;
        border-color:#FFFFFF;
      }
      .btn-danger {
        background-color: #ad0000;   
      }
      .btn-danger:hover {
        background-color: #000000;  
        color: #ad0000; 
      }
      a {
        /*-webkit-text-stroke-width: 0.1px;
        -webkit-text-stroke-color: white;*/
      }
      thead {
        background-color:#008F4C;
        color:white;
      }
      .dropdown-item:hover {
        background-color:#008f4c21
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
      <li class="nav-item {{'active' if page == 'Burling' else '' }}">
        <a class="nav-link" href="/burling">Burling</a>
      </li>
      <li class = "nav-item {{'active' if page == 'Events' else ''}}">
        <a class = "nav-link" href="/events">Events</a>
      </li>
      <li class = "nav-item {{'active' if page == 'Entries' else ''}}">
        <a style="margin-right:7.5px" class = "nav-link" href="/entries">Entries</a>
      </li>
      <li>
        <div class="btn-group mr-2">
          <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Submit
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/burling/15m">15 Male</a>
            <a class="dropdown-item" href="/burling/16m">16 Male</a>
            <a class="dropdown-item" href="/burling/17m">17 Male</a>
            <a class="dropdown-item" href="/burling/openm">Open Male</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/burling/15f">15 Female</a>
            <a class="dropdown-item" href="/burling/16f">16 Female</a>
            <a class="dropdown-item" href="/burling/17f">17 Female</a>
            <a class="dropdown-item" href="/burling/openf">Open Female</a>
          </div>
        </div>
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




