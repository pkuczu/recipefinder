import React from 'react';
import { useState } from 'react';
import './App.css'

const HomePage = () => {
  const [ingredientList, setIngredients] = useState([{ service: "" }]);
  
  const sendIngredientsToBackend = (ingredients) => {
    const backendEndpoint = 'REPLACE WITH ACTUAL URL OF BACKEND API';
  
    fetch(backendEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ingredients }),
    })
      .then((response) => {
        if (response.ok) {
          console.log('Ingredients sent to the backend successfully.');
        } else {
          console.error('Failed to send ingredients to the backend.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };
  const handleServiceChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...ingredientList];
    list[index][name] = value;
    setIngredients(list);
  };

  const handleServiceRemove = (index) => {
    const list = [...ingredientList];
    list.splice(index, 1);
    setIngredients(list);
  };

  const handleServiceAdd = () => {
    setIngredients([...ingredientList, { service: "" }]);
  };

  
  return (
    
    <div style={styles.pageContainer}>
      <header style={styles.header}>
        <a href="login" className="button button1" style={styles.loginButton}>
          Log in
        </a>
      </header>
      <form className="App" autoComplete="off">
      <div className="form-field">
        <label htmlFor="service">Ingredients</label>
        {ingredientList.map((singleService, index) => (
          <div key={index} className="services">
            <div className="first-division">
              <input
                name="service"
                type="text"
                id="service"
                value={singleService.service}
                onChange={(e) => handleServiceChange(e, index)}
                required
              />
              {ingredientList.length - 1 === index && ingredientList.length < 4 && (
                <button
                  type="button"
                  onClick={handleServiceAdd}
                  className="add-btn"
                >
                  <span>+ Ingredient</span>
                </button>
              )}
            </div>
            <div className="second-division">
              {ingredientList.length !== 1 && (
                <button
                  type="button"
                  onClick={() => handleServiceRemove(index)}
                  className="remove-btn"
                >
                  <span>Remove</span>
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
      <div className="output">
        <h2>List</h2>
        {ingredientList &&
          ingredientList.map((singleService, index) => (
            <ul key={index}>
              {singleService.service && <li>{singleService.service}</li>}
            </ul>
          ))}
          <button  style={{ paddingLeft: '10px' }}onClick={sendIngredientsToBackend(ingredientList)}>
          Search for Recipes
        </button >
      </div>
      
      <div >
        
      </div>
      
    </form>
      <p id="bottom" className="read-the-docs">
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

export default HomePage;