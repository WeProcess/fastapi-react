//C:\react-js\myreactdev\src\components\Auth.js
import React, { } from "react";
 
import {
    Navigate ,
    useLocation
  } from "react-router-dom";
export const setToken = (token, type) =>{
    // set token in localStorage
    localStorage.setItem('karmaglobaltech', token)
    localStorage.setItem('token_type', type)
}
export const fetchToken = (token) =>{
    // fetch the token
    return localStorage.getItem('karmaglobaltech')
}
export function RequireToken({children}) {
     
    let auth = fetchToken()
    let location = useLocation();
   
    if (!auth) {
       
      return <Navigate to="/" state={{ from: location }} />;
    }
   
    return children;
}