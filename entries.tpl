% rebase('base.tpl', title='ASAS Athletics', page='Entries')

<p>Here are all the students entered in events, with their event listed.</p>

<table class="table table-hover table-bordered table-sm ">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Gender</th>
      <th scope="col">House</th>
      <th scope="col">Age</th>
      <th scope="col">Event</th>
      <th scope="col">Event Type</th>
      <th scope="col">Delete Entry</th>
    </tr>
  </thead>
  <tbody>
%for row in rows:  
    <tr>
      <th scope="row">{{row[1]}}</th>
      <td>{{row[2]}}</td>
      <td>{{row[3]}}</td>
      <td>{{row[4]}}</td>
      <td>{{row[5]}}</td>
      <td>{{row[6]}}</td>
      <td>{{row[8]}}</td>
      <td>{{row[9]}}</td>
      <td>
      <form action='/entries/delete' method='post'>
      <input type="hidden" name="id" value="{{row[0]}}" />
      <button type="submit" class="btn btn-danger">Delete</button>
      </form>
      </td>
    </tr>
%end
  </tbody>
</table>
