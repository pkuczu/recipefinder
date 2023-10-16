import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';
import HomePage from './App';
import LoginPage from './login-page';
import RegistrationPage from './registration-page';

function MainApp() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={App} />
        <Route path="/home" component={HomePage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/registration" component={RegistrationPage} />
      </Switch>
    </Router>
  );
}

export default MainApp;