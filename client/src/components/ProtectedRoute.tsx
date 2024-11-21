import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute: React.FC<{ children: React.ReactElement }> = ({ children }) => {
    const token = sessionStorage.getItem('authToken');
    return token ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;
