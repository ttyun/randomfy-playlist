import { AppBar, IconButton, Toolbar } from "@mui/material";
import SortIcon from '@mui/icons-material/Sort';
import { Box } from "@mui/system";
import { textColor } from '../constants';

function Header() {
   return (
      <AppBar elevation={0}
         sx={{
            background: 'none',
            fontFamily: 'Raleway'
         }}
      >
         <Toolbar
            sx={{
               width: '80%',
               margin: '0 auto',
               color: textColor
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
                     color: textColor,
                     fontSize: '2rem'
                  }}
               />
            </IconButton>
         </Toolbar>
      </AppBar>
   );
}

export default Header;