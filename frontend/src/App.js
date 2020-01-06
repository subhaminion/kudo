import React from 'react';
import './App.css';
import Navbar from './Components/Navbar';
import Mykudos from './Components/Mykudos';
import Userlist from './Components/Userlist';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Mykudos />
      <Userlist />

    </div>
  );
}

export default App;
