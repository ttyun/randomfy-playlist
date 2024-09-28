import Button from '@mui/material/Button';
import { Box } from "@mui/system";


function SimpleButton(props) {
    return (
        <Box>
            <Button variant="contained" startIcon={props.icon} onClick={props.onClick}>
                {props.title}
            </Button>
        </Box>
    );
}

export default SimpleButton;