import React, { useState } from 'react';
import axios from 'axios';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();
    setIsLoading(true);
    setErrorMessage('');

    try {
      // Make a POST request to your FastAPI backend
      const response = await axios.post(`${process.env.BACKEND_URL}/v1/login`, {
        username,
        password,
      });

      // Handle successful login (e.g., save token, redirect user)
      console.log('Login successful:', response.data);
      // For now, let's just log the response
      alert('Login successful');
    } catch (error: any) {
      // Handle error (invalid credentials, server errors)
      setErrorMessage(`Invalid username or password: ${process.env.BACKEND_URL}/v1/login`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ width: '300px', margin: '0 auto', paddingTop: '50px' }}>
      <h2>Login</h2>
      {errorMessage && <div style={{ color: 'red' }}>{errorMessage}</div>}
      <form onSubmit={handleLogin}>
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>
        <button type="submit" disabled={isLoading} style={{ width: '100%', padding: '10px' }}>
          {isLoading ? 'Logging in...' : 'Login'}
        </button>
      </form>
    </div>
  );
};

export default Login;
