% rebase('base.tpl', title='ASAS Athletics', page='Students')

<p>Welcome to the Runners page, below is a list of the runners who already exist in our databases.</p>

<table class="table table-hover table-bordered table-sm table-dark">
  <thead class="thead-light">
    <tr>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
      <th scope="col">House</th>
      <th scope="col">Age</th>
    </tr>
  </thead>
  <tbody>
%for row in rows:  
    <tr>
      <th scope="row">{{row[0]}}</th>
      <td>{{row[1]}}</td>
      <td>{{row[2]}}</td>
      <td>{{row[3]}}</td>
      <td>{{row[4]}}</td>
    </tr>
%end
  </tbody>
</table>
