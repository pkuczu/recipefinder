import React from 'react';

function LoginPage() {
  return (
    <html>
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>Login - Recipe Finder</title>
        <style>
          {}
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
          <input type="text" placeholder="Username" size="+50" /><br /><br />
          <input type="password" placeholder="Password" size="+50" /><br /><br />
          <button className="button button1">Login</button><br /><br />
          <p>
            Don't have an account? <a href="registration-page.html">Register here</a>
          </p>
        </div>
      </body>
    </html>
  );
}

export default LoginPage;