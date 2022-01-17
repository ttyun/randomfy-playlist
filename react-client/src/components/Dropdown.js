import React, { useState } from 'react';
import { default as ReactSelect, components } from "react-select";
import Box from '@mui/material/Box';
import DropdownOption from "./DropdownOption";

function Dropdown(props) {
   const [optionSelected, setOptionSelected] = useState(null);

   const Menu = props => {
      const optionSelectedLength = props.getValue().length || 0;
      return (
         <components.Menu {...props}>
            {
               optionSelectedLength < 2 ?
               (props.children) : (
                  <div style={{ margin: 15 }}>Max genres selected</div>
               )
            }
         </components.Menu>
      );
   };

   function handleChange(selected) {
      setOptionSelected(selected);
      props.setGenreTypes(selected);
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
               Option: DropdownOption,
               Menu: Menu
            }}
            onChange={handleChange.bind(this)}
            allowSelectAll={true}
            value={optionSelected}
         />
      </Box>
   );
}

export default Dropdown;