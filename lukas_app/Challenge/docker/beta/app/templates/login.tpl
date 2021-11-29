<html>
<head>
</head>
<body>
<img src="https://cdn.lukas-app.de/static/logo.png" style="width:300px;" />
<br/>
<h1>Beta Login</h1>
<span style="color:red">{{ msg }}</span><br/>
<form action="/login" method="post">
Username: <input type="text" name="username" placeholder="username" /><br/>
Password: <input type="password" name="password" placeholder="password" /><br/>
<input type="submit" value="Login" />
</form>

</body>
</html>
