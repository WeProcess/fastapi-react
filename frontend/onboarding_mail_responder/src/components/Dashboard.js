//C:\react-js\myreactdev\src\components\Profile.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";
import { fetchToken } from "./Auth.js";

export default function Profile() {
  const navigate = useNavigate();
  const [userdata, setUserData] = useState("");
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [usertype, setUserType] = useState("");
  const [userdepartment, setUserDepartment] = useState("");
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted with:", {
      firstname,
      lastname,
      email,
      password,
      usertype,
      userdepartment,
    });
    setShowModal(true);
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
            setUserData(response.data["current_user"]);
            console.log(response.data["current_user"]);
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
            <nav className="navbar">
              <div className="container">
                <h2>Welcome, {userdata.full_name}</h2>
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
            <div className="container">
              <div className="form-layout">
                <form onSubmit={handleSubmit}>
                  <div className="form-group">
                    <input
                      className="form-control-md"
                      type="text"
                      id="firstname"
                      placeholder="First Name"
                      value={firstname}
                      onChange={(e) => setFirstName(e.target.value)}
                      required
                    />
                    <input
                      type="text"
                      id="lastname"
                      placeholder="Last Name"
                      value={lastname}
                      onChange={(e) => setLastName(e.target.value)}
                      required
                    />
                  </div>
                  <div className="form-group">
                    <input
                      type="email"
                      id="email"
                      placeholder="Email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      required
                    />
                    <input
                      type="password"
                      id="password"
                      placeholder="Password"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                    />
                  </div>
                  <div className="form-group">
                    <input
                      type="text"
                      id="usertype"
                      placeholder="User Type"
                      value={usertype}
                      onChange={(e) => setUserType(e.target.value)}
                      required
                    />
                    <input
                      type="text"
                      id="userdepartment"
                      placeholder="User Department"
                      value={userdepartment}
                      onChange={(e) => setUserDepartment(e.target.value)}
                      required
                    />
                  </div>

                  <div class="d-grid gap-2 col-6 mx-auto">
                    <button
                      class="btn btn-primary"
                      type="submit"
                      name="submit"
                      id="submit"
                      value="Login"
                      onClick={handleSubmit}
                    >
                      Login
                    </button>
                  </div>
                </form>
                {showModal && (
                  <div className="modal">
                    <div className="modal-content">
                      <span
                        className="close"
                        onClick={() => setShowModal(false)}
                      >
                        &times;
                      </span>
                      <h2>Form Submission Result</h2>
                      <p>
                        First Name: {firstname} <br />
                        Last Name: {lastname} <br />
                        Email: {email} <br />
                        User Type: {usertype} <br />
                        User Department: {userdepartment} <br />
                      </p>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
