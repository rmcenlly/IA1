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
      .btn-BL{
        color:#FFFFFF;
        background-color:#ED1C24;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-BL:hover{
        color:#FFFFFF;
        background-color:#ED1C24;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
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
      .btn-DY{
        color:#FFFFFF;
        background-color:#00B6AD;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-DY:hover{
        color:#FFFFFF;
        background-color:#00B6AD;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
      }
      .btn-FG{
        color:#FFFFFF;
        background-color:#7C51A1;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-FG:hover{
        color:#FFFFFF;
        background-color:#7C51A1;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
      }
      .btn-HT{
        color:#FFFFFF;
        background-color:#FFCB08;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-HT:hover{
        color:#FFFFFF;
        background-color:#FFCB08;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
      }
      .btn-MC{
        color:#FFFFFF;
        background-color:#004A8F;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-MC:hover{
        color:#FFFFFF;
        background-color:#004A8F;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
      }
      .btn-RP{
        color:#FFFFFF;
        background-color:#00AEEF;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-RP:hover{
        color:#FFFFFF;
        background-color:#00AEEF;
        border-color: #FFFFFF;
        border-radius:5px;
        text-decoration:underline;
      }
      .btn-RV{
        color:#FFFFFF;
        background-color:#9D0A0E;
        border-color: #FFFFFF;
        border-radius:5px;
      }
      .btn-RV:hover{
        color:#FFFFFF;
        background-color:#9D0A0E;
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
      <li class="nav-item {{'active' if page == 'Houses' else '' }}">
        <a class="nav-link" href="/houses">Houses</a>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-BL" href="/houses/burchill">Burchill</a>
          <button type="button" class="btn btn-BL dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/burchill/15m">15M</a>
            <a class="dropdown-item" href="/houses/burchill/16m">16M</a>
            <a class="dropdown-item" href="/houses/burchill/17m">17M</a>
            <a class="dropdown-item" href="/houses/burchill/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/burchill/15f">15F</a>
            <a class="dropdown-item" href="/houses/burchill/16f">16F</a>
            <a class="dropdown-item" href="/houses/burchill/17f">17F</a>
            <a class="dropdown-item" href="/houses/burchill/18f">18F</a>
            <a class="dropdown-item" href="/houses/burchill/19f">19F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-BG" href="/houses/burling">Burling</a>
          <button type="button" class="btn btn-BG dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/burling/15m">15M</a>
            <a class="dropdown-item" href="/houses/burling/16m">16M</a>
            <a class="dropdown-item" href="/houses/burling/17m">17M</a>
            <a class="dropdown-item" href="/houses/burling/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/burling/15f">15F</a>
            <a class="dropdown-item" href="/houses/burling/16f">16F</a>
            <a class="dropdown-item" href="/houses/burling/17f">17F</a>
            <a class="dropdown-item" href="/houses/burling/18f">18F</a>
            <a class="dropdown-item" href="/houses/burling/19f">19F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-DY" href="/houses/day">Day</a>
          <button type="button" class="btn btn-DY dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/day/15m">15M</a>
            <a class="dropdown-item" href="/houses/day/16m">16M</a>
            <a class="dropdown-item" href="/houses/day/17m">17M</a>
            <a class="dropdown-item" href="/houses/day/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/day/15f">15F</a>
            <a class="dropdown-item" href="/houses/day/16f">16F</a>
            <a class="dropdown-item" href="/houses/day/17f">17F</a>
            <a class="dropdown-item" href="/houses/day/18f">18F</a>
            <a class="dropdown-item" href="/houses/day/19f">19F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-FG" href="/houses/fradgley">Fradgley</a>
          <button type="button" class="btn btn-FG dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/fradgley/15m">15M</a>
            <a class="dropdown-item" href="/houses/fradgley/16m">16M</a>
            <a class="dropdown-item" href="/houses/fradgley/17m">17M</a>
            <a class="dropdown-item" href="/houses/fradgley/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/fradgley/15f">15F</a>
            <a class="dropdown-item" href="/houses/fradgley/16f">16F</a>
            <a class="dropdown-item" href="/houses/fradgley/17f">17F</a>
            <a class="dropdown-item" href="/houses/fradgley/18f">18F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-HT" href="/houses/hobart">Hobart</a>
          <button type="button" class="btn btn-HT dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/hobart/15m">15M</a>
            <a class="dropdown-item" href="/houses/hobart/16m">16M</a>
            <a class="dropdown-item" href="/houses/hobart/17m">17M</a>
            <a class="dropdown-item" href="/houses/hobart/18m">18M</a>
            <a class="dropdown-item" href="/houses/hobart/19m">19M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/hobart/15f">15F</a>
            <a class="dropdown-item" href="/houses/hobart/16f">16F</a>
            <a class="dropdown-item" href="/houses/hobart/17f">17F</a>
            <a class="dropdown-item" href="/houses/hobart/18f">18F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-MC" href="/houses/mcintosh">McIntosh</a>
          <button type="button" class="btn btn-MC dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/mcintosh/15m">15M</a>
            <a class="dropdown-item" href="/houses/mcintosh/16m">16M</a>
            <a class="dropdown-item" href="/houses/mcintosh/17m">17M</a>
            <a class="dropdown-item" href="/houses/mcintosh/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/mcintosh/15f">15F</a>
            <a class="dropdown-item" href="/houses/mcintosh/16f">16F</a>
            <a class="dropdown-item" href="/houses/mcintosh/17f">17F</a>
            <a class="dropdown-item" href="/houses/mcintosh/18f">18F</a>
            <a class="dropdown-item" href="/houses/mcintosh/19f">19F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-RP" href="/houses/rapp">Rapp</a>
          <button type="button" class="btn btn-RP dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/rapp/15m">15M</a>
            <a class="dropdown-item" href="/houses/rapp/16m">16M</a>
            <a class="dropdown-item" href="/houses/rapp/17m">17M</a>
            <a class="dropdown-item" href="/houses/rapp/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/rapp/15f">15F</a>
            <a class="dropdown-item" href="/houses/rapp/16f">16F</a>
            <a class="dropdown-item" href="/houses/rapp/17f">17F</a>
            <a class="dropdown-item" href="/houses/rapp/18f">18F</a>
          </div>
        </div>
      </li>
      <li>
        <div class="btn-group mr-2">
          <a type="button" class="btn btn-RV" href="/houses/reeves">Reeves</a>
          <button type="button" class="btn btn-RV dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="/houses/reeves/15m">15M</a>
            <a class="dropdown-item" href="/houses/reeves/16m">16M</a>
            <a class="dropdown-item" href="/houses/reeves/17m">17M</a>
            <a class="dropdown-item" href="/houses/reeves/18m">18M</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="/houses/reeves/15f">15F</a>
            <a class="dropdown-item" href="/houses/reeves/16f">16F</a>
            <a class="dropdown-item" href="/houses/reeves/17f">17F</a>
            <a class="dropdown-item" href="/houses/reeves/18f">18F</a>
            <a class="dropdown-item" href="/houses/reeves/19f">19F</a>
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