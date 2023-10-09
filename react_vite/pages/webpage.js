import React from 'react';

function HomePage() {
  return (
    <html>
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>Recipe Finder</title>
        <style>
          {`
            * {box-sizing: border-box;}

            .button {
              border: none;
              color: white;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              position: absolute;
              margin: 3px 2px;
              cursor: pointer;
            }
            .button1 {background-color: #4CAF50;} /* Green */
          `}
        </style>
      </head>
      <body style={{ backgroundColor: 'aquamarine' }}>
        <a href="login-page.html" className="button button1">Log in</a>
        <h1 align="center">
          <em>
            <strong>
              <font size="+5"> Recipe Finder </font>
            </strong>
          </em>
        </h1>
        <div className="topnav" align="center">
          <input type="text" placeholder="Search Recipes" size="+100" />
        </div>
      </body>
    </html>
  );
}

export default HomePage;




