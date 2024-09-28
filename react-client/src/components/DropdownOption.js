import { components } from "react-select";
import Box from '@mui/material/Box';

function DropdownOption(props) {
   return (
      <div>
         <components.Option {...props}>
            <Box
               sx={{
                  textAlign: 'left'
               }}
            >
               <input
                  type="checkbox"
                  checked={props.isSelected}
                  onChange={() => null}
               /> {" "}
               <label>{props.label}</label>
            </Box>
         </components.Option>
      </div>
   );
}

export default DropdownOption;