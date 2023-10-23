import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'

import LoginPage from '/src/login-page'
import RegisterPage from '/src/registration-page'
import HomePage from '/src/HomePage';
import pizzaLogo from './assets/pizza.png'; // Import the rotating pizza image


import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div >
      <img src={pizzaLogo} style={styles.logo} alt="Rotating Pizza" /> {/* Use the rotating pizza image */}

      </div>
      <h1 >Recipe Finder</h1>
      <div style={styles.under}>

      </div>
      <div >
        <Routes>
          <Route path='/' element={<HomePage />}></Route>
          <Route path='login' element={<LoginPage />}></Route>
          <Route path='registration' element={<RegisterPage />}></Route>
        </Routes>
      </div>
      <div style={styles.logo}>

      </div>

      
    </>
  )
}

const styles = {
  logo: {
    padding: 1,
    alignItems: 'top',
    justifyContent: 'top',
    height: '18vh',
  },
  under: {
    padding: 0,
    height: '5vh',
  },
};

export default App
