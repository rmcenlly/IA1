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
      .btn-BG{
        color:#FFFFFF;
        background-color:#008F4C;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-BG:hover{
        color:#FFFFFF;
        background-color:#008F4C;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
      }
      a {
        /*-webkit-text-stroke-width: 0.1px;
        -webkit-text-stroke-color: white;*/
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
      <li class="nav-item mr-3 {{'active' if page == 'Houses' else '' }}">
        <a class="nav-link" href="/houses">Houses</a>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-BG" href="/burling">Burling</a>
          <button type="button" class="btn btn-BG dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/burling/15m">15M</a>
            <a class="dropdown-item" href="/burling/16m">16M</a>
            <a class="dropdown-item" href="/burling/17m">17M</a>
            <a class="dropdown-item" href="/burling/openm">OpenM</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/burling/15f">15F</a>
            <a class="dropdown-item" href="/burling/16f">16F</a>
            <a class="dropdown-item" href="/burling/17f">17F</a>
            <a class="dropdown-item" href="/burling/openf">OpenF</a>
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



