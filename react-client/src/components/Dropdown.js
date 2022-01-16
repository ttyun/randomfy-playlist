import React, { useState } from 'react';
import { default as ReactSelect } from "react-select";
import Box from '@mui/material/Box';
import DropdownOption from "./DropdownOption";

function Dropdown(props) {
   const [optionSelected, setOptionSelected] = useState(null);

   function handleChange(selected) {
      setOptionSelected(selected);
      console.log(optionSelected);
   }

   return (
      <Box
         sx={{
            fontFamily: 'sans-serif',
            color: 'black',
            marginBottom: '20px',
            textAlign: 'left'
         }}
      >
         <ReactSelect
            options={props.options}
            isMulti
            closeMenuOnSelect={false}
            hideSelectedOptions={false}
            components={{
               Option: DropdownOption
            }}
            onChange={handleChange.bind(this)}
            allowSelectAll={true}
            value={optionSelected}
         />
      </Box>
   );
}

export default Dropdown;