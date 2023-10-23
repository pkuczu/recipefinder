import React from 'react';

const RegisterPage = () => {
  return (
    <div style={styles.pageContainer}>
      <header style={styles.header}>
        <a href="login" className="button button1" style={styles.loginButton}>
          Back to Home
        </a>
      </header>
      <div className="register-form">
        <h2 style={styles.title}>Register</h2>
        <form>
          <div className="form-group">
            <label htmlFor="username">Username:</label>
            <input type="text" id="username" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input type="password" id="password" />
          </div>
          <div className="form-group">
            <label htmlFor="confirmPassword">Confirm Password:</label>
            <input type="password" id="confirmPassword" />
          </div>
          <button type="submit" style={styles.registerButton}>Register</button>
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

export default RegisterPage;