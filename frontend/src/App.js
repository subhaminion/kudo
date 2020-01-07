import React from 'react';
import './App.css';
import Login from './Components/Login';
import Profile from './Components/Profile';
import PrivateRouter from './Components/PrivetRouter';

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

function App() {
  return (
    <div className="App">
    <Router>
    	<Switch>
	    	<Route path='/' exact component={Login} />
	    	<PrivateRouter component={Profile} path="/profile" exact />
		</Switch>
    </ Router>
    </div>
  );
}

export default App;
