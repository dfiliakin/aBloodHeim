import React, { useState } from 'react';

const Guild: React.FC = () => {
    // State for the response from backend when button is clicked
    const [response, setResponse] = useState('');

    // Function to handle button click and send request to the backend
    const handleTestButtonClick = async () => {
        try {
            const token = sessionStorage.getItem('authToken');

            if (!token) {
                throw new Error('User is not authenticated');
            }

            const res = await fetch(`${process.env.BACKEND_URL}/v0/test`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                }
            },);

            if (!res.ok) {
                throw new Error('Failed to fetch');
            }

            const data = await res.json();
            setResponse(data.message); // Assuming backend returns { message: "Success" }

        } catch (error) {
            console.error('Error:', error);
            alert('HTTPS Error: Self-signed certificate issue in development');
        }
    };

    return (
        <GuildPage onButtonClick={handleTestButtonClick} response={response} />
    );
};

// HomePage component that includes the button to send request
const GuildPage: React.FC<{ onButtonClick: () => void; response: string }> = ({ onButtonClick, response }) => {
    return (
        <div>
            <h1>Guild!</h1>
            <button onClick={onButtonClick}>Test Backend</button>
            {response && <p>Response: {response}</p>}
        </div>
    );
};


export default Guild;
