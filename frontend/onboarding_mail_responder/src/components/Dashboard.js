//C:\react-js\myreactdev\src\components\Profile.js
import React, { useState, useEffect } from "react";
import axios from 'axios';
import {useNavigate, Link} from "react-router-dom";
import {fetchToken} from './Auth.js';

 
export default function Profile(){
    const navigate = useNavigate();
    const [userdata,setUserData] = useState('');
   
    async function getUserData() {
        try {

            var token = fetchToken();
            if(token)
            {
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
                    setUserData(response.data["current_user"]);
                    console.log(response.data["current_user"])
                    
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
    useEffect(() => {
        getUserData();
    }, []);
    return(
        <>
            <div>
                <h2>Hi, {userdata.full_name}</h2>
            </div>
            <nav className="navbar bg-primary">
            <div className="container">
            <div>
                <Link to="/profile" className="btn btn-success">Profile</Link> |&nbsp;
                <Link to="/dashboard" className="btn btn-success">Dashboard</Link> |&nbsp;
                <Link to="/usertype" className="btn btn-success">User Type</Link> |&nbsp;
                <Link to="/userteam" className="btn btn-success">User Team</Link> |&nbsp;
                <Link to="/user" className="btn btn-success">User</Link> |&nbsp;
                <Link to="/matrix" className="btn btn-success">Matrix</Link> |&nbsp;
                <Link to="/email" className="btn btn-success">Email</Link>
            </div>
        </div>
        </nav>
            
             
            
            </>
    )
}