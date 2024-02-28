//C:\react-js\myreactdev\src\components\Profile.js
import React, { useState, useEffect } from "react";
import axios from 'axios';
import {useNavigate, Link} from "react-router-dom";
import {fetchToken} from './Auth.js';

 
export default function Profile(){
    const navigate = useNavigate();
    const [userdata,setUserData] = useState('');
    useEffect(() => {
        getUserData();
        
    }

    );
    async function getUserData() {
        try {

            var token = fetchToken();
            // alert(token);
            if(token)
            {
                
                // console.log('axios');
                axios({
                    method: 'get',
                    responseType: 'json',
                    url: 'http://localhost:8000/dashboard',
                    headers: {
                        'Content-Type': "application/json",
                        Authorization: "Bearer " + token,
                    }
                })
                .then(function (response) {
                    // console.log(response.data["current_user"]);
                    setUserData(response.data["current_user"].full_name);
                    
                })
                .catch(function (error) {
                    console.log(error, 'error');
                    if(error.response.status === 401 & error.response.data.detail === "Could not validate credentials" )
                    {
                        localStorage.removeItem('karmaglobaltech')
                        navigate("/");
                    }
                });
                
            }
            else
            {
                localStorage.removeItem('karmaglobaltech')
                navigate("/");
            }    
        
        } catch (error) {
        alert("Error in try." + error);
      }
    };
    return(
        <div className="vh-100 gradient-custom">
    <div className="container">
            
        <p><Link to="/" className="btn btn-success">Logout</Link> | <Link to="/profile" className="btn btn-success">Profile</Link> | <Link to="/dashboard" className="btn btn-success">Dashboard</Link> </p>
            <div style = {{minHeight: 800, marginTop: 20 }}>
                <h1>Dashboard Page</h1>
                <p>Hi, {userdata} this is your Dashboard</p>
            </div>
             
            </div>
            </div>
    )
}