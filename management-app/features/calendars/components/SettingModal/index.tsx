import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  FormGroup,
  FormControlLabel,
  Switch,
} from "@mui/material";

type Props = {
  open: boolean;
  onClose: () => void;
};

const style = {
  position: "absolute" as "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  // border: "2px solid #000",
  borderRadius: "10px",
  boxShadow: 24,
  p: 4,
};

const SettingModal = ({ open, onClose }: Props) => {
  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>営業日設定</DialogTitle>
      <DialogContent>
        <FormGroup>
          <FormControlLabel control={<Switch />} label="営業日" />
        </FormGroup>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} variant="outlined">
          キャンセル
        </Button>
        <Button onClick={onClose} color="primary" variant="contained">
          保存
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default SettingModal;
