% rebase('base.tpl', title='ASAS Atheltics', page='Events')

<h2 class='mt-3 mb-4'>Field Events</h2>

<p>Here is a list of all the existing field events. Each event is available for Males and Females separately, in separate groups of ages 14-18.</p>

<table class="table table-hover table-bordered table-sm mt-5 table-dark">
  <thead class="thead-light">
    <tr>
      <th scope="col">Event</th>
    </tr>
  </thead>
  <tbody>
%for row in rows:  
    <tr>
      <th scope="row">{{row[0]}}</th>
    </tr>
%end
  </tbody>
</table>