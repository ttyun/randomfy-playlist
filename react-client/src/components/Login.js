import Box from '@mui/material/Box';
import Header from './Header.js';

function Login() {
   return (
      <Box
         sx={{
            minHeight: '100vh',
            backgroundImage: `url('${process.env.PUBLIC_URL}/homepage.jpg')`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat'
         }}
      >
         <Header />
      </Box>
   );
}

export default Login;