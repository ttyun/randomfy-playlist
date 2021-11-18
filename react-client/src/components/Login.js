import react, { useEffect } from 'react';
import axios from 'axios';
import React from 'react';
import {
   CLIENT_ID,
   SPOTIFY_AUTHORIZE_ENDPOINT,
   REDIRECT_URL_AFTER_LOGIN,
   SCOPES_URL_PARAM
} from '../SpotifyCredentials.js';

function Login() {
   useEffect(() => {
      console.log(window.location.hash);
      if (window.location.hash) {
         const { access_token, expires_in, token_type } =
            authorizeWithSpotify(window.location.hash);
         localStorage.clear();
         localStorage.setItem("accessToken", access_token);
         localStorage.setItem("tokenType", token_type);
         localStorage.setItem("expiresIn", expires_in);
      }
   });

   function authorizeWithSpotify(hash) {
      const stringAfterHashtag = hash.substring(1);
      const paramsInUrl = stringAfterHashtag.split("&");
      const paramsSplitUp = paramsInUrl.reduce((accumulater, currentValue) => {
         console.log(currentValue);
         const [key, value] = currentValue.split("=");
         accumulater[key] = value;
         return accumulater;
      }, {});
    
      return paramsSplitUp;
   };

   function handleLogin() {
      window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
      console.log(window.location);
   }

   return (
      <div>
         <button onClick={handleLogin}>Authenticate with Spotify</button>
      </div>
   );
}

export default Login;
    
   // handleLogin = ()) => {
   //    // HTTP Request to app server (flask server handling spotify authentication)
   //    axios.get("http://localhost:5000/").then(res => {
   //       console.log(res);
   //    });
   //    console.log("MEH");
   // }