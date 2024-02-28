//C:\react-js\myreactdev\src\App.js
import React, { } from 'react';
import './App.css';
 
import {BrowserRouter, Routes, Route} from 'react-router-dom';
 
import Login from './components/Login.js'
import Profile from './components/Profile.js'
import Dashboard from './components/Dashboard.js'
import {RequireToken} from './components/Auth.js'
 
function App() {
  return (
    <div className="vh-100 gradient-custom">
    <div className="container">
      <h1 className="page-header text-center">Onboarding, Welcome and Matrix emailing</h1>
  
      <BrowserRouter>
        
  
        <Routes>
            <Route path="/" element={<Login />} />
            <Route
              path="/profile"
              element={
                <RequireToken>
                  <Profile />
                </RequireToken>
              }
            />
            <Route
              path="/dashboard"
              element={
                <RequireToken>
                  <Dashboard />
                </RequireToken>
              }
            />
            
        </Routes>
      </BrowserRouter>
    </div>
    </div>
  );
}
  
export default App;