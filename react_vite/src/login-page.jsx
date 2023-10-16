import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleLogin = () => {
    // Replace this with your actual authentication logic.
    // For example, you can make an API request to validate user credentials.

    if (username === 'exampleUser' && password === 'examplePassword') {
      // Successful login, navigate to the user's dashboard.
      history.push('/dashboard');
    } else {
      // Handle failed login (e.g., show an error message).
    }
  };

  return (
    <div>
      <h1 align="center">
        <em>
          <strong>
            <font size="+5"> Recipe Finder </font>
          </strong>
        </em>
      </h1>
      <div className="topnav" align="center">
        <input
          type="text"
          placeholder="Username"
          size="+50"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <br />
        <input
          type="password"
          placeholder="Password"
          size="+50"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <br />
        <button className="button button1" onClick={handleLogin}>
          Login
        </button>
        <br />
        <p>
          Don't have an account? <a href="registration-page.html">Register here</a>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;