//C:\react-js\myreactdev\src\components\Profile.js
import React, { useState, useEffect } from "react";
import axios from 'axios';
import {useNavigate, Link} from "react-router-dom";
import {fetchToken} from './Auth.js';

 
export default function Profile(){
    const navigate = useNavigate();
    const [usertypedata, setUsertypeData] = useState([]);
    const [userdata, setuserdata] = useState("");
    
    useEffect(() => {
        getUsertypeData();
    }, []);

    async function getUsertypeData() {
        try {
            var token = fetchToken();
            if(token)
            {
                axios({
                    method: 'get',
                    responseType: 'json',
                    url: 'http://localhost:8000/getUserType',
                    headers: {
                        'Content-Type': "application/json",
                        Authorization: "Bearer " + token,
                    }
                })
                .then(function (response) {
                    setUsertypeData(response.data["user_type"]);
                    setuserdata(response.data["current_user"].full_name);
                     
                    // console.log(response.data);
                    
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
        <>
    
            <nav className="navbar bg-primary">
            <div className="container">
            <div>
                <Link to="/profile" className="btn btn-success">Profile</Link> | <Link to="/dashboard" className="btn btn-success">Dashboard</Link>  | <Link to="/usertype" className="btn btn-success">User Type</Link> 
            </div>
        </div>
        </nav>
        <div>
                <h2>Hi, {userdata}</h2>
            </div>
            <div>
                <table className="table table-striped table-bordered table-hover">
                    <thead>
                    <tr>
                    <th>Sr</th>
                    <th>User Type</th>
                    </tr>
                    </thead>
                    <tbody>
                        {usertypedata.map((usertypedata, index) => (
                            <tr key={usertypedata.id}>
                                <td>
                                    {index+1}
                                </td>
                                <td>
                                    {usertypedata.userType}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
             
            
            </>
    )
}