import React from 'react';


const HomePage = () => {
  return (
    <div style={styles.pageContainer}>
      <header style={styles.header}>
        <a href="login-page.html" className="button button1" style={styles.loginButton}>
          Log in
        </a>
      </header>
      <div className="topnav" align="center">
        <input type="text" placeholder="Search Recipes" size="+100" />
      </div>
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

export default HomePage;