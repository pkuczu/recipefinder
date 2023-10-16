import React, { useState } from 'react';
import pizzaLogo from './assets/pizza.png'; // Import the rotating pizza image
import './App.css';
import HomePage from './webpage';
import LoginPage from './login-page';
import RegistrationPage from './registration-page';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={styles.appContainer}>
      <div style={styles.logoContainer}>
        <a target="_blank">
          <img src={pizzaLogo} className="logo pizza" alt="Rotating Pizza" /> {/* Use the rotating pizza image */}
        </a>
      </div>
      <h1 style={styles.appTitle}>Recipe Finder</h1>
      <HomePage /> {/* Render the HomePage component here */}
    </div>
  );
}

const styles = {
  appContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: '', // Reverted to the default background color
    height: '100vh',
  },
  logoContainer: {
    marginTop: '20px', // Adjust the margin-top as needed to move the logo closer to the top
  },
  appTitle: {
    fontSize: '40px',
    fontFamily: 'sans-serif', // Reverted to the default font
  },
};

export default App;