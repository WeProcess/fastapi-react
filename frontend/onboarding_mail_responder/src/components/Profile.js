//C:\react-js\myreactdev\src\components\Profile.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";
import { fetchToken } from "./Auth.js";

export default function Profile() {
  const navigate = useNavigate();
  const [userdata, setUserData] = useState("");
  const signOut = () => {
    localStorage.removeItem("karmaglobaltech");
    navigate("/");
  };

  async function getUserData() {
    try {
      var token = fetchToken();
      if (token) {
        axios({
          method: "get",
          responseType: "json",
          url: "http://localhost:8000/dashboard",
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + token,
          },
        })
          .then(function (response) {
            setUserData(response.data["current_user"].full_name);
          })
          .catch(function (error) {
            console.log(error, "error");
            if (
              (error.response.status === 401) &
              (error.response.data.detail === "Could not validate credentials")
            ) {
              localStorage.removeItem("karmaglobaltech");
              navigate("/");
            }
          });
      } else {
        localStorage.removeItem("karmaglobaltech");
        navigate("/");
      }
    } catch (error) {
      alert("Error in try." + error);
    }
  }
  useEffect(() => {
    getUserData();
  }, []);
  return (
    <div className="container">
      <div className="d-flex justify-content-center">
        <div className="card-1">
          <div className="container">
            <nav className="navbar ">
              <div className="container">
                <h2>Welcome, {userdata}</h2>
                <div>
                  <Link to="/profile" className="btn btn-success">
                    Profile
                  </Link>{" "}
                  |&nbsp;
                  <Link to="/dashboard" className="btn btn-success">
                    Dashboard
                  </Link>{" "}
                  |&nbsp;
                  <Link to="/usertype" className="btn btn-success">
                    User Type
                  </Link>{" "}
                  |&nbsp;
                  <Link to="/userteam" className="btn btn-success">
                    User Team
                  </Link>{" "}
                  |&nbsp;
                  <Link to="/user" className="btn btn-success">
                    User
                  </Link>{" "}
                  |&nbsp;
                  <Link to="/matrix" className="btn btn-success">
                    Matrix
                  </Link>{" "}
                  |&nbsp;
                  <Link to="/email" className="btn btn-success">
                    Email
                  </Link>
                </div>
              </div>
            </nav>
            <div style={{ marginTop: 20 }}>
              <div className=" d-flex justify-content-end">
                <button
                  type="button"
                  className="btn btn-success d-flex justify-content-end"
                  onClick={signOut}
                >
                  Sign Out
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
