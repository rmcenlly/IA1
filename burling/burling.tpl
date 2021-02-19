% rebase('base.tpl', title='ASAS Athletics', page='Burling')

<p style="text-align:center">
<img src="/img/burling.png" alt="Unavalible" class="img-fluid" style="width:20%;">
</p>
<br>
<h4>Here is a list of all of Burling students, sorted by age group:</h4>
<br>

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#008F4C; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample1" aria-expanded="false" aria-controls="collapseExample">
    15 Year Olds
</button>
<div class="collapse" id="collapseExample1">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm ">
  <thead>
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

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#008F4C; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample2" aria-expanded="false" aria-controls="collapseExample">
    16 Year Olds
  </button>
<div class="collapse" id="collapseExample2">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm ">
  <thead style="background-color:#008F4C;color:white">
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

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#008F4C; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample3" aria-expanded="false" aria-controls="collapseExample">
    17 Year Olds
  </button>
<div class="collapse" id="collapseExample3">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm ">
  <thead style="background-color:#008F4C;color:white">
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

<button class="btn btn-light dropdown-toggle btn-block" style="background-color:#008F4C; color:white; font-weight:bold;" type="button" data-toggle="collapse" data-target="#collapseExample4" aria-expanded="false" aria-controls="collapseExample">
    Opens
  </button>
<div class="collapse" id="collapseExample4">
  <div class="table table-body">
<table style="background-color:transparent;" class="table table-hover table-bordered table-sm ">
  <thead style="background-color:#008F4C;color:white">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
    </tr>
  </thead>
  <tbody>
%for open in opens:  
    <tr>
      <td>{{open[1]}}</th>
      <td>{{open[2]}}</td>
      <td>{{open[3]}}</td>
    </tr>
%end
  </tbody>
</table>
  </div>
</div>
<br>
</div>
<br>