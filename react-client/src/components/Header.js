import { AppBar, IconButton, Toolbar, Collapse } from "@mui/material";
import SortIcon from '@mui/icons-material/Sort';
import { Box } from "@mui/system";
import {
   CLIENT_ID,
   SPOTIFY_AUTHORIZE_ENDPOINT,
   REDIRECT_URL_AFTER_LOGIN,
   SCOPES_URL_PARAM
} from '../SpotifyCredentials.js';

function Header() {
   function handleLogin() {
      window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
      console.log(window.location);
   }

   return (
      <Box
         sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: '100vh'
         }}
      >
         <AppBar elevation={0}
            sx={{
               background: 'none',
               fontFamily: 'Nunito'
            }}
         >
            <Toolbar
               sx={{
                  width: '80%',
                  margin: '0 auto'
               }}
            >
               <Box
                  sx={{
                     flexGrow: '1'
                  }}
               >
                  <h1>Randomfy Playlist</h1>
               </Box>
               <IconButton>
                  <SortIcon
                     sx={{
                        color: 'white',
                        fontSize: '2rem'
                     }}
                  />
               </IconButton>
            </Toolbar>
         </AppBar>
         <Collapse in={true}>
            <Box>
               <button onClick={handleLogin}>Authenticate with Spotify</button>
            </Box>
         </Collapse>
      </Box>
   );
}

export default Header;