//C:\react-js\myreactdev\src\components\Login.js
import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { setToken, fetchToken } from "./Auth.js";

export default function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = () => {
    if (username.length === 0) {
      alert("Username has left Blank!");
    } else if (password.length === 0) {
      alert("password has left Blank!");
    } else {
      // console.log('axios');
      axios({
        method: "post",
        responseType: "json",
        url: "http://localhost:8000/login",
        data: {
          username,
          password,
        },
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
        .then(function (response) {
          // console.log("Hii " + response.data["token_type"]);
          // console.log(response);
          // alert(response.data["message"])
          // alert(response);
          if (response.data["message"] === "Login failed") {
            alert("Login failed");
          } else {
            if (response.data["access_token"]) {
              setToken(
                response.data["access_token"],
                response.data["token_type"]
              );
              navigate("/dashboard");
            }
          }
        })
        .catch(function (error) {
          console.log(error, "error");
        });
    }
  };
  return (
    <div>
      <div className="mask d-flex align-items-center gradient-custom-3">
        <div className="container">
          <div className="row d-flex justify-content-center align-items-center">
            <div className="col-12 col-md-9 col-lg-7 col-xl-6">
              <div className="card">
                <h1 className="page-header text-center">
                  Onboarding, Welcome and Matrix emailing
                </h1>
                <div className="card-body p-3">
                  {fetchToken() ? (
                    <p className=" d-flex justify-content-center align-items-center">
                      You are logged in!
                    </p>
                  ) : (
                    <p className="text d-flex justify-content-center align-items-center">
                      Login Account!
                    </p>
                  )}
                  <form>
                    <div className="form-outline mb-4">
                      <input
                        type="text"
                        className="form-control form-control-md"
                        name="username"
                        id="username"
                        value={username}
                        placeholder="Your Email"
                        onChange={(e) => setUsername(e.target.value)}
                      />
                    </div>

                    <div className="form-outline mb-4">
                      <input
                        type="text"
                        className="form-control form-control-md"
                        name="password"
                        id="password"
                        value={password}
                        placeholder="Your Password"
                        onChange={(e) => setPassword(e.target.value)}
                      />
                    </div>
                    <div class="d-grid gap-2 col-6 mx-auto">
                      <button
                        class="btn btn-primary"
                        type="button"
                        name="submit"
                        id="submit"
                        value="Login"
                        onClick={handleSubmit}
                      >
                        Login
                      </button>
                    </div>
                    {/* <div className="d-flex justify-content-center">
                      <input
                        type="button"
                        className="btn btn-info"
                        name="submit"
                        id="submit"
                        value="Login"
                        onClick={handleSubmit}
                      />
                    </div> */}
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
