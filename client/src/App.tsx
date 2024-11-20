import React, { useState } from 'react';
import axios from 'axios';

const App: React.FC = () => {
  const [response, setResponse] = useState<string>('');

  const handleButtonClick = async () => {
    try {
      const res = await axios.get('http://localhost:8080/v1/test');
      setResponse(res.data.message);
    } catch (error) {
      setResponse('Error connecting to the backend!');
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Frontend to Backend Communication</h1>
      <button onClick={handleButtonClick}>Send Request</button>
      <p>Response from backend: {response}</p>
    </div>
  );
};

export default App;
