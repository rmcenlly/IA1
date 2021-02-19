% rebase('houses/hbase.tpl', title='ASAS Athletics', page='Hobart')

<p style="text-align:center">
<img src="/img/hobart.png" alt="Unavalible" class="img-fluid" style="width:20%;">
</p>
<br>
<h4>Welcome to the Hobart Homepage. Here is a list of all of our students</h4>
<br>

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#FFCB08; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample1" aria-expanded="false" aria-controls="collapseExample">
    15 Year Olds
</button>
<div class="collapse" id="collapseExample1">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm table-dark">
  <thead style="background-color:#FFCB08;color:white">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
    </tr>
  </thead>
  <tbody>
%for fifteen in fifteens:  
    <tr>
      <td>{{fifteen[1]}}</th>
      <td>{{fifteen[2]}}</td>
      <td>{{fifteen[3]}}</td>
    </tr>
%end
  </tbody>
</table>
  </div>
</div>
<br>

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#FFCB08; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample2" aria-expanded="false" aria-controls="collapseExample">
    16 Year Olds
  </button>
<div class="collapse" id="collapseExample2">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm table-dark">
  <thead style="background-color:#FFCB08;color:white">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
    </tr>
  </thead>
  <tbody>
%for sixteen in sixteens:  
    <tr>
      <td>{{sixteen[1]}}</th>
      <td>{{sixteen[2]}}</td>
      <td>{{sixteen[3]}}</td>
    </tr>
%end
  </tbody>
</table>
  </div>
</div>
<br>

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#FFCB08; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample3" aria-expanded="false" aria-controls="collapseExample">
    17 Year Olds
  </button>
<div class="collapse" id="collapseExample3">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm table-dark">
  <thead style="background-color:#FFCB08;color:white">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
    </tr>
  </thead>
  <tbody>
%for seventeen in seventeens:  
    <tr>
      <td>{{seventeen[1]}}</th>
      <td>{{seventeen[2]}}</td>
      <td>{{seventeen[3]}}</td>
    </tr>
%end
  </tbody>
</table>
  </div>
</div>
<br>

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#FFCB08; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample4" aria-expanded="false" aria-controls="collapseExample">
    18 Year Olds
  </button>
<div class="collapse" id="collapseExample4">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm table-dark">
  <thead style="background-color:#FFCB08;color:white">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
    </tr>
  </thead>
  <tbody>
%for eighteen in eighteens:  
    <tr>
      <td>{{eighteen[1]}}</th>
      <td>{{eighteen[2]}}</td>
      <td>{{eighteen[3]}}</td>
    </tr>
%end
  </tbody>
</table>
  </div>
</div>
<br>

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#FFCB08; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample5" aria-expanded="false" aria-controls="collapseExample">
    19 Year Olds
  </button>
<div class="collapse" id="collapseExample5">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm table-dark">
  <thead style="background-color:#FFCB08;color:white">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
    </tr>
  </thead>
  <tbody>
%for nineteen in nineteens:  
    <tr>
      <td>{{nineteen[1]}}</th>
      <td>{{nineteen[2]}}</td>
      <td>{{nineteen[3]}}</td>
    </tr>
%end
  </tbody>
</table>
  </div>
</div>
<br>