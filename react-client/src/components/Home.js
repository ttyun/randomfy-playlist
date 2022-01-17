import axios from 'axios';
import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import AudiotrackIcon from '@mui/icons-material/Audiotrack';
import Header from './Header';
import SimpleButton from './SimpleButton';
import Dropdown from './Dropdown';
import { genreTypeOptions } from '../data/genreTypes';
import { textColor } from '../constants';

const textMargin = {
   margin: '5px 0'
}

function Home() {
   // React method to set state in non-React component
   const [isGenerated, setIsGenerated] = useState(false);
   const [songsAdded, setSongsAdded] = useState([]);
   const [genreTypes, setGenreTypes] = useState([]);

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

   function clearResults() {
      setIsGenerated(false);
      setSongsAdded([]);
   }

   function setResults(res) {
      setIsGenerated(true);
      setSongsAdded(res['data']['added_tracks']);
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
      let genres = genreTypes.map(genreType => genreType['value']);
      let genresJson = [];

      genres.forEach(genre => {
         genresJson.push({'value': genre})
      });

      clearResults();
      const config = {
         headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem("accessToken"),
         },
         params: {
            genres
         }
      }

      axios.get("http://127.0.0.1:5000/playlists", config).then(res => {
         console.log(res);
         setResults(res);
      });
   }

   return (
      <Box
         sx={{
            minHeight: '100vh',
            backgroundImage: `url('${process.env.PUBLIC_URL}/home.jpg')`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            backgroundAttachment: 'fixed',
            fontFamily: 'Raleway'
         }}
      >
         <Box
            sx={{
               display: 'flex',
               justifyContent: 'center',
               alignItems: 'center',
               color: 'white'
            }}
         >
            <Header />
            <Box
               sx={{
                  margin: '20% 0 0 0',
                  textAlign: 'center'
               }}
            >
               <h1>Welcome to your Randomfy Spotify Playlist Generator.</h1>
               <h4>You've authenticated and it's finally time to fire up the playlist generator.</h4>
               <h5>Go ahead and hit the button to randomly generate a Spotify playlist for yourself and enjoy.</h5>
               <Dropdown type="genre" options={genreTypeOptions} setGenreTypes={setGenreTypes} />
               <SimpleButton onClick={generatePlaylist.bind(this)} title='Generate' icon={<AudiotrackIcon />}/>
               {isGenerated && 
                  <div>
                     <h2>Completed!</h2>
                     <Box
                        sx={{
                           textAlign: 'start',
                           marginTop: '20px',
                           border: '1px solid white'
                        }}
                     >
                        {songsAdded.map((songAdded) => (
                           <Box
                              sx={{
                                 padding: '10px 16px',
                                 margin: '20px 0',
                                 borderBottom: '1px solid white',
                                 boxShadow: '1px 3px 5px rgba(0,0,0,0.1)'
                              }}
                           >
                              <h2 style={textMargin}>{songAdded.name}</h2>
                              <p style={textMargin}>{songAdded.artist}</p>
                              <p style={textMargin}>{songAdded.album}</p>
                           </Box>
                        ))}
                     </Box>
                  </div>
               }
            </Box>
         </Box>
      </Box>
   );
}

export default Home;