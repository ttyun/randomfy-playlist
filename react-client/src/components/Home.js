import axios from 'axios';
import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';

function Home() {
   // React method to set state in non-React component
   const [isGenerated, setIsGenerated] = useState(false);

   // React method to call "side effect"
   // Effectively the callback function is called whenever
   // DOM changes (componentDidMount and componentDidUpdate)
   useEffect(() => {
      if (window.location.hash) {
         const { access_token, expires_in, token_type } =
            authorizeWithSpotify(window.location.hash);
         localStorage.clear();
         localStorage.setItem("accessToken", access_token);
         localStorage.setItem("tokenType", token_type);
         localStorage.setItem("expiresIn", expires_in);
      }
   });

   function clearIsGenerated() {
      setIsGenerated(false);
   }

   function toggleIsGenerated() {
      setIsGenerated(!isGenerated);
   }

   function authorizeWithSpotify(hash) {
      const stringAfterHashtag = hash.substring(1);
      const paramsInUrl = stringAfterHashtag.split("&");
      const paramsSplitUp = paramsInUrl.reduce((accumulater, currentValue) => {
         const [key, value] = currentValue.split("=");
         accumulater[key] = value;
         return accumulater;
      }, {});
    
      return paramsSplitUp;
   };

   function generatePlaylist() {
      clearIsGenerated();
      const config = {
         headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem("accessToken"),
         }
      }

      axios.get("http://localhost:5000/playlists", config).then(res => {
         console.log(res);
         toggleIsGenerated();
      });
   }

   return (
      <Box
         sx={{
            minHeight: '100vh',
            backgroundImage: `url('${process.env.PUBLIC_URL}/homepage.jpg')`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            color: 'green',
            fontFamily: 'Nunito'
         }}
      >
         <div>
            <h1>Welcome [NAME].</h1>
            <button onClick={generatePlaylist.bind(this)}>Generate Playlist!</button> 
            {isGenerated && <h3>Completed!</h3>}
         </div>
      </Box>
   );
}

export default Home;