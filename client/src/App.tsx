import React, { useState } from 'react';
import ReactDOM from 'react-dom/client'; // For React 18 and above
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Login from './Login'; // Import the Login component

const App: React.FC = () => {
  // State for the response from backend when button is clicked
  const [response, setResponse] = useState('');

  // Function to handle button click and send request to the backend
  const handleTestButtonClick = async () => {
    try {
      const res = await fetch(`${process.env.BACKEND_URL}/v1/test`, { method: 'GET' });
      const data = await res.json();
      setResponse(data.message); // Assuming backend returns { message: "Success" }
    } catch (error) {
      console.error('Error:', error);
      setResponse('Failed to reach backend');
    }
  };

  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> |
        <Link to="/login">Login</Link>
      </nav>
      <Routes>
        <Route path="/" element={<HomePage onButtonClick={handleTestButtonClick} response={response} />} />
        <Route path="/login" element={<Login />} /> {/* Route to login page */}
      </Routes>
    </Router>
  );
};

// HomePage component that includes the button to send request
const HomePage: React.FC<{ onButtonClick: () => void; response: string }> = ({ onButtonClick, response }) => {
  return (
    <div>
      <h1>Welcome to the App!</h1>
      <button onClick={onButtonClick}>Test Backend</button>
      {response && <p>Response: {response}</p>}
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(<App />);

export default App;
