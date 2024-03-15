//C:\react-js\myreactdev\src\App.js
import React from "react";
import "./App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./components/Login.js";
import Profile from "./components/Profile.js";
import Dashboard from "./components/Dashboard.js";
import UserType from "./components/User_Type.js";
import UserTeam from "./components/User_Team.js";
import User from "./components/User.js";
import Matrix from "./components/Matrix.js";
import Email from "./components/Email.js";

import { RequireToken } from "./components/Auth.js";

function App() {
  return (
    <div className="vh-100 gradient-custom">
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

          <Route
            path="/usertype"
            element={
              <RequireToken>
                <UserType />
              </RequireToken>
            }
          />

          <Route
            path="/userteam"
            element={
              <RequireToken>
                <UserTeam />
              </RequireToken>
            }
          />

          <Route
            path="/user"
            element={
              <RequireToken>
                
                <User />
              </RequireToken>
            }
          />

          <Route
            path="/matrix"
            element={
              <RequireToken>
                <Matrix />
              </RequireToken>
            }
          />

          <Route
            path="/email"
            element={
              <RequireToken>
                <Email />
              </RequireToken>
            }
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
