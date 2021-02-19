% rebase('houses/hbase.tpl', title='ASAS Athletics', page='Reeves')

<p>Welcome to the Reeves Homepage. Here is a list of all of our students</p>

<div>
    <table style="background-color:transparent;" class="table table-hover table-bordered table-sm table-dark">
    <thead style="background-color:#9D0A0E;">
        <tr>
        <th scope="col">Event Name</th>
        <th scope="col">Event Type</th>
        <th scope="col">Select Student</th>
        <th scope="col">Confirm</th>
        </tr>
    </thead>
    <tbody>
%for event in events:  
        <tr>
            <form action='/houses/reeves/16m/submit' method='post'>
            <input type="hidden" name="EventID" value="{{event[0]}}">
                <td>{{event[1]}}</td>
                <td>{{event[2]}}</td>
            </input>
                <td>
                    <div class="dropdown">
                        <select name="StudentID" id="StudentID" class="btn btn-RV dropdown-toggle">
                            <option selected>Student</option>
%for student in students:  
                            <option name = "option" value="{{student[0]}}">{{student[1]}} {{student[2]}}</option>
%end
                        </select>
                    </div>
                </td>
                <td>
                <input type="hidden" name="StudentID, EventID" value="{{events[0]}}, {{students[0]}}" />
                <button type="submit" class="btn">Submit</button>
                </td>
                </form>
        </tr>
%end
    </tbody>
    </table>
</div>