import Box from '@mui/material/Box';
import Header from './Header.js';
import SimpleButton from './SimpleButton.js';
import LockOpenIcon from '@mui/icons-material/LockOpen';
import { textColor } from '../constants';
import {
   CLIENT_ID,
   SPOTIFY_AUTHORIZE_ENDPOINT,
   REDIRECT_URL_AFTER_LOGIN,
   SCOPES_URL_PARAM
} from '../SpotifyCredentials.js';

function Login() {
   function handleLogin() {
      window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
      console.log(window.location);
   }

   return (
      <Box
         sx={{
            minHeight: '100vh',
            backgroundImage: `url('${process.env.PUBLIC_URL}/loginMain.jpg')`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            backgroundAttachment: 'fixed'
         }}
      >
         <Header />
         <Box
            sx={{
               display: 'flex',
               justifyContent: 'center',
               alignItems: 'center',
               height: '100vh'
            }}
         >
            <SimpleButton onClick={handleLogin} title='Authenticate' icon={<LockOpenIcon />}/>
         </Box>
      </Box>
   );
}

export default Login;