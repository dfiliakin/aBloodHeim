import React, { useState } from 'react';
import ReactDOM from 'react-dom/client'; // For React 18 and above
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Login from './Login'; // Import the Login component
import ProtectedRoute from './components/ProtectedRoute';
import Guild from './Guild';

const App: React.FC = () => {
  // State for the response from backend when button is clicked
  const [response, setResponse] = useState('');

  return (
    <Router>
      <nav>
        <Link to="/login">Login</Link>  |
        <Link to="/guild">Guild</Link>
      </nav>
      <Routes>
        <Route path="/" element={<HomePage response={response} />} />
        <Route path="/login" element={<Login />} /> {/* Route to login page */}
        <Route
          path="/guild"
          element={
            <ProtectedRoute>
              <Guild />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
};

// HomePage component that includes the button to send request
const HomePage: React.FC<{ response: string }> = ({ response }) => {
  return (
    <div>
      <h1>Welcome to the App!</h1>
      {response && <p>Response: {response}</p>}
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(<App />);

export default App;
