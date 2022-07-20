import React, { useState, useEffect } from 'react';
import './App.css';

function App() {

  const [error, setError] = useState(null); 
  const [day, setDay] = useState('Sun');

  useEffect(() => {
    fetch('http://localhost:8080/api/day?day_num=3')
    .then((res) => setDay(res.data))
    .catch((err) => setError(err.message))
  }, []);

  return (
    <>
    <>Hello</>
    <>{day}{error}</>
    </>
  );
}

export default App;
