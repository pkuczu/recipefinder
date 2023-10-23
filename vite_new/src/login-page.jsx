import React from 'react';

const LoginPage = () => {
  return (
    
    <div style={styles.pageContainer}>
            <div className="card"> </div>
            <div className="card"></div>
            <div className="card"></div>
      <header style={styles.header}>
        <a href="/" className="button button1" style={styles.loginButton}>
          Back to Home
        </a>
      </header>
      <div className="login-form">
        <h2 style={styles.title}>Log In</h2>
        <form>
          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input type="password" id="password" />
          </div>
          <button type="submit" style={styles.loginButton}>Log In</button>
        </form>
      </div>
      <p className="read-the-docs">
        Made by Team 47
      </p>
    </div>
  );
};

const styles = {
  pageContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '0vh',
    backgroundColor: 'aquamarine',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    width: '100%',
    padding: '20px',
  },
  loginButton: {
    backgroundColor: 'green', // Add a green background color
    color: 'white',
    padding: '10px 20px',
    textDecoration: 'none',
    fontSize: '16px',
    cursor: 'pointer',
    borderRadius: '5px', // Add rounded corners
  },
  title: {
    fontSize: '24px',
  },
};

export default LoginPage;