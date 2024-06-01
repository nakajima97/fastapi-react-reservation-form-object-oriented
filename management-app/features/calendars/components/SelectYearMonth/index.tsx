import {
  Box,
  Button,
  MenuItem,
  Select,
  SelectChangeEvent,
} from "@mui/material";
import { useState } from "react";

const SelectYearMonth = () => {
  const [selectedMonth, setSelectedMonth] = useState<number>(1);
  const [selectedYear, setSelectedYear] = useState<number>(2024);

  const createNumbers = (start: number, end: number) => {
    const numbers = [];
    for (let i = start; i <= end; i++) {
      numbers.push(i);
    }
    return numbers;
  };
  const months = createNumbers(1, 12);
  const years = createNumbers(2020, 2030);

  const handleChangeMonth = (event: SelectChangeEvent) => {
    setSelectedMonth(+event.target.value);
  };

  const handleChangeYear = (event: SelectChangeEvent) => {
    setSelectedYear(+event.target.value);
  };

  return (
    <Box sx={{ display: "flex", gap: "10px", alignItems: "center" }}>
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
      <Button variant="contained">のカレンダーを表示する</Button>
    </Box>
  );
};

export default SelectYearMonth;
