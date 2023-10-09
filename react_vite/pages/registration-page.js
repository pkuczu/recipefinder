import React from 'react';

function RegisterPage() {
  return (
    <html>
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>Register - Recipe Finder</title>
        <style>
          {/* Your CSS styles go here */}
        </style>
      </head>
      <body style={{ backgroundColor: 'aquamarine' }}>
        <h1 align="center">
          <em>
            <strong>
              <font size="+5"> Recipe Finder </font>
            </strong>
          </em>
        </h1>
        <div className="topnav" align="center">
          <form action="/register" method="post">
            <input type="text" placeholder="Username" size="+50" id="username" name="username" /><br /><br />
            <input type="password" placeholder="Password" size="+50" id="password" name="password" /><br /><br />
            <input type="password" placeholder="Confirm Password" size="+50" id="confirmPassword" name="confirmPassword" /><br /><br />
            <input type="button" value="Register" />
          </form>
        </div>
      </body>
    </html>
  );
}

export default RegisterPage;