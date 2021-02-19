% rebase('base.tpl', title='ASAS Athletics', page='Students')

<p>Welcome to the Students page, below is a list of all senior school students.</p>

<table class="table table-hover table-bordered table-sm table-dark">
  <thead class="thead-light">
    <tr>
      <th scope="col">Student ID</th>
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
      <td>{{row[0]}}</td>
      <td>{{row[1]}}</td>
      <td>{{row[2]}}</td>
      <td>{{row[3]}}</td>
      <td>{{row[4]}}</td>
      <td>{{row[5]}}</td>
    </tr>
%end
  </tbody>
</table>
