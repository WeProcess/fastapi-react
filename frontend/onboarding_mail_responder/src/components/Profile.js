//C:\react-js\myreactdev\src\components\Profile.js
import React, { } from "react";
import {useNavigate, Link} from "react-router-dom";
 
export default function Profile(){
    const navigate = useNavigate();
    const signOut = () => {
        localStorage.removeItem('karmaglobaltech')
        navigate("/");
    }
    return(
        
        <>
    
        <nav className="navbar bg-primary">
            <div className="container">
            <div>
                <Link to="/profile" className="btn btn-success">Profile</Link> | <Link to="/dashboard" className="btn btn-success">Dashboard</Link>  | <Link to="/usertype" className="btn btn-success">User Type</Link> 
            </div>
        </div>
        </nav>
            <div style = {{marginTop: 20 }}>
                <div>
                    <button type = 'button' className="btn btn-success" onClick= {signOut}>Sign Out</button>
                </div>
            </div>
             
        
        </>
    )
}