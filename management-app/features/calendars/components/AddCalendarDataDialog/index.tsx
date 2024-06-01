import {
  Dialog,
  DialogContent,
  DialogTitle,
  Select,
  MenuItem,
  SelectChangeEvent,
  DialogActions,
  Button,
  Box,
} from "@mui/material";
import { useState } from "react";

type Props = {
  open: boolean;
  onClose: () => void;
};

const AddCalendarDataDialog = ({ open, onClose }: Props) => {
  const createNumbers = (start: number, end: number) => {
    const numbers = [];
    for (let i = start; i <= end; i++) {
      numbers.push(i);
    }
    return numbers;
  };
  const months = createNumbers(1, 12);
  const years = createNumbers(2020, 2030);

  const [selectedMonth, setSelectedMonth] = useState<number>(1);
  const [selectedYear, setSelectedYear] = useState<number>(2024);

  const handleChangeMonth = (event: SelectChangeEvent) => {
    setSelectedMonth(+event.target.value);
  };

  const handleChangeYear = (event: SelectChangeEvent) => {
    setSelectedYear(+event.target.value);
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>カレンダーデータの追加</DialogTitle>
      <DialogContent>
        <Box sx={{ display: "flex", gap: "5px" }}>
          <Select value={selectedYear.toString()} onChange={handleChangeYear}>
            {years.map((year) => (
              <MenuItem key={year} value={year}>
                {year}年
              </MenuItem>
            ))}
          </Select>
          <Select value={selectedMonth.toString()} onChange={handleChangeMonth}>
            {months.map((month) => (
              <MenuItem key={month} value={month}>
                {month}月
              </MenuItem>
            ))}
          </Select>
        </Box>
      </DialogContent>
      <DialogActions sx={{ display: "flex", gap: "5px" }}>
        <Button onClick={onClose} variant="outlined">
          キャンセル
        </Button>
        <Button onClick={onClose} variant="contained">
          追加
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default AddCalendarDataDialog;
