% rebase('base.tpl', title='ASAS Atheltics', page='Sign-in')


<div class="container">

<div class="main">

<br>

<!--<form action='/signin' method = 'post' class = 'mt-5' name="myform">
    <div class="form-group">
        <label for="username">Please input your Username</label>
        <input type="username" class="form-control" id="username"/>
    </div>
    <div class="form-group">
        <label for="password">Please input your Password</label>
        <input type="password" class="form-control" id="password"/>
    </div>
    <div class="col-sm-10">
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
</form>-->

<form id='form_id' method='post' name='myform' class='mt-5'>

    <div class="form-group">
        <label for="username">User Name:</label>
        <input type="username" class="form-control" name="username" id="username"/>
    </div>

    <div class="form-group">
        <label for="password">Password:</label>
        <input class="form-control" type="password" name="password" id="password"/>
    </div>
    <div class="col-sm-10 mb-5">
        <input type="button" class="btn btn-primary" value="Login" id="submit" onclick="validate()"/>
    </div>

</form>

<!--<span><b class="note">Note : </b>For this demo use following username and password. <br/><b class="valid">User Name : Admin<br/>Password : Pass</b></span>-->

</div>

</div>

</body>

 

<script>

var attempt = 7; // Variable to count number of attempts.

// Below function Executes on click of login button.

function validate(){

var username = document.getElementById("username").value;

var password = document.getElementById("password").value;

if ( username == "Admin" && password == "Pass"){

href='/admin/';  

window.location = "/admin/";

return false;

}

else{

attempt --;// Decrementing by one.

alert("You have left "+attempt+" attempt;");

if( attempt == 0){

document.getElementById("username").disabled = true;

document.getElementById("password").disabled = true;

document.getElementById("submit").disabled = true;

return false;

}

}

}

</script>